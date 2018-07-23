#!/usr/bin/python
import socket, sys, logging

from comm_services import message_to_server, message_from_server, message_to_client
from config_services import add_client_msg_header



# Server operation functions
def system_operation_handler (my_sock, client_msg, dev_sock, dev_msg):
    logging.debug('System_operation_handler')
    dev_msg['mode'] = 'MANUAL'
    message_to_server(dev_sock, dev_msg)
    #message_to_client(my_sock, client_msg)
