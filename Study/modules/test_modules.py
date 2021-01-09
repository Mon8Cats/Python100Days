#import datetime
from datetime import date
import time
import camelcase
from validator import validate_email

'''
#today = datetime.date.today()
today = date.today()
timestamp = time.time()
# print(today)
print(timestamp, today)


camel = camelcase.CamelCase()
text = 'Hello there world'
print(camel.hump(text))
'''
print(validate_email("steve@__gmail.com11111"))
