import re
import csv
import datetime as dt


def text_parser_ctwo(file_name):
    """ this one is for company two """
    with open(file_name.decode("utf-8")) as file:
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
    split_file_name = file_name.split("\\")
    split_file_name.remove(split_file_name[-1])
    split_file_name.append(f"new_file{now}.csv")
    new_file_name = "\\".join(split_file_name)
    with open(new_file_name, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["description", "QTY", "Price (EUR)"])
        csv_writer.writerows(new_lst)
    return new_file_name

