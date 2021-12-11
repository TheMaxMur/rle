#!/usr/bin/python3
import os

def read_file(filename: str="") -> bytes:
    with open(filename, "rb") as b_file:
        return (b_file.read())

def decode(b_file: bytes=b"") -> list:
    result = []
    i = 0
    while (i < len(b_file)):
        counter = b_file[i] - 128
        if counter < 0:
            tmp = bytearray()
            for j in range(1, -counter + 1):
                tmp.append(b_file[i + j])
            i += -counter + 1
            result.append([counter, tmp])
            #print(result)
        else:
            tmp = bytearray()
            tmp.append(b_file[i + 1])
            result.append([counter, tmp])
            i += 2
    return (result)

def write_file(filename: str="", massive: list=[]) -> None:
    with open(filename, 'wb') as b_file:
        for el in massive:
            if el[0] > 0:
                for _ in range(el[0]):
                    b_file.write(el[1])
            else:
                b_file.write(el[1])

def main(filename: str="") -> int:
    b_file = read_file("./output/" + filename)
    massive = decode(b_file)
    write_file("./decode/" + filename[:-4], massive)
    return (0)

if __name__ == "__main__":
    arr = os.listdir("./output")
    for el in arr:
        main(el)
