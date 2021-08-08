import json

def loadJsonData(file):
    with open(file, "r") as f:
      data = f.read()
    return data


if __name__ == "__main__":
  print(loadJsonData("jsondata.json"))