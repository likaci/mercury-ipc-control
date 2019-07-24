#!/usr/bin/python
# -*- coding: UTF-8 -*-

import base64
import json
import sys
from urllib import unquote

import requests
import rsa


# usage
# python mipcc.py admin password http://192.168.2.89:80 '{"method":"do","preset":{"goto_preset": {"id": "1"}}}'
# https://github.com/likaci/mercury-ipc-control

# ref https://github.com/gyje/tplink_encrypt/blob/9d93c2853169038e25f4e99ba6c4c7b833d5957f/tpencrypt.py
def tp_encrypt(password):
    a = 'RDpbLfCPsJZ7fiv'
    c = 'yLwVl0zKqws7LgKPRQ84Mdt708T1qQ3Ha7xv3H7NyU84p21BriUWBU43odz3iP4rBL3cD02KZciXTysVXiV8ngg6vL48rPJyAUw0HurW20xqxv9aYb4M9wK1Ae0wlro510qXeU07kV57fQMc8L6aLgMLwygtc0F10a0Dg70TOoouyFhdysuRMO51yY5ZlOZZLEal1h0t9YQW0Ko7oBwmCAHoic4HYbUyVeU3sfQ1xtXcPcf1aT303wAQhv66qzW '
    b = password
    e = ''
    f, g, h, k, l = 187, 187, 187, 187, 187
    n = 187
    g = len(a)
    h = len(b)
    k = len(c)
    if g > h:
        f = g
    else:
        f = h
    for p in list(range(0, f)):
        n = l = 187
        if p >= g:
            n = ord(b[p])
        else:
            if p >= h:
                l = ord(a[p])
            else:
                l = ord(a[p])
                n = ord(b[p])
        e += c[(l ^ n) % k]
    return e


# ref https://www.cnblogs.com/masako/p/7660418.html
def convert_rsa_key(s):
    b_str = base64.b64decode(s)
    if len(b_str) < 162:
        return False
    hex_str = ''
    for x in b_str:
        h = hex(ord(x))[2:]
        h = h.rjust(2, '0')
        hex_str += h
    m_start = 29 * 2
    e_start = 159 * 2
    m_len = 128 * 2
    e_len = 3 * 2
    modulus = hex_str[m_start:m_start + m_len]
    exponent = hex_str[e_start:e_start + e_len]
    return modulus, exponent


def rsa_encrypt(string, pubkey):
    key = convert_rsa_key(pubkey)
    modulus = int(key[0], 16)
    exponent = int(key[1], 16)
    rsa_pubkey = rsa.PublicKey(modulus, exponent)
    crypto = rsa.encrypt(string, rsa_pubkey)
    return base64.b64encode(crypto)


def get_stok(url, username, password):
    # get key nonce
    print "-get rsa and nonce"
    j = post_data(url, json.dumps({"method": "do", "login": {}}))
    key = unquote(j['data']['key'])
    nonce = str(j['data']['nonce'])
    print "rsa: " + key
    print "nonce: " + nonce

    # encrypt tp
    print "--encrypt password by tp"
    tp_password = tp_encrypt(password)
    tp_password += ":" + nonce
    print "tp_password: " + tp_password

    # rsa password
    print "--encrypt password by rsa"
    rsa_password = rsa_encrypt(tp_password, key)
    print "rsa_password: " + rsa_password

    # login
    d = {
        "method": "do",
        "login": {
            "username": username,
            "encrypt_type": "2",
            "password": rsa_password
        }
    }
    print "--login"
    j = post_data(url, json.dumps(d))
    stok = j["stok"]
    return stok


def post_data(base_url, data, stok=""):
    url = base_url + (("/stok=" + stok + "/ds") if stok else "")
    print "post: " + url + " data: " + data
    r = requests.post(url, data)
    print "response: " + str(r.status_code) + " " + str(r.json())
    return r.json()


if __name__ == '__main__':
    username = str(sys.argv[1])
    password = str(sys.argv[2])
    base_url = str(sys.argv[3])
    data = str(sys.argv[4])
    print "username: " + username
    print "password: " + password
    print "base_url: " + base_url
    print "data: " + data
    post_data(base_url, data, get_stok(base_url, username, password))
