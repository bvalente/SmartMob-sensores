#!/usr/bin/python
import socket, select, sys, logging
from comm_services import remote_host_IP_address, create_server_socket, connect_to_client, message_from_client, message_to_client
from config_services import request_system_config
from operation_services import system_operation_handler
from exit_services import client_termination
from device_services import init_dev_server
from log_tools import init_logging



#comm_server_host = '10.1.5.1'
#comm_server_host = '127.0.0.1'
comm_server_port = 1102
BACK_LOG = 5
TIME_OUT = 5


def message_handler(my_sock, dev_sock, inputs, sys_config_info):
    logging.debug('Message_handler')
    rxd_msg = {}
    ret_code, msg_rxd = message_from_client(my_sock)
    if (ret_code == True):
        if msg_rxd['mode'] == 'CONFIG':
            sys_config_info = request_system_config (dev_sock, sys_config_info)
            message_to_client(my_sock, sys_config_info)
        elif msg_rxd['mode'] == 'MODE':
            system_operation_handler(my_sock, 'OK', dev_sock, msg_rxd)
        elif msg_rxd['mode'] == 'QUIT':
            inputs = client_termination(my_sock,'client succesfully terminating',inputs)
        else:
            logging.warning('Unknown command')
    return inputs

    logging.debug('remote_host_IP_address')
    try:
        comm_server_host = sys.argv[1]
        logging.debug('comm_server_host: {}'.format(comm_server_host))
    except:
        comm_server_host='127.0.0.1'
        logging.debug('comm_server_host: {}'.format(comm_server_host))
    return comm_server_host

init_logging('comm_srv_log.log')
dev_sock = init_dev_server()
sys_config_info = {}
sys_config_info = request_system_config(dev_sock, sys_config_info)
comm_server_host = remote_host_IP_address(sys.argv)
server_sock = create_server_socket(comm_server_host, comm_server_port, BACK_LOG)
inputs = [server_sock]
logging.warning('Server started successfully')
while True:
    infds, outfds, errfds = select.select(inputs, inputs, [], TIME_OUT)
    if len(infds) != 0:
        for fds in infds:
            if fds is server_sock:
                client_sock, client_addr = connect_to_client(fds)
                inputs.append(client_sock)
            else:
                message_handler(fds, dev_sock, inputs, sys_config_info)
