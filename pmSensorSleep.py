from sds011 import SDS011
import time

sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)
#pmValue = sensor.query()
#print(pmValue)
#sensor.sleep()
sensor.sleep(sleep=False) 
time.sleep(15)
pmValue = sensor.query()
print(pmValue)