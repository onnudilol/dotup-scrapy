from configparser import ConfigParser
from argparse import ArgumentParser

from operator import itemgetter
import json
import sys

config = ConfigParser()
config.read('../scrapy.cfg')


def dl_links(json_input, output, mode='default'):
    # zeroes out the output file
    open(output, 'w').close()

    with open(json_input) as json_data:
        links = json.load(json_data)
        links.sort(key=itemgetter('id'))

        with open(output, 'a') as out:

            for link in links:
                if mode == 'light':
                    if link['id'] > int(config['files']['dotup_light']):
                        out.write(link['url'] + '\n')

                else:
                    if link['id'] > int(config['files']['dotup']):
                        out.write(link['url'] + '\n')

        if mode == 'light':
            config['files']['dotup_light'] = str(links[-1]['id'])

        else:
            config['files']['dotup'] = str(links[-1]['id'])

        with open('../scrapy.cfg', 'w') as cfg:
            config.write(cfg)


if __name__ == '__main__':
    parser = ArgumentParser(description='Output txt file from json to download with wget.')
    parser.add_argument('--input-json', '-i', help='The json file input.')
    parser.add_argument('--output', '-o', help='The txt file output.')
    parser.add_argument('--mode', '-m', choices=['default', 'light'],
                        default='default', help='The function mode.')
    args = parser.parse_args()

    if len(sys.argv) > 1:
        dl_links(args.input_json, args.output, args.mode)

    else:
        parser.print_help()
