#!/usr/bin/python3
"""
determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    bytes_to_process = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        byte = byte & 0xFF

        if bytes_to_process == 0:
            if (byte & mask1) == 0:
                continue
            elif (byte & (mask1 >> 1)) == (mask1 >> 1):
                bytes_to_process = 1
            elif (byte & (mask1 >> 2)) == (mask1 >> 2):
                bytes_to_process = 2
            elif (byte & (mask1 >> 3)) == (mask1 >> 3):
                bytes_to_process = 3
            else:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
            bytes_to_process -= 1

    return bytes_to_process == 0
