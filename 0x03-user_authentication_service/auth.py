#!/usr/bin/env python3

"""
hash password with bcrypt.hashpw
"""

import bcrypt


def hash_password(password: str) -> str:
    """ takes in a password string arguments and returns a string
        The returned string is a salted hash of the input password,
        hashed with bcrypt.hashpw """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
