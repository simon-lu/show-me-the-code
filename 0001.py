# -*- coding: utf-8
# !/usr/bin/env python

import uuid

with open('key.txt', 'a') as file:
    for i in range(200):
        file.write(str(uuid.uuid1())+'\n')
    file.close()


