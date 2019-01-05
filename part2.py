import pandas as pd
import settings
import datetime

today = datetime.date.today()
file_name = 'test-2019-01-04'  # settings.file_name + + '-%s' % today

file_output = open(file_name + '.txt', 'r')
while True:
    text = file_output.readline()
    if 'Hi ' in text:
        print(text)

## Work on Parsing Text ##
