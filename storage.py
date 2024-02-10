import csv
import pandas as pd
import json

def insertDatatoJson(filePath, objDict):
  with open(filePath, 'w') as file:
    json.dump(objDict, file)

def deletetDataFromJson(filePath, colValueDict):
  targetValue = ""
  targetCol = ""
  for col, value in colValueDict.items():
    targetCol = col
    targetValue = value
  # Read the CSV file into a DataFrame
  with open(filePath, 'r') as file:
    data = json.load(file)
  
  targetIsbn = []
  for key, value in data.items():
    if value[targetCol] == targetValue:
      targetIsbn.append(key)
  
  for isbn in targetIsbn:
    del data[isbn]
  
  with open(filePath, 'w') as file:
    json.dump(data, file)


def updateDatatoCSV(filePath, primaryKey, colValueDict):
  with open(filePath, 'r') as file:
    data = json.load(file)
  
  # targetValue = ""
  # targetCol = ""
  targetIsbn = primaryKey
  for col, value in colValueDict.items():
    targetCol = col
    targetValue = value
    data[targetIsbn][targetCol] = targetValue
  
  with open(filePath, 'w') as file:
    json.dump(data, file)
