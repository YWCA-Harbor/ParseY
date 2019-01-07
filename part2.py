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
                new_row.append(row)
                rc_arr.append(new_row)

    # Issue if there are more values in one field than others
    # return print(column, value)
    return print(cc_arr, rc_arr, csv_file_name)
    # write_CSV(cc_arr, rc_arr, csv_file_name)
# Convert field and line to CSV


def write_CSV(column, rows, file_name):
    csv_file = file_name + '-%s' % today

    with open(csv_file + '.csv', 'w') as new_csv:
        csv_writer = csv.writer(new_csv)
        csv_writer.writerow(column)

        for row in rows:
            csv_writer.writerow(row)
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

for field in fields_list:
    find_fields(field)
