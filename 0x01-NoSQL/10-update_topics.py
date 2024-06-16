#!/usr/bin/env python3
""" This script shall change all topics of a document based on the name"""
import pymongo
from typing import List


def update_topics(mongo_collection, name, topics):
    """ This instance shall change all topics of document based on name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
