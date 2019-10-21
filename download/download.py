#!/usr/bin/env python
import requests

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")
    with open(file_name[-1], "wd") as out_file:
        out_file.write(get_response.content)

download("https://cdn.pixabay.com/photo/2016/10/20/18/35/sunrise-1756274__340.jpg")