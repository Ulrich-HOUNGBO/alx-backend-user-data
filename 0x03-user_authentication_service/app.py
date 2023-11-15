#!/usr/bin/env python3

"""Flask App"""

from flask import Flask, jsonify, abort, request, redirect
from auth import Auth

app = Flask(__name__)

AUTH = Auth()

app.route('/', methods=['GET'], strict_slashes=False)


def welcome():
    """ GET /
        Return:
          - Welcome message
    """
    return jsonify({"message": "Bienvenue"})
