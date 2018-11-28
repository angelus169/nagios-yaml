# Bring YAML to Nagios (r) configuration
> Convert configuration written in YAML into Nagios objects definition.

[![Build Status](https://travis-ci.org/angelus169/nagios-yaml.svg?branch=master)](https://travis-ci.org/angelus169/nagios-yaml)

## Installation

### Docker

Pull the latest docker image from the docker hub

```
docker pull angelus169/nagios-yaml
```

### From the repository

```
git clone https://github.com/angelus169/nagios-yaml.git
cd nagios-yaml
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage example

### Using Docker

```
docker run \
    -ti \
    -rm \
    -v ./input/nagios.yml:/usr/src/app/input/nagios.yml \
    -v ./output/objects.cfg:/usr/src/app/output/objects.cfg \
    angelus169/nagios-yaml:latest
```

### From the repository via virtual env

```
python converter.py --help
```

```
python converter.py -i /path/to/file.yml -o /path/to/nagios/objects.cfg
```

Default locations for the input file is input/nagios.yml for the output file output/objects.cfg


## Development setup

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Release History

* 0.0.2
    * Added configuration examples based on the default configuration files from the default Nagios installation
    * Added input file schema validator with some basic rules
    * Updated README file, added some helpful information about usage
    * Updated Make file, added new targets

* 0.0.1
    * Initial release


## Meta

Borys Babii – [@babiyboris](https://twitter.com/babiyboris) – angelus169@gmail.com

Distributed under the Apache license 2.0 license. See ``LICENSE`` for more information.

[https://github.com/angelus169](https://github.com/angelus169/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

[travis-image]: https://img.shields.io/travis/angelus169/nagios-yaml/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/angelus169/nagios-yaml
[wiki]: https://github.com/angelus169/nagios-yaml/wiki
