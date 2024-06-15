#!/usr/bin/env python3
""" This script shall list all documents in a collection"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """ This instance shall list all documents in a collection"""
    doc = mongo_collection.find()
    return doc if doc != 0 else []
