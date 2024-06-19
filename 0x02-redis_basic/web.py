#!/usr/bin/env python3
""" this script shall obtain an html content from a webpage """
import requests
import redis
x = redis.Redis()
compte = 0


def get_page(url: str) -> str:
    """ This shall fetch the html content of a webpage """
    x.set(f"cached:{url}", count)
    rspo = requests.get(url)
    x.incr(f"count:{url}")
    x.setex(f"cached:{url}", 10, x.get(f"count:{url}"))
    return rspo.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
