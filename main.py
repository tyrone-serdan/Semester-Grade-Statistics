
from pandas import read_excel
import misc

def calculateSample(x: float, x_: float, s: float):
    """ Calculates Sample Standard Deviation

    Args:
        x (int): Raw Score
        x_ (int): Sample Mean
        s (int): Sample Standard Deviation

    Returns:
        [int]: Returns the Standard Score
    """
    rawScore = x
    sampleMean = x_
    sampleStandardDeviation = s
    
    standardScore = (rawScore - sampleMean) / sampleStandardDeviation
    standardScore = round(standardScore, 2)
    return standardScore


def calculatePercentileRank(zscore: float):
    """Calculates the Percentile Rank of the Z Score given

    Args:
        zscore (float): Z Score obtained from Standard Normal Table

    Returns:
        [str]: A string showing the rank in Percent
    """
    pRank = str(zscore * 100)
    
    return pRank + "%"

def obtainZScore(sd: float):
    """This function references a Standard Normal Table created in Excel to determine the area to return

    Args:
        sd (float): Standard Deviation

    Returns:
        [int]: The area under the curve between the Mean z Standard Deviations above the Mean
    """
    zIndex = 0
    
    sheetData = read_excel("Z Scores From 0 to 4.9.xlsx")
    zTable = sheetData.to_dict()
    
    firstTwoDigits = zTable.get('Z')
    
    for i in range(49):
        sdFirstTwoDigits = misc.removelastDigit(sd)
        
        if (firstTwoDigits[i] == sdFirstTwoDigits):
            break
        
        zIndex += 1
    
    for hundredthDigit in zTable:
        if (hundredthDigit == 'Z'):
            continue

        sdLastDigit = misc.getLastDigit(sd)
        getHundredthDigit = misc.getLastDigit(hundredthDigit)
        
        findZScore = zTable[hundredthDigit]
        
        if (getHundredthDigit == sdLastDigit):
            return findZScore[zIndex]
        

# CHANGE VALUES INSIDE .get() TO OTHER SUBJECTS TO GET OUTCOME
      
subjects = misc.subjects
tyroneGrades = misc.tyroneGrades

SD = (calculateSample
                (
                tyroneGrades.get('REED'), 
                subjects.get('REED').get('Mean'), 
                subjects.get('REED').get('SD')
                )
     )

Z = obtainZScore(SD)

rank = calculatePercentileRank(Z)

print(SD)
print(Z)
print(rank)