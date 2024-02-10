def getInput(msgList, optionfunc=None):
  for msg in msgList:
    print(msg)
  inp = int(input("Enter any of the above option in integer: "))
  if optionfunc:
    return optionfunc[inp]
  return inp

def addPrinter(msgDict):
  #print(msgDict)
  resultDict = {}
  for key, value in msgDict.items():
    inp = input(value)
    resultDict[key] = inp
  return resultDict
