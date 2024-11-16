import csv

with open('csdl.csv', 'r', newline='') as f:
    users = list(csv.reader(f))


    print(users)
    print(len(users))