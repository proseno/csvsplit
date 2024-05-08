import csv
from mapping import mapLocalesAndLanguage

promoFolder = 'promo/'
promoNewFolder = 'promo_new/'

for lang, locales in mapLocalesAndLanguage.items():
    fileInitContent = []
    fileContent = []
    filename = promoFolder + lang + '.csv'
    resultFilename = promoNewFolder + lang + '.csv'

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headerRow = header = next(reader)
        storeIndex = header.index('store_view_code')
        for row in reader:
            fileInitContent.append(row)

        for locale in locales:
            for row in fileInitContent:
                newRow = row.copy()
                newRow[storeIndex] = locale
                fileContent.append(newRow)

    with open(resultFilename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headerRow)
        writer.writerows(fileContent)
