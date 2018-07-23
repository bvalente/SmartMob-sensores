#!/usr/bin/python
import logging

LOG_DATA = True

def init_logging(log_file):
    if LOG_DATA == True:
            #logging.basicConfig(filename=log_file, level=logging.DEBUG)
        logging.basicConfig(filename=log_file, level=logging.DEBUG)
