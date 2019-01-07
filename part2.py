from itertools import repeat
import settings
import datetime
import csv


def find_fields(field):
    try:
        with open(text_file_name + '.txt') as file_output:
            for line in file_output:
                if line.count(field):
                    csv_obj = turn_into_CSV(field, line)
    except FileNotFoundError:
        print('Sorry, there was an error due to a text file not being found')

    return csv_obj
# Read only lines that contain the word in the parameter `field`


def turn_into_CSV(column, value):
    value = sanitize_value(column, value)
    cc_arr = settings.column_csv_arr
    rc_arr = settings.rows_csv_arr
    new_row = []

    if column not in cc_arr:
        cc_arr.append(column)

    rc_length = len(rc_arr)
    cc_length = len(cc_arr)

    if rc_length == 0:
        new_row.append(value)
        rc_arr.append(new_row)
    else:
        for index, row in enumerate(rc_arr):
            if len(row) != cc_length:
                row.append(value)
                break
            elif index == rc_length - 1:
                new_row.extend(repeat('', cc_length - 1))
                new_row.append(value)
                rc_arr.append(new_row)

    return [cc_arr, rc_arr]
# Convert field and line to CSV


def write_CSV(column, rows, file_name):
    csv_file = file_name + '-%s' % today
    column_len = len(column)

    with open(csv_file + '.csv', 'w') as new_csv:
        csv_writer = csv.writer(new_csv)
        csv_writer.writerow(column)

        for row in rows:
            row_len = len(row)
            if row_len != column_len:
                row.extend(repeat('', column_len - row_len))
            csv_writer.writerow(row)

    return print('Congratulations! Your new file is ready!')
# Writes CSV File


def sanitize_value(column, value):
    # Undesirable because makes copy of variable, for now works #
    sanitized_string = value.split(column)[1].rstrip()
    unwanted_char = '!?:;,'

    value = ''.join(
        char for char in sanitized_string if char not in unwanted_char)

    return value.strip()
# Removes whitespaces and special charactes in value


settings.part2_gloabls()
today = datetime.date.today()
text_file_name = 'test-2019-01-04'  # settings.file_name + '-%s' % today
fields_strings = input('Enter fields to search seperated by a comma: ')
fields_list = fields_strings.replace(' ', '').split(',')
csv_file_name = input('Finally, create a name for your Excel Spreadsheet: ')

for index, field in enumerate(fields_list):
    csv_obj = find_fields(field)

column = csv_obj[0]
rows = csv_obj[1]

write_CSV(column, rows, csv_file_name)
