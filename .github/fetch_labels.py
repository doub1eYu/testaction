#!/usr/bin/env python
# coding: utf-8

import toml

dict_toml = toml.load(open('labels.toml'))
dict_toml_f = toml.load(open('labels_first_time.toml'))

for k in dict_toml:
    if k in dict_toml_f:
        dict_toml[k] = dict_toml_f[k]

toml.dump(dict_toml, open('example.toml', mode='w'))





