# Make CSV file
#
# This script creates a CSV file that contains a simple "stray whitespace" error.
#
# The code below makes the file using Faker and injects the whitespace error.
#
# We create a CSV file that looks like data from a hospital about individuals
# that have digestive illnesses.
#
from faker import Faker
from random import randint, normalvariate

fake = Faker()

with open('digestive_illnesses.csv','w') as illnesses_file:
    # Write the illnesses_file header
    header = 'Case ID, SSN, Birth Date, First Name, Last Name, Address, City, ICD9'
    illnesses_file.write(header+'\n')

    # Write rows of data to the illnesses_file, add the error
    row = []
    for i in range(1000):
        first_name     = fake.first_name().ljust(50)
        last_name      = fake.first_name().ljust(50)
        street_address = fake.street_address().ljust(50)
        city           = fake.city().ljust(25)
        birth_date     = fake.date().replace('-','')
        ssn            = fake.ssn().replace('-','')
        icd9           = "%03d"%normalvariate(550, 10)
        identifier     = "%09d"%randint(1, 999999999)
        stray_white_space = '\n'

        row = [ identifier,
                ssn,
                birth_date,
                first_name,
                last_name + stray_white_space, # Here's your issue
                street_address,
                city,
                icd9]

        row = ','.join(row)

        illnesses_file.write(row+'\n')
