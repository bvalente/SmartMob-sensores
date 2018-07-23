#!/usr/bin/python
import json, logging
from comm_services import server_comm, message_to_client, message_to_server, message_from_server
from help_services import print_info, print_operation_instructions


# Client configuration functions
def init_config(my_sock, msg_header, sys_config_info):
    logging.debug('init_config')
    config_info = load_sys_conf(my_sock, config_info)
    msg_header =  add_client_msg_header(config_info)
    return msg_header, config_info

def create_dict():
    logging.debug('create_dict')
    msg_header = {}
    config_info = {}
    return msg_header, config_info

def load_sys_conf(my_sock, config_info):
    logging.debug('load_sys_conf')
    config_info['mode'] = 'CONFIG'
    config_info = server_comm(my_sock, config_info)
    return config_info

def add_client_msg_header(config_info, mode):
    logging.debug('add_client_msg_header')
    msg_header = {}
    msg_header['mode'] = mode
    msg_header['device_mode'] = config_info['device_info']['device_mode']
    msg_header['device_type'] = config_info['device_info']['device_type']
    msg_header['device_name'] = config_info['device_info']['device_name']
    logging.debug('msg_header: {}'.format(msg_header))
    return msg_header

def print_system_config(config_info):
    logging.debug('print_system_config')
    print_info(config_info['device_info'])
    for sensor in config_info['sensor_info']:
        print_info(sensor)
    print_operation_instructions(config_info['device_info']['device_type'])


# CommSever configuration functions
def request_system_config (this_sock, sys_config_info):
    logging.debug('request_sys_conf')
    msg_dev = {}
    msg_dev['mode'] = 'CONFIG'
    message_to_server(this_sock, msg_dev)
    sys_config_info = message_from_server(this_sock)
    return sys_config_info

def reply_system_config (dev_sock):
    logging.debug('reply_system_config')
    dev_config_info = read_sys_conf()
    message_to_client(dev_sock, dev_config_info)
    return dev_config_info


def read_sys_conf():
    logging.debug('read_sys_conf')
    with open('node_config.txt') as json_data:
        data = json.load(json_data)
        json_data.close()
    return data


# Generic configuration functions
