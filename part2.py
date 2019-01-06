import settings
import datetime
import csv


def find_fields(field):
    try:
        with open(file_name + '.txt') as file_output:
            for line in file_output:
                if line.count(field):
                    turn_into_CSV(field, line)
    except FileNotFoundError:
        print('No file')
# Read only lines that contain the word in the parameter `field`


def turn_into_CSV(column, value):
    value = sanitize_value(column, value)
    first_csv_arr = settings.first_csv_arr

    if column not in first_csv_arr:
        first_csv_arr.append(column)

    # csv_file = input('Finally, create a name for your Excel Spreadsheet: ')
    # csv_file = csv_file + '-%s' % today
    # with open(csv_file + '.csv', 'w') as new_csv:
    #         csv_writer = csv.writer(new_csv)

    # for
    print(first_csv_arr)
    return print(column, value)
# Convert field and line to CSV


def sanitize_value(column, value):
    # Undesirable because makes copy of variable, for now works #
    sanitized_string = value.split(column)[1].rstrip()
    unwanted_char = '!?:;,'

    value = ''.join(
        char for char in sanitized_string if char not in unwanted_char)

    return value
# Removes whitespaces and special charactes in value


settings.part2_gloabls()
today = datetime.date.today()
file_name = settings.file_name + '-%s' % today
fields_strings = input('Enter fields to search seperated by a comma: ')
fields_list = fields_strings.split(',')

for field in fields_list:
    find_fields(field)
