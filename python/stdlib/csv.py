#!/usr/bin/env python3

import csv

# Simplest example of reading a CSV file
with open('some.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Reading a file with an alternate format:
with open('passwd', newline='') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)

# Simplest writing example
with open('some.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(someiterable)

# Better interface?

with open('some.csv') as f:
    for line in f:
        print(csv.read(line))

with open('some.csv', mode='w') as f:
    csv.write(line for line in f)

