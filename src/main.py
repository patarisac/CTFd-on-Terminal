#!/usr/bin/env python3
from ctfd import CTFd


def dead(code, msg):
    print(msg)
    exit(code)

def menu():
    print("")

def main():
    team = CTFd()
    if team.login() != 200:
        dead(1, "Login failed.")
    print("Login Success.")
    return 0


if __name__ == "__main__":
    main()
