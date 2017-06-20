#!/usr/bin/env python3

import vk

proxies = {
    'http':  'http://194.67.208.117:3129',
    'https': 'http://194.67.208.117:3129',
}

session = vk.Session()
api = vk.API(session,  proxies=proxies)

print(api.users.get(user_ids=1))
