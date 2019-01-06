import settings
import datetime
import csv


def find_fields(field):
    try:
        with open(text_file_name + '.txt') as file_output:
            for line in file_output:
                if line.count(field):
                    turn_into_CSV(field, line)
    except FileNotFoundError:
        print('Sorry, there was an error due to a text file not being found')
# Read only lines that contain the word in the parameter `field`


def turn_into_CSV(column, value):
    value = sanitize_value(column, value)
    new_row = []

    if len(settings.column_csv_arr) <= 1:
        new_row.append(value)
        settings.rows_csv_arr.append(new_row)
    else:
        for arr in settings.rows_csv_arr:
            arr.append(value)

    if column not in settings.column_csv_arr:
        settings.column_csv_arr.append(column)

    csv_column = settings.column_csv_arr
    csv_rows = settings.rows_csv_arr

    # Issue if there are more values in one field than others
    return print(column, value)
    # return print(csv_column, csv_rows, csv_file_name)
    # write_CSV(csv_column, csv_rows, csv_file_name)
# Convert field and line to CSV


def write_CSV(column, rows, file_name):
    csv_file = file_name + '-%s' % today
    try:
        with open(csv_file + '.csv', 'r') as current_csv:
            csv_reader = csv.reader(current_csv)
            for line in csv_reader:
                print(line)
    except FileNotFoundError:
        with open(csv_file + '.csv', 'w') as new_csv:
            csv_writer = csv.writer(new_csv)
            csv_writer.writerow()
# Writes CSV File


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
text_file_name = 'test-2019-01-04'  # settings.file_name + '-%s' % today
fields_strings = input('Enter fields to search seperated by a comma: ')
fields_list = fields_strings.replace(" ", "").split(',')
csv_file_name = input('Finally, create a name for your Excel Spreadsheet: ')

for field in fields_list:
    find_fields(field)
