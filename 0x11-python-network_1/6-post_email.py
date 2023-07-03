#!/usr/bin/python3
"""Python  script that:
- takes in the URL and email address
- sends a POST request to the URL passed with the email as the parameter
- and displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
