#!/usr/bin/python3
"""
Helper function to check if a given number is a valid UTF-8 start byte
"""


def validUTF8(data):
    def is_start_byte(byte):
        return (byte & 0b10000000) == 0b00000000

    i = 0
    while i < len(data):
        byte = data[i]

        if is_start_byte(byte):
            if (byte & 0b10000000) == 0b00000000:
                length = 1
            elif (byte & 0b11100000) == 0b11000000:
                length = 2
            elif (byte & 0b11110000) == 0b11100000:
                length = 3
            elif (byte & 0b11111000) == 0b11110000:
                length = 4
            else:
                return False

            if i + length > len(data):
                return False

            for j in range(1, length):
                if (data[i + j] & 0b11000000) != 0b10000000:
                    return False

            i += length
        else:
            return False

    return True
