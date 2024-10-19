import openpyxl

file = openpyxl.load_workbook('Расписание 14.10-26.10 2024-2025.xlsx')

sheet = file['2 курс']
kurs2 = {}
for column in range(0, sheet.max_column):
    if sheet[5][column].value != None:
        kurs2[f'{sheet[5][column].value}'] = column

test = input('aaa: ')
for row in range(7, sheet.max_row):
    print(sheet[row][kurs2[test]].value)