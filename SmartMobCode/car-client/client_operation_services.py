#!/usr/bin/python
import socket, sys, keyboard, logging

from functools import partial
from comm_services import message_to_server, message_from_server, message_to_client
from client_config_services import add_client_msg_header


# Client operation functions

def system_handler(sys_config_info, user_command, my_sock):
    logging.debug('system_handler')
    if (len(user_command) != 1) and (user_command[1] == 'AUTO'):
        mode = AUTO
        input('Enter a command to continue: ')
    else:
        controlled_system(sys_config_info, my_sock)

def read_keys(my_sock, msg, event):
    line = ','.join(str(code) for code in keyboard._pressed_events)
    if line != '':
        msg['sens_action'] = line
        print ('This is the key:',line)
        message_to_server(my_sock, msg)


def controlled_system(sys_config_info, my_sock):
    logging.info('Controlled system mod started')
    logging.debug('controlled_system')
    msg = {}
    msg = add_client_msg_header(sys_config_info, 'MODE')
    while True:
        fn = partial(read_keys, my_sock, msg)
        keyboard.hook(fn)
        keyboard.wait('esc')
        keyboard.unhook(fn)
        break
    input ('Controlled system mode is terminating... Press any key to continue.')
