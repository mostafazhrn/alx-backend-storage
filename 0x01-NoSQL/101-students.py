#!/usr/bin/env python3
""" This script shall return all students sorted by average score"""
import pymongo


def top_students(mongo_collection):
    """ This instance shall return all students sorted by average score"""
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
