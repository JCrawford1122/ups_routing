# utility.py
# Author: Justin Crawford
# Student ID: 000918681
# Date: 5/17/2020

from datetime import timedelta


def get_time_stamp(timestamp):
    hour = int(timestamp[0:2])
    minutes = int(timestamp[3:5])
    seconds = int(timestamp[6:])
    delta = timedelta(hours=hour, minutes=minutes, seconds=seconds)
    return delta
