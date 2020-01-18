from sds011 import SDS011
import time
import argparse
import datetime

sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)

#awake device
sensor.sleep(sleep=False) 
time.sleep(20)

pmValue = sensor.query() #(pm2.5,pm10)
if pmValue = None then
	pmValue=(0,0)
data={'PM10': pmValue[1], 'PM2_5': pmValue[0]}
print("data: PM2.5 ",data["PM2_5"]," PM10 ",data["PM10"])

parser = argparse.ArgumentParser(description='Read data from Nova PM sensor.')
#parser.add_argument('--device', default='/dev/ttyUSB0',
#                        help='Device file of connected by USB RS232 Nova PM sensor')
parser.add_argument('--csv', default=None,
                        help='Append results to csv, you can use year, month, day in format')
args = parser.parse_args()

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
sensor.sleep()

