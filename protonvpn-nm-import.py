#!/usr/bin/env python3

"""ProtonVPN NetworkManager import script.

Usage:
  protonvpn-nm-import.py [options] <username> <password>
  protonvpn-nm-import.py [options] --cleanup
  protonvpn-nm-import.py (-h | --help)

Options:
  -c CONFIG --config=CONFIG     Specify directory containing ProtonVPN config files
  --cleanup                     Remove any NetworkManager connection having 'protonvpn' in the name
  -d --debug                    Enable debugging
  -h --help                     Show this screen
  --version                     Show version

"""

import logging
import os
import re
import subprocess
from pathlib import Path
from collections import Counter


from docopt import docopt


class ProtonVPNConfigs():

    CONFIG_DIR = Path(__file__).absolute().parent / 'configs'

    def __init__(self, username, password, config_dir=None):
        self.username = username
        self.password = password
        self.config_dir = self.CONFIG_DIR
        if config_dir is not None:
            self.config_dir = config_dir
        self.stats = Counter()

    def walk_configs(self):
        logging.info('walking through %s', self.config_dir)
        for root, subdirs, files in os.walk(self.config_dir):
            for config_file in files:
                config_file_path = Path(root) / config_file
                yield config_file_path

    def cleanup(self, sub_str='protonvpn'):
        """
        Delete all NetworkManager connections containing a certain string in their name
        :param sub_str: the string to be searched in the connection name
        :return:
        """
        cmdline = ['nmcli', 'connection']
        output = subprocess.check_output(cmdline)
        for line in output.decode().splitlines():
            m = re.match(r'(?P<name>.*?)\s.*', line)
            if sub_str in m.group('name'):
                self.nm_delete(m.group('name'))

    def import_configs(self):
        for config_file in self.walk_configs():
            con_name = config_file.stem
            if self.nm_exist(con_name):
                self.nm_delete(con_name)
            self.nm_ovpn_import(config_file)
            self.nm_ovpn_set_credentials(con_name)

    def nm_exist(self, con_name):
        cmdline = ['nmcli', 'connection']
        output = subprocess.check_output(cmdline)
        for line in output.decode().splitlines():
            m = re.match(r'(?P<name>.*?)\s.*', line)
            if con_name == m.group('name'):
                return True
        return False

    def nm_delete(self, con_name):
        logging.info('DELETE connection: %s', con_name)
        cmdline = ['nmcli', 'connection', 'delete', con_name]
        subprocess.run(cmdline, check=True, stdout=subprocess.DEVNULL)
        self.stats['deleted'] += 1

    def nm_ovpn_import(self, config_file):
        logging.info('IMPORT %s', config_file.name)
        cmdline = ['nmcli', 'connection', 'import', 'type', 'openvpn', 'file', str(config_file)]
        subprocess.run(cmdline, check=True, stdout=subprocess.DEVNULL)
        self.stats['imported'] += 1
        return config_file.stem

    def nm_ovpn_set_credentials(self, con_name):
        # set username
        cmdline = ['nmcli', 'connection', 'modify', con_name, 'vpn.user-name', self.username]
        subprocess.run(cmdline, check=True, stdout=subprocess.DEVNULL)
        # set password
        cmdline = ['nmcli', 'connection', 'modify', con_name, 'vpn.secrets', 'password={}'.format(self.password)]
        subprocess.run(cmdline, check=True, stdout=subprocess.DEVNULL)


def main():
    args = docopt(__doc__)
    debug = args['--debug']

    log_level = logging.INFO
    if debug:
        log_level = logging.DEBUG
    logging.basicConfig(level=log_level)
    username = args['<username>']
    password = args['<password>']
    config_dir = args['--config']

    pvpn_configs = ProtonVPNConfigs(username, password, config_dir)
    if args['--cleanup']:
        pvpn_configs.cleanup()
    else:
        pvpn_configs.import_configs()
    logging.info('Stats: %s', pvpn_configs.stats)

if __name__ == "__main__":
    main()
