#!/usr/bin/env python3
import requests
import re
from getpass import getpass


class CTFd:
    def __init__(self):
        self.URL = "https://agrihack.ipb.ac.id/"
        self.s = requests.Session()
        self.nonce = None
        self.csrf = None

    def get_nonce(self, target):
        resp = self.s.get(self.URL + target)
        self.nonce = re.findall('<input id="nonce" name="nonce" type="hidden" value="[0-9a-z]+">', resp.text)[0][52:-2]
        return self.nonce

    def get_csrf(self, target):
        resp = self.s.get(self.URL + target)
        self.csrf = re.findall("'csrfNonce': \"[a-z0-9]+\"", resp.text)[0][14:-1]
        return self.csrf

    def login(self):
        user = input("Username: ")
        passw = getpass()
        nonce = self.get_nonce("login")
        body = {"name": user, "password": passw, "_submit": "Submit", "nonce": self.nonce}
        r = self.s.post(self.URL + "login", data=body)
        self.csrf = re.findall("'csrfNonce': \"[a-z0-9]+\"", r.text)[0][14:-1]
        self.s.headers.update({"CSRF-Token": self.csrf})
        return r.status_code

    def submit_flag(self, chall_id, flagz):
        body = {
            "challenge_id": int(chall_id),
            "submission": str(flagz),
        }
        r = self.s.post(self.URL + "api/v1/challenges/attempt", json=body)
        return r
