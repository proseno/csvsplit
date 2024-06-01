import csv
from prd_mapping import mapLocalesAndLanguage
from prd_mapping import productCopy
from split_file import split

promoFolder = 'prd_missed_business_template/'
promoNewFolder = 'prd_missed_business/'


def create_import_file(result_filename, header_row, file_content):
    with open(result_filename, 'w', newline='') as csvfile_write:
        writer = csv.writer(csvfile_write)
        writer.writerow(header_row)
        writer.writerows(file_content)


def read_init_file(init_filename):
    file_init_content = []
    with open(init_filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header_row = header = next(reader)
        try:
            store_index = header.index('store_view_code')
        except ValueError:
            store_index = -1
        for row in reader:
            file_init_content.append(row)

    return file_init_content, header_row, store_index


def copy_rows(locales, file_init_content, file_content, store_index):
    if len(locales):
        for locale in locales:
            for row in file_init_content:
                if row[0] in productCopy.keys():
                    for sku, product_type in productCopy[row[0]].items():
                        new_row = [sku, product_type] + row[2:]
                        if store_index == -1:
                            new_row.append('__EMPTY__VALUE__')
                        else:
                            new_row[store_index] = locale
                        file_content.append(new_row)
                new_row = row.copy()
                if store_index == -1:
                    new_row.append('__EMPTY__VALUE__')
                else:
                    new_row[store_index] = locale
                file_content.append(new_row)
    else:
        for row in file_init_content:
            file_content.append(row)
            if row[0] in productCopy.keys():
                for sku, product_type in productCopy[row[0]].items():
                    new_row = [sku, product_type] + row[2:]
                    file_content.append(new_row)


def main():
    # if (True):
    #     split(open('prd_promo/weu.csv', 'r'), row_limit=5000, output_name_template='weu_%s.csv', output_path='prd_promo')


    for region, langs in mapLocalesAndLanguage.items():
        result_filename = promoNewFolder + region + '.csv'
        file_content = []
        for lang, locales in langs.items():
            filename = promoFolder + lang + '.csv'
            (file_init_content, header_row, store_index) = read_init_file(filename)
            copy_rows(locales, file_init_content, file_content, store_index)

        create_import_file(result_filename, header_row, file_content)


main()
