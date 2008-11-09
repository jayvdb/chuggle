# -*- coding: utf-8  -*-
class Error(Exception):
    """Wikipedia error"""

class NoUsername(Error):
    """Username is not in config.py"""

class NoPage(Error):
    """Page does not exist"""
