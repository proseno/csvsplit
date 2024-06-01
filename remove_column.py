import csv
import os


promoFolder = 'promo/'
promoNewFolder = 'promo_new/'

for file in os.listdir(promoFolder):
    if file.endswith('.csv'):
        print(file + ' started')
        with open(promoFolder + file, "r") as source:
            reader = csv.reader(source)

            with open(promoNewFolder + file, "w") as result:
                writer = csv.writer(result)
                for r in reader:
                    writer.writerow(r[0:5] + r[6:])
        print(file + ' finished')