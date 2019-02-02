import os
import warnings


def check_chromedriver():
    BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    DRIVER = os.path.join(BASE, 'bin', 'chromedriver')

    try:
        r = os.stat(DRIVER)
    except FileNotFoundError:
        print("THE CHROME DRIVER IS MISSING")

    if r.st_size != 14780812:
        warnings.warn("This chromedriver might not be the coorect one..", Warning)

if __name__ == '__main__':
    check_chromedriver()