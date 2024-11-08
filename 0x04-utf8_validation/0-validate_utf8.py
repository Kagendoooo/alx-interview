#!/usr/bin/python3
"""
determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    method that determines if a given data set reps a valid UTF-8 encodining
    """
    bytes_num = 0
    mask_1 = 1 << 7
    mask_2 = 1 << 6
    for num in data:
        num &= 0xFF

        if bytes_num == 0:
            mask = 1 << 7
            while mask & num:
                bytes_num += 1
                mask >>= 1

            if bytes_num == 0:
                continue

            if bytes_num == 1 or bytes_num > 4:
                return False
        else:
            if not (num & mask_1 and not (num & mask_2)):
                return False

        bytes_num -= 1

    return bytes_num == 0
