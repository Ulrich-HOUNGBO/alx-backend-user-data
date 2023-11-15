#!/usr/bin/env python3

"""
hash password with bcrypt.hashpw
"""

import bcrypt
from sqlalchemy.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> str:
    """ takes in a password string arguments and returns a string
        The returned string is a salted hash of the input password,
        hashed with bcrypt.hashpw """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """takes in a string email and password arguments and returns None
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            _password = _hash_password(password)
            return self._db.add_user(email, _password)
        except ValueError:
            raise ValueError('email already exists')
