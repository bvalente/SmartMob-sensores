#!/usr/bin/python
import json

def welcome_info():
    print ('*************** WELCOME TO SMART_MOB@IST *************** \n')
    print ('Press <enter> to start running the system on manual mode, or select one of the following commands:\n')
    print ('\tHELP:   online manual information')
    print ('\tCONFIG: system device and sensors configuration')
    print ('\tMODE:  start system operation Default mode = MANUAL')
    print ('\tQUIT:  terminate client execution')

def print_info (my_option):
    #my_option = cmd_menu[cmd]
    print ('\n-------------------------------------------------------------------')
    for key, val in list(my_option.items()):
        print ('\t\t', key, val)

def print_help_menu(cmd_menu, user_command):
    print_info(cmd_menu[user_command[0]])
    if len(user_command) == 2: print_info(cmd_menu[user_command[1]])


def print_operation_instructions(my_device):
    print ('\n-------------------------------------------------------------------')
    print ('Virtual sensors are not available in manual operation')
    print ('To operate the system, please press:')
    if my_device == 'car':
        print ('\tArrow keys to select the car direction')
        print ('\t<ESC> to terminate')
    elif my_device != 'car':
        print ('\t<sensor name>: <operation> (1: ON and 0: OFF)')
        print ('\t<ESC> to terminate')
    print ('\n-------------------------------------------------------------------')

def get_menu_option():
    with open('menu_man.txt') as json_data:
        data = json.load(json_data)
        json_data.close()
    cmd_menu = data['command_info']
    return cmd_menu
