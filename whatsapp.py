import io
import re
import csv
import datetime as dt

def text_parser_ctwo(string):
    """ this one is for company two """
    lines = string.split("\n")
    new_lst = []
    for i in lines:
        split_i = i.split(",")
        pcs_and_price_with_symbols = split_i[-1].split()
        pcs_and_price_only = [i for i in pcs_and_price_with_symbols if re.search(r"\d+\.*?\d*", i)]
        try:
            pcs = pcs_and_price_only[0]
            price = pcs_and_price_only[1]
            new_lst.append([split_i[0], pcs, price])
        except IndexError:
            pcs = "-"
            price = "-"
            new_lst.append([split_i[0], pcs, price])
    data = io.StringIO()
    csv_writer = csv.writer(data)
    csv_writer.writerow(["description", "QTY", "Price (EUR)"])
    csv_writer.writerows(new_lst)
    return_data = data.getvalue()
    return return_data


