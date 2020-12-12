import netCDF4 as nc
from netCDF4 import Dataset
from netCDF4 import num2date, date2num
path = '/Users/dongpingping/Documents/个人文件/毕业大论文/Dataset/201003.nc'
# path = '/Users/dongpingping/Desktop/全选.nc'
nc_obj = Dataset(path)
print(nc_obj)

# tim  = nc_obj.variables['time']
#
# print(len(tim))
# data = str(num2date(tim[:],  units=tim.units, calendar=tim.calendar))[:]
#
# # print(data)
# ms  = str(num2date(tim[0],  units=tim.units, calendar=tim.calendar))[:]
# me  = str(num2date(tim[-1], units=tim.units, calendar=tim.calendar))[:]
# print(ms)
# print(me)
