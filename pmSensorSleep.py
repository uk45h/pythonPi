from sds011 import SDS011
import time
import argparse
import datetime

sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)

#awake device
sensor.sleep(sleep=False) 
time.sleep(15)

parser = argparse.ArgumentParser(description='Read data from Nova PM sensor.')
#parser.add_argument('--device', default='/dev/ttyUSB0',
#                        help='Device file of connected by USB RS232 Nova PM sensor')
parser.add_argument('--csv', default=None,
                        help='Append results to csv, you can use year, month, day in format')
args = parser.parse_args()

data = sensor.query() #(pm2.5,pm10)
logging.info('PM10=% 3.1f ug/m^3 PM2.5=% 3.1f ug/m^3', data[2], data[1])

if args.csv:
	field_list = ['date', 'PM10', 'PM2_5']
    today = datetime.datetime.today()
    data['date'] = today.strftime('%Y-%m-%d %H:%M:%S')
    csv_file = args.csv % {'year': today.year,
                               'month': '%02d' % today.month,
                               'day': '%02d' % today.day,
                               }
    append_csv(csv_file, field_list, data)

#pmValue = sensor.query()
#print(pmValue)

#put to sleep so it will be quite
#sensor.sleep()

print(pmValue)