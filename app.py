import service
import db
import csv

db.deleteAllCodes()

with open('data/icd_10_short.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        service.postDiagnosisCode(row[0],row[1])
        print(row[0])