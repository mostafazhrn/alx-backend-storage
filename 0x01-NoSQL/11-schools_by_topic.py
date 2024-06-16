#!/usr/bin/env python3
""" This script shall return the list of school having a specific topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """ This instance shall return lst of school having specific topic"""
    return mongo_collection.find({"topics": {"$in": [topic]}})
