from hashlib import md5
from random import choice
import concurrent.futures


def generate_coin():
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            break
    return s + ' ' + h

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=100) as executor:
        for future in concurrent.futures.as_completed([executor.submit(generate_coin)]):
            print(future.result())
