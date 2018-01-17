#!/usr/bin/python
# -*- coding: utf-8 -*-
# Lab 1: Reading data from a file

csv_file = open('/Users/mikeghen/Desktop/dss615-spring-2018/module2/data/ripple_price.csv','r')

for line in csv_file:
    print(line)

csv_file.close()


# Lab 2: Reading data from a CSV file
## Method 1: Treat the file like a file

with open('./data/ripple_price.csv') as csv_file:

    for line in csv_file:
        print(line)

print("outside the with", csv_file)


## Method 2: Use csv module from the Standard Library
import csv

csv_file = open('./data/ripple_price.csv')

csv_reader = csv.reader(csv_file)

for row in csv_reader:
    print(row)

csv_file.close()


#
# # With with...
# with open('./data/ripple_price.csv') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for row in csv_reader:
#         print(row)

# Lab 3: Writing to files
import csv

input_file  = open('./data/ripple_price.csv','r')
output_file = open('./data/ripple_price.tsv','w')

csv_reader = csv.reader(input_file)

for row in csv_reader:

    tsv_row = '\t'.join(row) + '\n'

    output_file.write(tsv_row)

input_file.close()
output_file.flush()
output_file.close()

# # Lab 4: Reading tab seperated value (TSV) files
import csv

with open('./data/ripple_price.tsv') as tsv_file:

    tsv_reader = csv.reader(tsv_file)

    for row in tsv_reader:
        print(row)


# Lab 4: Parsing data to keep what we want
import csv

input_file  = open('./data/LoanStats_2017Q3.csv', 'r')
interesting_columns = ["loan_amnt","funded_amnt","funded_amnt_inv","term","int_rate","installment","grade"]

with open('./data/cleaned_LoanStats_2017Q3.csv', 'w') as output_file:

    csv_reader = csv.reader(input_file)

    # Pop off the first two rows from the CSV file
    credits = csv_reader.next()
    header  = csv_reader.next()


    for row in csv_reader:
        row_count = len(row)
        # NOTE: We only want to keep: "loan_amnt","funded_amnt","funded_amnt_inv",
        #       "term","int_rate","installment","grade"
        print(row)
        output_row = [ row[2],row[3],row[4],row[5],row[6],row[7],row[8] ]
        output_line = ','.join(output_row) + '\n'
        output_file.write(output_line)

input_file.close()


# Lab 5: Parsing data to and casting types
import csv

with open('./data/cleaned_LoanStats_2017Q3.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

    row = csv_reader.next()

    loan_amnt       = int(row[0])
    funded_amnt     = int(row[1])
    funded_amnt_inv = int(row[2])
    term            = int(row[3].strip().split(' ')[0]) # ['36','months']
    int_rate        = float(row[4].replace('%',''))/100
    installment     = float(row[5])
    grade           = row[6]

    print("loan_amnt: ", type(loan_amnt), loan_amnt)
    print("funded_amnt: ", type(funded_amnt), funded_amnt)
    print("funded_amnt_inv: ", type(funded_amnt_inv), funded_amnt_inv)
    print("term: ", type(term), term)
    print("int_rate: ", type(int_rate), int_rate)
    print("installment: ", type(installment), installment)
    print("grade: ", type(grade), grade)




















# End
