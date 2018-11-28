from cerberus import Validator
import yaml


if __name__ == '__main__':
    try:
        schema = eval(open('schema.py', 'r').read())
    except IOError as exception:
        raise exception

    config = {}
    with open('input/nagios.yml', 'r') as stream:
        try:
            config = yaml.load(stream)
        except yaml.YAMLError as exception:
            raise exception

    v = Validator(schema)

    print "Is valid?:"
    print v.validate(config, schema)
    print v.errors
