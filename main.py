
from pandas import read_excel
import misc

def calculateSC(x: float, x_: float, s: float):
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
    
    # Formula for Calculating StandardScore
    standardScore = (rawScore - sampleMean) / sampleStandardDeviation
    
    # Rounds up Standard Score to 2 decimals
    standardScore = round(standardScore, 2)
    
    return standardScore


def calculatePercentileRank(zscore: float):
    """Calculates the Percentile Rank of the Z Score given
    
    Args:
        zscore (float): Z Score obtained from Standard Normal Table
        
    Returns:
        [str]: A string showing the rank in Percent
    """
    # NOTE: The zscore provided from the table
    # has already added 0.5 to the value.
    pRank = str(zscore * 100)
    
    return pRank + "%"

def obtainZScore(standardScore: float):
    """This function references a Standard Normal Table created in Excel to determine the area to return

    Args:
        standardScore (float): Standard Score

    Returns:
        [float]: The area under the curve between the Mean z Standard Deviations above the Mean
    """
    zIndex = 0
    
    sheetData = read_excel("Z Scores From 0 to 4.9.xlsx")
    zTable = sheetData.to_dict()
    
    firstTwoDigits = zTable.get('Z')
    
    for i in range(49):
        sdFirstTwoDigits = misc.removelastDigit(standardScore)
        
        if (firstTwoDigits[i] == sdFirstTwoDigits):
            break
        
        zIndex += 1
    
    for hundredthDigit in zTable:
        if (hundredthDigit == 'Z'):
            continue

        sdLastDigit = misc.getLastDigit(standardScore)
        getHundredthDigit = misc.getLastDigit(hundredthDigit)
        
        findZScore = zTable[hundredthDigit]
        
        if (getHundredthDigit == sdLastDigit):
            return findZScore[zIndex]
        


# These lines of code does the calculations for all the subjects
# And prints out their result

subjects = misc.subjects
tyroneGrades = misc.tyroneGrades
subjectsToCheck = ["REED","Literature","EarthScience","GenMath","Filipino","UCSP","MIL","OralComm","PE"]

for subject in subjectsToCheck:
    standardScore = (calculateSC
                    (
                    tyroneGrades.get(subject), 
                    subjects.get(subject).get('Mean'), 
                    subjects.get(subject).get('SD')
                    )
        )

    Z = obtainZScore(standardScore)

    rank = calculatePercentileRank(Z)

    print("Calculations for The Subject " + subject)
    print("Standard Score = " + str(standardScore))
    print("Z Score = " + str(Z))
    print("Percentile Rank = " + str(rank))
    print("========================")