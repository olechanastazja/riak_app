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
    key = None
    if len(sys.argv) > 1:
        key = sys.argv[1]
    config = parse_config()
    riak_host = config['riak']['host']
    riak_port = config['riak']['port']

    riak_client = RiakClient(riak_host, riak_port)

    with open('data.json') as json_file:
        data = json.load(json_file)

    key = riak_client.add_object(data, key)
    print(riak_client.get_object(key).data)
    riak_client.update_object(key, {"name": "John"})
    print(riak_client.get_object(key).data)
    riak_client.delete_object(key)
    print(riak_client.get_object(key).data)


if __name__ == '__main__':
    main()
