import datetime
import re
import openpyxl
from pydantic.v1.datetime_parse import parse_time

file = openpyxl.load_workbook('Расписание.xlsx')
sheet = file['2 курс']

min_num2 = [8, 25, 47, 73, 94]
max_num2 = [23, 46, 71, 90, 105]

num = 1
weekday = 2

faculty_num = {}
for column in range(0, sheet.max_column):
    if sheet[5][column].value != None:
        faculty_num[f'{sheet[5][column].value}'] = column+1

print(faculty_num)

def schedule_of_the_day(num_day:int, weekday:int, faculty:int)->list:
    schedule = []
    end_schedule = []
    for column in range(min_num2[num_day], max_num2[num_day]-1):
        if weekday % 2 != 0:
            if sheet[column][2].value == None or sheet[column][2].value == 'н/ч':
                schedule.append(sheet[column][faculty].value)
        else:
            if sheet[column][2].value == 'ч' or sheet[column][2].value == None:
                if any(sheet[column][faculty].coordinate in merged_range for merged_range in sheet.merged_cells.ranges):
                    schedule.append(sheet[column - 1][faculty].value)
                else:
                    schedule.append(sheet[column][faculty].value)
    for i in schedule:
        if i != None:
            end_schedule.append((re.sub(r'\s+', ' ', i)))
    return end_schedule


print(schedule_of_the_day(num, weekday, faculty_num['Дф-20']))