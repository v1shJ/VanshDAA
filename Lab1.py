def spi_calculator(grades, credits):
    # the count of credits and grades should match 
    if len(grades) != len(credits):
        return "ERROR: Number of grades and credits don't match"
    
    # the grades and credits should only be positive and within their normal ranges
    for i in grades:
        if 10 < i or i < 0:
            return f"ERROR: Value of grade {i} is Invalid"
    
    for j in credits:
        if 4 < j or j <= 0:
            return f"ERROR: Value of credit {j} is Invalid"
    
    spi = 0
    total_cred = 0
    for i in range(0, len(grades)):
        spi += grades[i]*credits[i]
        total_cred += credits[i]
    spi = spi/total_cred
    
    return spi

def cpi_calculator(spi, sem_cred): 
    if len(spi) not in [i for i in range(1, 9)]:
        return "Error: Invalid Number of Semesters"
    elif len(sem_cred) != len(spi):
        return "Error: Number of Credits and Semesters don't match"
    elif any([cred < 0 for cred in sem_cred]) or any([sp < 0 or sp > 10 for sp in spi]):
        return "Error: Value of Credits or SPIs are invalid"
    else:
        total_cred = 0
        cpi = 0
        for i in range(len(spi)):
            cpi += sem_cred[i]*spi[i]
            total_cred += sem_cred[i]
        cpi = cpi/total_cred
        return cpi


#Testcases for SPI:
#TESTCASCE 1: Length of grades and credits do not match
grades = [9, 9, 10]
credits = [3, 3, 4, 4]
print(spi_calculator(grades, credits))
#TESTCASE 2: 1 of the credits is negative
grades = [10, 8, 9, 10]
credits = [3, -1, 4, 4]
print(spi_calculator(grades, credits))
#TESTCASE 3: 1 of the grades is higher than 10
grades = [9, 9, 14, 10]
credits = [3, 3, 3, 4]
print(spi_calculator(grades, credits))
#TESTCASE 4: NORMAL
grades = [10, 10, 10, 10]
credits = [4, 4, 3, 4]
print(spi_calculator(grades, credits))
#TESTCASE 5: NORMAL
grades = [10, 10, 9, 9]
credits = [4, 4, 4, 3]
print(spi_calculator(grades, credits))

print("\n\n")
#Testcases for CPI:

#TEST CASE 1: Length of the SPI Array is 0
spi = []
sem_cred = [22, 22, 22, 23, 23, 22]
print(cpi_calculator(spi, sem_cred))

spi = [10.0, 11.0, 9.3, 9.6, 9.4, 9.5]
sem_cred = [22, 22, 22, 23, 23, 22]
print(cpi_calculator(spi, sem_cred))

spi = [10.0, 9.53, 9.8, 9.9, 9.6]
sem_cred = [22, 22, -1, 23, 23, 22]
print(cpi_calculator(spi, sem_cred))

spi = [10.0, 9.53, 9.8]
sem_cred = [22, 22, 22, 23, 23, 22]
print(cpi_calculator(spi, sem_cred))

spi = [10.0, 9.53, 9.8, 9.9, 9.6, 9.8]
sem_cred = [22, 22, 22, 23, 23, 22]
print(cpi_calculator(spi, sem_cred))

spi = [10.0, 9.8, 9, 9.6, 9.8, 10.0]
sem_cred = [22, 22, 22, 23, 23, 22]
print(cpi_calculator(spi, sem_cred))
