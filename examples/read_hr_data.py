import sys
sys.path.append('../')

from ast_monitor.hr_sensor import HrSensor


# Where to store data.
path = '../sensor_data/hr.txt'

hr = HrSensor(hr_path=path)
hr.get_hr_data()
