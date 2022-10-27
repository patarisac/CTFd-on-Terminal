#!/usr/bin/env python3
from ctfd import CTFd
import os
team = CTFd()


def dead(code, msg):
    print(msg)
    print("\nPress enter to quit...", end="")
    input()
    exit(code)

def clear():
    if os.name == 'posix':
        os.system("clear")
    elif os.name == 'nt':
        os.system("cls")

def menu():
    print()
    print("Chose menu :")
    print("[1] See challenges.")
    print("[2] Submit a flag.")

    print("[q] Exit.")


def get_challenges():
    # to do
    return


def submit_a_flag():
    chall_id= input("Please enter challenge id : ")
    try:
        chall_id = int(chall_id)
    except ValueError:
        print("Challenges id must be integer!")
        return
    flagz = input("Please enter the flag : ")
    team.submit_flag(chall_id, flagz)


def main():
    global team
    if not team.login():
        dead(1, "Login Failed.")
    while True:
        clear()
        print(f"Welcome to {team.ctfname} on Terminal!")
        menu()
        op = input(">>> ")

        if op.lower() == 'q':
            clear()
            break
    return 0


if __name__ == "__main__":
    main()
