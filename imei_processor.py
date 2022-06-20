from openpyxl import Workbook, load_workbook

# --- Loading workbook --- #
wb = load_workbook("IMEI SCANNING 7TH JUNE 21 FORMULSUZ.xlsx")
sheet_names_lst = wb.sheetnames
ws = wb[sheet_names_lst[0]]

# --- Creating new workbook ---#
new_wb = Workbook()
new_ws = new_wb.active
row_number = 1

# --- Iterating over all the columns --- #
for cols in ws.iter_cols(max_col=7, values_only=True):
    # Assigning the column header that contains the description of the phone
    column_headers = cols[0]
    # Cleaning up the column tuple from None types
    clean_cols = [c_cols for c_cols in cols if c_cols is not None]
    # Usually phone descriptions end with 1 or 2 so here we filter for phones essentially
    if column_headers is not None and column_headers.endswith("1"):
        # Assigning the ONLY IMEI to be put through the IMEI info API
        first_imei = cols[1]
        for cells in clean_cols:
            # Checking to see if the cell only contains numbers
            if isinstance(cells, int):
                # Appending to the new ws and leaving the second IMEI slot empty
                new_ws.append([cells, " ", "Samsung", "MODEL_NUMBER"])
        # imei_detection function here
    # filtering for the second IMEI
    elif column_headers is not None and column_headers.endswith("2"):
        for cells in cols:
            if isinstance(cells, int):
                # Assigning the second IMEI next to the first one we put into the ws above.
                new_ws.cell(row=row_number, column=2, value=cells)
                # Need to keep track of number of rows the s
                row_number += 1

    else:
        # For tablets
        pass
        # print(column_headers)
new_wb.save("19.06.22.xlsx")


