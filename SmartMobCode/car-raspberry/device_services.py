#!/usr/bin/python
import logging

from comm_services import create_client_socket, connect_to_server
from config_services import read_sys_conf
from gpio_services import read_gpio_conf, control_gpio_car

dev_control_host = '127.0.0.1'
dev_control_port = 10101
FORWARD = 126
BACKWARD = 125
RIGHT = 124
LEFT = 123

# Client operation functions

def init_dev_server():
    logging.debug('init_dev_server')
    dev_sock = create_client_socket()
    connect_to_server(dev_sock, dev_control_host, dev_control_port)
    return dev_sock

def driver_mode(msg_rxd, dev_config_info, gpio_data, pwm_motion_engine):
    logging.warning('driver_mode')
    res = 'not_ok'
    action_list = {}
    action_list = read_gpio_conf('action_request')
    if (msg_rxd['sens_action'] in action_list):
        logging.debug('sens_action {}'.format(msg_rxd['sens_action']))
        action = action_list[msg_rxd['sens_action']]
        if (msg_rxd['device_mode'] == 'physical'):
            res = control_gpio_car(gpio_data, action, pwm_motion_engine)
        dev_config_info['device_status'] = 'on'
    return res

def infrastructure_mode(msg_rxd, dev_config_info, gpio_data):
    logging.warning('infrastructure_mode')
