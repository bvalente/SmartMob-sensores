#!/usr/bin/python
import socket, select, sys, logging
from comm_services import create_server_socket, connect_to_client, message_from_client, message_to_client
from config_services import reply_system_config
from device_services import driver_mode, infrastructure_mode
from gpio_services import read_gpio_conf, gpio_init, gpio_terminate
from log_tools import init_logging


dev_control_host = ''
dev_control_port = 10101
BACK_LOG = 5
TIME_OUT = 5


def device_handler(my_sock, gpio_data, pwm_motor):
    logging.debug('device_handler')
    dev_config_info = {}
    dev_msg_rxd = {}
    ret_code, dev_msg_rxd = message_from_client(my_sock)
    if ret_code == True:
        logging.debug('message_from_client: {}'.format(dev_msg_rxd))
        if dev_msg_rxd['mode'] == 'CONFIG':
            dev_config_info = reply_system_config(my_sock)
        elif dev_msg_rxd['device_type'] == 'car':
            driver_mode(dev_msg_rxd, dev_config_info, gpio_data, pwm_motor)
        else:
            infrastructure_mode(dev_msg_rxd, dev_config_info, gpio_data)

init_logging('dev_log.log')
gpio_data = {}
gpio_data = read_gpio_conf('gpio_pins')

pwm_motor = {}
gpio_init(gpio_data, pwm_motor)

server_sock = create_server_socket(dev_control_host, dev_control_port, BACK_LOG)
inputs = [server_sock]
logging.warning('Device control server successfully created')
while True:
    infds, outfds, errfds = select.select(inputs, inputs, [], TIME_OUT)
    if len(infds) != 0:
        for fds in infds:
            if fds is server_sock:
                client_sock, client_addr = connect_to_client(fds)
                inputs.append(client_sock)
            else:
                res = device_handler(fds, gpio_data, pwm_motor)
