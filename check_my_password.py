import requests
import hashlib
import datetime

def request_api_data(qurey_check):
    url = 'https://api.pwnedpasswords.com/range/' + qurey_check
    responce = requests.get(url)
    if responce.status_code != 200:
        raise RuntimeError(f'ERROR Fatching {responce.status_code}, check the data and try  aging')
    return responce
def password_leaks_count(hashs,  hash_to_check):
    hashs = (line.split(':') for line in hashs.text.splitlines())
    for h, count in hashs:
        if h == hash_to_check:
            return count
    return 0
def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5char, another_char = sha1_password[:5], sha1_password[5:]
    responce1 = request_api_data(first_5char)
    return password_leaks_count(responce1, another_char)

def time_now():
    x = datetime.datetime.now()
    return x.strftime("%c")

def mani(*args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'your {password} password was found {count} time.')
            print("Till " + time_now())
            print('you should change your password.')
        else:
            print(f'your {password} password was not found.')
            print("Till " + time_now())
            print("Always  be safe.")

pw = (input("Enter your password: "))
mani(pw)


