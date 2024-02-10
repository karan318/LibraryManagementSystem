def getInput(msgList, optionfunc=None):
  for msg in msgList:
    print(msg)
  inp = input("Enter response: ")
  if optionfunc:
    return optionfunc[int(inp)]
  return inp

def addPrinter(msgDict):
  #print(msgDict)
  resultDict = {}
  for key, value in msgDict.items():
    inp = input(value)
    resultDict[key] = inp
  return resultDict
