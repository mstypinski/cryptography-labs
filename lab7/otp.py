#!/usr/bin/env python3
import pyotp
import sys

SECRET = "5YALZBSETHXCOJ4ZH6RNJ3GYIOQEBFZI"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Wrong args, provide `at`")
        sys.exit(1)
    print(pyotp.HOTP(SECRET).at(int(sys.argv[1])))