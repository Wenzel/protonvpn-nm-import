# protonvpn-nm-import

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)


> ProtonVPN to NetworkManager import script

## Table of Contents

- [Overview](#overview)
- [Install](#install)
- [Usage](#usage)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Overview

This script will automatically import your ProtonVPN{`server/country/securecore`} configuration files
into `NetworkManager`, preconfigured with your credentials. 

## Requirements

- `Python >= 3.4`
- `python3-docopt`

## Install

To install the dependencies on `Ubuntu`:

~~~
sudo apt-get install python3-docopt
~~~

## Usage

### Import

~~~
protonvpn-nm-import.py [options] <username> <password>
~~~

By default, the script will import **all** the configuration files in `configs` directory (more than `800`).

To import a specific directory, use `--config`:

~~~
protonvpn-nm-import.py --config configs/tcp/country USERNAME PASSWORD
INFO:root:walking through configs/tcp/country
INFO:root:IMPORT fi.protonvpn.com.tcp.ovpn
INFO:root:IMPORT il.protonvpn.com.tcp.ovpn
INFO:root:IMPORT dk.protonvpn.com.tcp.ovpn
INFO:root:IMPORT pt.protonvpn.com.tcp.ovpn
INFO:root:IMPORT fr.protonvpn.com.tcp.ovpn
INFO:root:IMPORT is.protonvpn.com.tcp.ovpn
~~~


### Cleanup

To clean your previous config files:

~~~
protonvpn-nm-import.py --cleanup
INFO:root:DELETE connection: at.protonvpn.com.tcp
INFO:root:DELETE connection: au.protonvpn.com.tcp
INFO:root:DELETE connection: be.protonvpn.com.tcp
INFO:root:DELETE connection: br.protonvpn.com.tcp
INFO:root:DELETE connection: ca.protonvpn.com.tcp
INFO:root:DELETE connection: ch.protonvpn.com.tcp
INFO:root:DELETE connection: cz.protonvpn.com.tcp
INFO:root:DELETE connection: de.protonvpn.com.tcp
~~~

## References

- [ProtonVPN](https://protonvpn.com/): ProtonVPN website

## Maintainers

[@Wenzel](https://github.com/Wenzel)

## Contributing

PRs accepted.

Small note: If editing the Readme, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

[GNU General Public License v3.0](https://github.com/Wenzel/pyvmidbg/blob/master/LICENSE)
