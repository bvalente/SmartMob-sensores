#!/usr/bin/python
import logging
from comm_services import message_to_server, message_from_server, message_from_client, message_to_client
from client_config_services import add_client_msg_header

# Client operation functions
def client_exit_handler(sys_config_info, my_sock):
    logging.debug('client_exit_handler')
    msg = {}
    msg = add_client_msg_header(sys_config_info, 'QUIT')
    message_to_server(my_sock, msg)
    msg_from_server = message_from_server(my_sock)
    logging.warning('client_exit_handler: msg_from_server {}'.format(msg_from_server))
    return msg_from_server

def mod_client_msg_header(msg, mode):
    logging.debug('mod_client_msg_header')
    msg['mode'] = mode
    return msg

# Server operation functions
def client_termination(my_sock, client_data, inputs):
    logging.warning('Client_termination')
    message_to_client(my_sock, client_data)
    inputs.remove(my_sock)
    my_sock.close()
    return inputs
