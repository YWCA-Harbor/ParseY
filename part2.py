import pandas as pd
import settings
import datetime

## Work on Parsing Text ##


def find_fields(field):
    try:
        with open(file_name + '.txt') as file_output:
            return print(file_output.read().count(field))
    except FileNotFoundError:
        print('No file')
# Convert user inputs to CSV


today = datetime.date.today()
file_name = 'test-2019-01-04'  # settings.file_name + + '-%s' % today
fields_strings = input('Enter fields to search seperated by a comma: ')
fields_list = fields_strings.split(',')

for field in fields_list:
    find_fields(field)
