#!/usr/bin/python
import logging, sys

from comm_services import remote_host_IP_address, create_client_socket, connect_to_server
from log_tools import init_logging
from client_help_services import welcome_info, print_help_menu, get_menu_option
from client_config_services import request_system_config, print_system_config
from client_operation_services import system_handler
from client_exit_services import client_exit_handler



comm_server_port = 1102

def controller(my_sock):
    cmd_menu = get_menu_option()
    sys_config_info = {}
    sys_config_info = request_system_config(my_sock, sys_config_info)
    while True:
        in_test = True
        while in_test:
            user_msg = input(' SmartMob >  ')
            if (len(user_msg) != 0):
                in_test=False
        user_command = user_msg.split()
        if user_command[0] == 'HELP':
            print_help_menu(cmd_menu, user_command)
        elif user_command[0] == 'CONFIG':
            sys_config_info = request_system_config(my_sock, sys_config_info)
            print_system_config(sys_config_info)
        elif user_command[0] == 'MODE':
            system_handler(sys_config_info, user_command, my_sock)
        elif user_command[0] == 'QUIT':
            code = client_exit_handler(sys_config_info, my_sock)
            print (' SmartMob > {} Client terminated'. format(code))
            break
        else:
            print (' SmartMob >  Invalid command')

#def main(argv):
init_logging('client_log.log')
logging.info('Client started')
comm_server_host = remote_host_IP_address(sys.argv)
client_sock = create_client_socket()
connect_to_server(client_sock, comm_server_host, comm_server_port)
welcome_info()
controller(client_sock)
logging.info('Client succesfully terminating')
client_sock.close()
