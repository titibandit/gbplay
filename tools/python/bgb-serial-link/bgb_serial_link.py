#!/usr/bin/python3
import argparse
import os
import sys

# Ugliness to do relative imports without a headache
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from common.bgb_link_cable_server import BGBLinkCableServer
from common.serial_link_cable import SerialLinkCableClient

arg_parser = argparse.ArgumentParser(description='Provides BGB <-> serial link cable communication.')
arg_parser.add_argument('--bgb-port', type=int, help='port to listen on for BGB data')
arg_parser.add_argument('serial_port', type=str, help='serial port to connect to')

args = arg_parser.parse_args()

kwargs = { 'port': args.bgb_port } if args.bgb_port is not None else {}
bgb_server = BGBLinkCableServer(**kwargs)

with SerialLinkCableClient(args.serial_port) as serial_link:
    data_handler = lambda b: serial_link.send(b)
    bgb_server.run(data_handler)
