import json
import os

def extract_data(filename="interact/case.json"):
    with open(filename, 'r') as fl:
        data = json.load(fl)

    return data

def info():
    print(os.getcwd())
    print(os.listdir())


if __name__ == "__main__":
    info()
    print(extract_data())