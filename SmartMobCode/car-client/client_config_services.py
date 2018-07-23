#!/usr/bin/python
import json, logging

from comm_services import server_comm, message_to_client, message_to_server, message_from_server
from client_help_services import print_info, print_operation_instructions

# Communication API
# Client side
def request_system_config(this_sock, sys_config_info):
    logging.debug('request_system_config')
    sys_config_request = {}
    sys_config_request['mode'] = 'CONFIG'
    message_to_server(this_sock, sys_config_request)
    sys_config_reply = message_from_server(this_sock)
    return sys_config_reply

# Client configuration functions - generic functions
def print_system_config(config_info):
    logging.debug('print_system_config')
    print_info(config_info['device_info'])
    for sensor in config_info['sensor_info']:
        print_info(sensor)
    print_operation_instructions(config_info['device_info']['device_type'])

def add_client_msg_header(config_info, mode):
    logging.debug('add_client_msg_header')
    msg_header = {}
    msg_header['mode'] = mode
    msg_header['device_mode'] = config_info['device_info']['device_mode']
    msg_header['device_type'] = config_info['device_info']['device_type']
    msg_header['device_name'] = config_info['device_info']['device_name']
    logging.debug('msg_header: {}'.format(msg_header))
    return msg_header
