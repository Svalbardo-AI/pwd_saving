import os
import configparser
import re

work_path = os.getcwd()

letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890`~!@#$%^&*()-=_+[]{}|;:"",.<>?'

config = configparser.ConfigParser()
config.read(work_path + '\\' + 'nicknames.ini', 'utf-8')
nicknames = {}
for i in range(len(config.sections())):
    module_name = config.sections()[i]
    module = config.items(module_name)
    nicknames[module_name] = [a[1] for a in module][0]


def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')


def isExist(elem, dictionary):
    return elem in dictionary


def cal_root(num):
    if 0 < int(num) < 10:
        return num
    else:
        cache = 0
        for a in str(num):
            cache += int(a)
        if cache >= 10:
            return cal_root(cache)
        else:
            return cache


def lock(pwd, alphabet=letters):
    lock_key = str(input('请输入根密码： '))
    alphabet = [a for a in alphabet] * int(lock_key)
    cache_pwd = []
    random_add = cal_root(int(lock_key))
    for i in range(random_add):
        cache_pwd.append(alphabet[(i + random_add) ** 2])
    for i in pwd:
        cache_pwd.append(alphabet[alphabet.index(i) + int(lock_key)])
    for i in range(random_add + 1):
        cache_pwd.append(alphabet[(i + int(lock_key[0])) ** 2])
    return ''.join(cache_pwd)


def unlock(pwd, alphabet=letters):
    lock_key = str(input('请输入根密码： '))
    alphabet = [a for a in alphabet] * int(lock_key)
    random_add = cal_root(int(lock_key))
    true_pwd = []
    for i in pwd[random_add:-random_add - 1]:
        word = alphabet[alphabet.index(i) - (int(lock_key) % len(letters))]
        true_pwd.append(word)
    return ''.join(true_pwd)


def nick_name(name):
    name = name.lower()
    if (name in nicknames) == 1:
        return nicknames[name]
    else:
        print('请检查网站名')



