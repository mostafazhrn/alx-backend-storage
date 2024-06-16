#!/usr/bin/env python3
""" This script shall insert a new document in a collection based on kwargs"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ This instance shall insert new document in collection usin kwargs"""
    nuevo_id = mongo_collection.insert(kwargs)
    return neuvo_id
