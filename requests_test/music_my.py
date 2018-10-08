#coding = utf-8
from Crypto.Cipher import AES
import base64
import requests
import json

headers = {
    'Cookie': 'appver=1.5.0.75771;',
    'Referer': 'http://music.163.com/',
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

first_param = "{rid:\"\", offset:\"0\", total:\"true\", limit:\"20\", csrf_token:\"\"}"
second_param = b"010001"
third_param = b"00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
forth_param = b"0CoJUm6Qyw8W8jud"


def get_params():
    iv = b"0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    h_encText = AES_encrypt(first_param, first_key, iv)
    h_encText = AES_encrypt(h_encText, second_key, iv)
    return h_encText


def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey


def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)

    encryptor = AES.new(key, AES.MODE_CBC, iv)
    text1 = bytes(text, encoding='utf-8')
    print(type(text1))
    encrypt_text = encryptor.encrypt(text1)
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text


def get_json(url, params, encSecKey):
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    response = requests.post(url, headers=headers, data=data)
    return response.content


if __name__ == "__main__":
    url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_486999661?csrf_token=5f7d0bd85f820f6ce199da6ee101e24e"
    params = 'YD8XBwVNRbEDd9Yoll88f+WVoondxO+z8Z7Ai3KPKZ1ZPVCDbiLvn5ep67QzjaXCHMqDvdcPnrjF/aLWhxMjdxZMDtxuZTBPuY2uIfTXYES4KYH2vk9RkHBQRBuVWr5wEQK5m2NT7TCTYEYWs/lpc6FdWPSnXDF1rkXLHZ/v2jtrQxMKgRfX2+ARNAIYfzep1Yhi4nZV42AGxuJT0cm3mwu0cl+2bFLj1xsvulBNuho='

    encSecKey = '935917b1941c7660fff0dee3cd72d76ebf76dc9b9b62ebc6ddcf491b45750b5574e3b3a5811b439a19fc59c2ead6de56f46087f6e344009d036b06168419d8a2b12c12877103994ed90009c21f52c802f743fce7e979581a80c6212b3228f92b631cb10210cc7ab917f253e42c951411c126311ce711e8d8eef3d4749a7f13bd'
    json_text = get_json(url, params, encSecKey)
    print(json_text)
    json_dict = json.loads(json_text)
    print (json_dict['total'])



