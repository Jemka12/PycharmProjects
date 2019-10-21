#!usr/bin/env python

import requests
import re
import urlparse


def extract_links_from(url):
    response = requests.get(url)
    return re.findall(r'(?:href=")(.*?)"', response.content)


target_links = {}
def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urlparse.urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link:
            try:
                target_links[link] += 1
            except KeyError:
                target_links[link] = 0
                print(link)
                crawl(link)



target_url = "http://10.0.2.14/mutillidae/"
crawl(target_url)
