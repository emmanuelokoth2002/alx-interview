#!/usr/bin/python3
"""
Helper function to check if a given number is a valid UTF-8 start byte
"""


def validUTF8(data):
    def is_start_byte(byte):
        return (byte & 0b10000000) == 0b00000000

    i = 0
    for x in data:
        if i == 0:
            if x & 128 == 0:
                i = 0
            elif x & 224 == 192:
                i = 1
            elif x & 240 == 224:
                i = 2
            elif x & 248 == 240:
                i = 3
            else:
                return False
        else:
            if x & 192 != 128:
                return False
            i -= 1
    if i == 0:
        return True
    return False
