#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import urllib3
from pprint import pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class session:
    def __init__(self, url, timeout=10):
        self.Headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Host": "{}".format(url),
            "Origin": "".format(url),
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/99.110.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
    def test(self):
        pprint(self.Headers)


session = session("https://ya.ru")
session.test()
