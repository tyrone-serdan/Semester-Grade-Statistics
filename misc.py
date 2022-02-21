def getLastDigit(digit: float):
    text = digit.__str__()
    lastText = text[text.__len__() - 1]
    lastDigit = int(lastText)
    
    return lastDigit

def removelastDigit(digit: float):
    lastDigit = getLastDigit(digit)
    text = digit.__str__()
    lastText = text.replace(str(lastDigit), '')
    
    newDigit = float(lastText)
    
    return newDigit

def removeDotInDecimal(digit: float):
    text = digit.__str__()
    newDigit = int(text.replace('.', ''))
    
    return newDigit

def changeToDecimal(percent: str):
    newDecimal = float(percent.replace("%", ''))
    
    return newDecimal
    

tyroneGrades = {
    "REED": 97.0,
    "Literature": 97.0,
    "EarthScience": 97.5,
    "GenMath": 93.5,
    "Filipino": 92.0,
    "UCSP": 95.5,
    "MIL": 95.5,
    "OralComm": 95.0,
    "PE": 95.0
}

subjects = {
    "REED": 
        {"Mean": 89.62, "SD": 6.55},
    "Literature": 
        {"Mean": 94.24, "SD": 2.71},
    "EarthScience": 
        {"Mean": 94.34, "SD": 2.17},
    "GenMath": 
        {"Mean": 88.64, "SD": 4.16},
    "Filipino": 
        {"Mean": 91.28, "SD": 4.37},
    "UCSP": 
        {"Mean": 90.88, "SD": 4.23},
    "MIL": 
        {"Mean": 93.42, "SD": 2.61},
    "OralComm": 
        {"Mean": 91.17, "SD": 2.52},
    "PE": 
        {"Mean": 94.91, "SD": 1.33},
}