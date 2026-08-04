#!/usr/bin/env python3
"""This module provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")

    db = client.logs
    collection = db.nginx

    print("{} logs".format(collection.count_documents({})))

    