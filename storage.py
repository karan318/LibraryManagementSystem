import csv
import pandas as pd


def insertDatatoCSV(filePath, obj, headers):
  obj_info = {header: getattr(obj, header, None) for header in headers}

  # Open the CSV file in append mode ('a') and write the object's information
  with open(filePath, 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writerow(obj_info)


def deletetDataFromCSV(filePath, colValueDict):
  targetValue = ""
  targetCol = ""
  for col, value in colValueDict.items():
    targetCol = col
    targetValue = value
  # Read the CSV file into a DataFrame
  df = pd.read_csv(filePath)
  # Filter the DataFrame to keep only rows where the 'isbn' column matches the given key
  filtered_df = df[df[targetCol] == targetValue]
  # If no rows were found, return
  if filtered_df.empty:
    print("Nothing matches here")
    return
  # Delete the filtered rows from the DataFrame
  df.drop(filtered_df.index, inplace=True)


def updateDatatoCSV(filePath, primaryKey, colValueDict):
  df = pd.read_csv(filePath)

  # Step 2: Update the relevant rows
  # Find the row index where the primary key matches
  row_index = df[df[primaryKey] == colValueDict[primaryKey]].index
  # Update each specified column in that row
  for col, value in colValueDict.items():
    if col in df.columns:
      df.at[row_index, col] = value

  # Step 3: Write the updated DataFrame back to the CSV
  df.to_csv(filePath, index=False)
