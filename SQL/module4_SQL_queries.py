PASSENGERS_SURVIVED = '''
SELECT COUNT(Survived) FROM review
where survived = 1'''
PASSENGERS_DIED = '''
SELECT COUNT(Survived) FROM review
where survived = 0
'''
PASSENGERS_PER_CLASS = '''
SELECT COUNT(pclass) FROM review
GROUP BY Pclass
'''
SURVIVORS_BY_CLASS = '''
SELECT count(Survived) FROM review
GROUP BY Pclass
'''
DIED_BY_CLASS = '''
SELECT count(Survived) FROM review
where Survived = FALSE
GROUP BY Pclass
'''
AVERAGE_AGE_SURVIVED_AND_DIED = '''
SELECT AVG(Age)FROM review
GROUP BY Survived
'''
AVERAGE_FARE_BY_PASSENGER_AND_LIVED = '''
SELECT AVG(Fare)FROM review
WHERE Survived = TRUE
GROUP BY Pclass
'''
AVERAGE_FARE_BY_PASSENGER_AND_DIED = '''
SELECT AVG(Fare)FROM review
WHERE Survived = FALSE
GROUP BY Pclass
'''
AVERAGE_SIB_SPOUSE_ONBOARD_SURVIVED = '''

SELECT AVG(SibSp)FROM review
WHERE Survived = TRUE
GROUP BY Pclass
'''
AVERAGE_SIB_SPOUSE_ONBOARD_DIED = '''
SELECT AVG(SibSp)FROM review
WHERE Survived = FALSE
GROUP BY Pclass
'''
AVERAGE_PARCH_ONBOARD_SURVIVED = '''
SELECT AVG(Parch)FROM review
WHERE Survived = TRUE
GROUP BY Pclass'''

AVERAGE_PARCH_ONBOARD_DIED = '''
SELECT AVG(Parch)FROM review
WHERE Survived = TRUE
GROUP BY Pclass'''

SAME_NAMES = '''
SELECT count(name) FROM review
group by name
'''
