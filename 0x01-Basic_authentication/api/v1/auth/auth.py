#!/usr/bin/env python3
""" Module to test the auth module"""

from flask import request

from typing import TypeVar


class Auth:
    """Auth class """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require auth function"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        for i in excluded_paths:
            if path.endswith('*'):
                if path.startswith(i):
                    return False
        if path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        if request is None:
            return None
        if not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user"""
        return None

