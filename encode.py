#!/usr/bin/python3
import os

def read_file(filename: str="") -> bytes:
    with open(filename, "rb") as b_file:
        return (b_file.read())

def create_massive(b_file: bytes=b"") -> list:
    counter = 1
    result = []
    for index in range(1, len(b_file)):
        if b_file[index] == b_file[index - 1]:
            if counter == 127:
                result.append([127, b_file[index - 1]])
                counter = 0
            counter += 1
        else:
            result.append([counter, b_file[index - 1]])
            counter = 1
        if index == len(b_file) - 1:
            result.append([counter, b_file[index]])
    return (result)

def check_non_r(massive: list=[]) -> list:
    result = []
    counter = 0
    string = bytearray()
    for index in range(len(massive)):
        if massive[index][0] == 1:
            if counter == 128:
                if string != bytearray():
                    result.append([-counter + 128, string])
                counter = 0
                string = bytearray()
            string.append(massive[index][1])
            counter += 1
        else:
            if string != bytearray():
                result.append([-counter + 128, string])
            counter = 0
            string = bytearray()
            tmp = bytearray()
            tmp.append(massive[index][1])
            result.append([massive[index][0] + 128, tmp])
            
    if counter > 0:
        result.append([-counter + 128, string])

    return (result)

def write_file(filename: str="", massive: list=[]) -> None:
    with open(filename, 'wb') as b_file:
        for el in massive:
            tmp = bytearray()
            tmp.append(el[0])
            b_file.write(tmp)
            b_file.write(el[1])

def main(filename: str="") -> int:
    b_file = read_file("./input/" + filename)
    massive = create_massive(b_file)
    massive = check_non_r(massive)
    write_file("./output/" + filename + ".enc", massive)
    return (0)

if __name__ == "__main__":
    arr = os.listdir("./input")
    for el in arr:
        main(el)
