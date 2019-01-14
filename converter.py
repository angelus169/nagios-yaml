#!/usr/bin/env python

import yaml
import sys
import os
import argparse
from jinja2 import FileSystemLoader, Environment


def main(arguments):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-i', '--input', help='Input file', default='input/nagios.yml',
                        type=argparse.FileType('r'))
    parser.add_argument('-o', '--output', help='Output file', default='output/objects.cfg',
                        type=argparse.FileType('w'))

    args = parser.parse_args(arguments)
    yaml_content = yaml.safe_load(args.input)
    objects_definition = yaml_content['objects']
    loader = FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates'))
    environment = Environment(loader=loader, trim_blocks=True, keep_trailing_newline=True)
    for object_name in objects_definition:
        objects_template = environment.get_template(object_name + '.j2')
        print objects_template.render(objects=objects_definition[object_name])


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
