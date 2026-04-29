#!/usr/bin/env python3
"""This module writes a Python that lists all documents"""

def list_all(mongo_collection):
    """Returns an empty lists if no document"""
    return list(mongo_collection.find())
