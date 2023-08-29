import openpyxl


def load_column_data_from_excel(excel_file_path):
    # List to store the data from column C
    data_list = []

    # Load the Excel file
    workbook = openpyxl.load_workbook(excel_file_path)
    sheet = workbook.active  # Assume you want to work with the active sheet

    # Loop through the rows, starting from the third row (index 2)
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if len(row) >= 3:  # Ensure there is data in column B
            data_list.append(row[1])  # Assuming column B is at index 1

    return data_list


"""

# Example usage
excel_file_path = 'Search_meaning.xlsx'
data = load_column_data_from_excel(excel_file_path)

# Print each item in the data list
for item in data:
    print(item)
    
"""
