import re
import csv
import datetime as dt

def text_parser_ctwo(file):
    """ this one is for company two """
    lines = file.readlines()
    new_lst = []
    for i in lines:
        split_i = i.split(",")
        pcs_and_price_with_symbols = split_i[-1].split()
        pcs_and_price_only = [i for i in pcs_and_price_with_symbols if re.search(r"\d+\.*?\d*", i)]
        pcs = pcs_and_price_only[0]
        price = pcs_and_price_only[1]
        new_lst.append([split_i[0], pcs, price])
    now = dt.datetime.now().strftime("%d%m%Y")
    new_file_name = now + ".csv"
    with open(new_file_name, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["description", "QTY", "Price (EUR)"])
        csv_writer.writerows(new_lst)
    return csv_file

