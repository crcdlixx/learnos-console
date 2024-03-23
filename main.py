#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import subprocess

a = os.getcwd()
file_path = os.path.join(a, "程序", "index.txt")


def read_index_file(file_path):
    """
    Read the index file and return a list of tuples containing functionality and program paths.
    """
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(' ')
            if len(parts) >= 2:
                function = parts[0]
                program_path = ' '.join(parts[1:])
                data.append((function, program_path))
    return data


def display_menu(data):
    """
    Display the menu with numbered functionality.
    """
    print("菜单")
    for idx, (function, program_path) in enumerate(data, start=1):
        print(f"{idx}. {function} {program_path}")
    print("0. 退出")


def open_program(program_path):
    """
    Open the specified program using python3 command.
    """
    try:
        a = os.getcwd()
        subprocess.run(['python', a + program_path], check=True)
        # print(program_path)
    except FileNotFoundError:
        print(f"错误：在以下位置找不到程序 {program_path}")


# Main program
if __name__ == "__main__":
    programs_data = read_index_file(file_path)
    while True:
        display_menu(programs_data)
        user_input = input("输入要打开的程序编号（0 退出）： ")

        if user_input.isdigit():
            choice = int(user_input)
            if 0 <= choice <= len(programs_data):
                if choice == 0:
                    print("退出程序。")
                    break
                else:
                    _, program_path = programs_data[choice - 1]
                    open_program(program_path)
            else:
                print("无效的选择。请输入一个有效的号码。")
        else:
            print("输入无效。请输入一个有效的号码。")
