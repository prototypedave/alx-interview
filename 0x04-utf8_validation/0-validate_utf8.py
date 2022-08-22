#!/usr/bin/python3
"""
0. UTF-8 Validation
"""


def validUTF8(data):
    bytesLen = 0
    """shifts binary to the left 7 steps"""
    shiftLeft7 = 1 << 7
    """shifts binary to the left 6 steps"""
    shiftLeft6 = 1 << 6
    for byte in data:
        move = 1 << 7
        if bytesLen == 0:
            while byte & move:
                bytesLen += 1
                """ shifts one binary to the right """
                move = move >> 1
            if bytesLen == 0:
                continue
            if bytesLen == 1 or bytesLen > 4:
                return False
        else:
            if not (byte & shiftLeft7 and not (byte & shiftLeft6)):
                return False
        bytesLen -= 1
    if bytesLen == 0:
        return True
    return False
