#!/usr/bin/python
import socket, sys, json, logging

MSG_SIZE = 1024
NULL = ''


# Client communication functions
def remote_host_IP_address(argv):
    logging.debug('remote_host_IP_address')
    try:
        comm_server_host = sys.argv[1]
        logging.debug('comm_server_host: {}'.format(comm_server_host))
    except:
        comm_server_host='127.0.0.1'
        logging.debug('comm_server_host: {}'.format(comm_server_host))
    return comm_server_host


def create_client_socket():
    logging.debug('create_client_socket')
    try:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.warning('client_socket successfully created')
    except socket.error as msg:
        logging.exception('Failed to create socket - Error: {}, -  {}'.format(msg[0], msg[1]))
        sys.exit()
    return my_socket

def connect_to_server(my_sock, host, port):
    logging.debug('connect_to_server')
    try:
        my_sock.connect((host, port))
        logging.warning('Client successfully connected to server- IP address:{}, port {}'.format(host, port))
    except socket.error as msg:
        logging.exception('Failed to connect to server: {}'.format(msg))
        my_sock.close()
        sys.exit()

def message_to_server(my_sock, data):
    logging.debug('message_to_server: {}'.format(data))
    msg_to_server = json.dumps(data)
    encoded_msg = msg_to_server.encode('utf-8')
    try:
        my_sock.send(encoded_msg)
    except socket.error as msg:
        logging.exception('Failed to send message to server: {}'.format(msg))
        my_sock.close()
        sys.exit()

def message_from_server(my_sock):
    try:
        msg_from_server = my_sock.recv(MSG_SIZE)
        logging.debug('message_from_server: {}'.format(msg_from_server))
    except socket.error as msg:
        logging.exception('Failed to receive message from server: {}'.format(msg))
        my_sock.close()
        sys.exit()
    msg_from_server_json = json.loads(msg_from_server.decode('utf-8'))
    return msg_from_server_json

def server_comm(my_sock, data):
    logging.debug('server_comm')
    logging.debug('message_to_server: {}'.format(data))
    message_to_server(my_sock, data)
    msg_from_server = message_from_server(my_sock)
    logging.debug('message_from_server: {}'.format(msg_from_server))
    return msg_from_server

# Server communication functions

def create_server_socket(host, port, back_log):
    logging.debug('create_server_socket')
    try:
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.info('server_socket successfully created')
    except socket.error as msg:
        logging.exception('Failed to create socket - Error: {}, -  {}'.format(msg[0], msg[1]))
        sys.exit()
    try:
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind((host, port))
        logging.debug('server_socket successfully binded')
    except socket.error as msg:
        logging.exception('Failed to bind socket: {}'.format(msg))
        server_sock.close()
        sys.exit()
    server_sock.listen(back_log)
    return server_sock

def connect_to_client(server_sock):
    try:
        sock, addr = server_sock.accept()
        logging.info('server accept connection from client')
    except socket.error as msg:
        logging.exception('Failed to accept connection from client: {}'.format(msg))
        sock = NULL
        addr = NULL
    return sock, addr

def message_to_client(my_sock, data):
    client_data = json.dumps(data)
    try:
        my_sock.send(client_data.encode('utf-8'))
        logging.debug('message_to_client: {}'.format(client_data))
    except socket.error as msg:
        logging.exception('Failed to send message: {}'.format(msg))

def message_from_client(my_sock):
    try:
        data_message = my_sock.recv(MSG_SIZE)
    except socket.error as msg:
        logging.exception('Failed to receive message: {}'.format(msg))
    if (len(data_message) != 0):
        logging.debug('message_from_client: {} with len {}'.format(data_message, len(data_message)))
        try:
            client_data = json.loads(data_message.decode('utf-8'))
            return True, client_data
        except:
            return False, NULL
    else:
        return False, NULL
