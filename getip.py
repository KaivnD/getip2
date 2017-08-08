#!/usr/bin/env python
#
# Gets your public IP address

import requests
import random
import re

servers = [ 'http://ipecho.net/plain', 'http://websiteipaddress.com/WhatIsMyIp',
            'http://getmyipaddress.org/', 'http://myexternalip.com/raw',
            'http://www.canyouseeme.org/', 'http://www.trackip.net/',
            'http://icanhazip.com/', 'http://www.ipchicken.com/',
            'http://whatsmyip.net/', 'http://checkmyip.com/',
            'http://www.lawrencegoetz.com/programs/ipinfo/',
            'http://ip-lookup.net/', 'http://www.myip.ru',
            'http://ipgoat.com/', 'http://www.myipnumber.com/my-ip-address.asp',
            'http://formyip.com/', 'https://check.torproject.org/',
            'http://www.displaymyip.com/', 'http://checkip.dyndns.com/',
            'http://myexternalip.com/', 'http://www.ip-adress.eu/',
            'https://wtfismyip.com/text', 'http://httpbin.org/ip',
            'http://checkip.amazonaws.com', 'http://get.youripfast.com/']


def get():
    page = get_page(random.choice(servers))
    ip = re.search('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',
                    str(page.content))

    if ip is not None and ip.group is not None:
        return ip.group(0)
    else:
        return get()


def get_page(url):
    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    if page.ok:
        return page
    else:
        return get_page(random.choice(servers))


if __name__ == '__main__':
    get()
