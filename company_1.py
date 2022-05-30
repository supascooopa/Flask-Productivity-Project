import camelot
import pandas as pd
import datetime
import numpy as np

def company_number_one(file_name):
    now = datetime.datetime.now().strftime("%d-%m-%Y")
    new_file_name = file_name + now
    joined_coordinates = ["45,779,545,90", "45,779,545,90", "45,779,545,90"]
    tables = []
    pages = 1
    for coordinates in joined_coordinates:
        table = camelot.read_pdf(f"{file_name}",
                                 flavor='stream',
                                 table_areas=[coordinates],
                                 pages=str(pages),
                                 strip_text="\n")
        tables.append(table)
        pages += 1
    no_of_rows = 0
    for pages in tables:
        page_df = pages[0].df
        page_df = page_df.replace(r'^\s*$', np.nan, regex=True)

        try:
            # TODO THE PROBLEM IS WITH THE FILE NAME BEING WRITTEN
            with pd.ExcelWriter(f"{new_file_name}.xlsx",
                                mode="a",
                                engine="openpyxl",
                                if_sheet_exists="overlay") as writer:
                page_df.to_excel(writer, startrow=no_of_rows, index=False, header=False)
                no_of_rows += page_df[page_df.columns[1]].count()
        except FileNotFoundError:
            with pd.ExcelWriter(f"{new_file_name}.xlsx",
                                mode="w",
                                engine="openpyxl", ) as writer:
                page_df.to_excel(writer, index=False)
    return f"{new_file_name}.xlsx"

