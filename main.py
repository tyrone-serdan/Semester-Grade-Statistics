# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
import misc

def calculateSample(x: float, x_: float, s: float):
    """ Calculates sample

    Args:
        x (int): Raw Score
        x_ (int): Sample Mean
        s (int): Sample Standard Deviation

    Returns:
        [int]: Returns a Float number between 0 and 1
    """
    rawScore = x
    sampleMean = x_
    sampleStandardDeviation = s
    
    standardScore = (rawScore - sampleMean) / sampleStandardDeviation
    
    return standardScore


def calculatePercentileRank(zscore: float):
    pRank = str((0.5 + zscore) * 100)
    
    return pRank + "%"

def obtainZScore(sd: float):
    zTable = misc.zTable
    zIndex = 0
    
    sheetData = pd.read_excel("Z Scores From 0 to 4.9.xlsx")
    data = sheetData.to_dict()
    
    firstTwoDigits = zTable.get('Z')
    
    for i in range(49):
        sdFirstTwoDigits = misc.removelastDigit(sd)
        
        if (firstTwoDigits[i] == sdFirstTwoDigits):
            break
        
        zIndex += 1
        
    print(zIndex)
        
        
        
        
    
obtainZScore(2.37)

# sScore = (calculateSample(85,70,15))
# print(calculatePercentileRank(0.3413))