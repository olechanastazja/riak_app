#!/usr/bin/env python3
import configparser
import sys
import json
from RiakClient import RiakClient


def parse_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


def main():
    if len(sys.argv) < 3:
        sys.stderr.write('Usage: python3 main.py operation_type key\n')
        exit(1)

    if sys.argv[2] in ['insert', 'update']:
        sys.stderr.write('Bad operation argument. Available options are:'
                         ' "insert", "update", "delete".\n')
        exit(1)

    config = parse_config()
    riak_host = config['riak']['host']
    riak_port = config['riak']['port']
    key = sys.argv[2]

    riak_client = RiakClient(riak_host, riak_port)

    with open('data.json') as json_file:
        data = json.load(json_file)
        riak_client.add_object(data, key)

    print(riak_client.get_object(key).data)
    riak_client.update_object(key, {"name": "John"})
    print(riak_client.get_object(key).data)
    riak_client.delete_object(key)
    print(riak_client.get_object(key).data)


if __name__ == '__main__':
    main()
