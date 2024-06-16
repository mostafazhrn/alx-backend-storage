#!/usr/bin/env python3
""" This script shall insert a new document in a collection based on kwargs"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ This instance shall insert document in collection based on kwargs"""
    nuevo_id = mongo_collection.insert_one(kwargs)
    return nuevo_id.inserted_id
