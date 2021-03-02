import math
result=(math.pow(2,4)+7-3*4)/5
print(result)
result2=(math.pow(3,2)+1)*(math.fmod(16,7))/7
print(result2)
import datetime
today=datetime.date.today()
print("Today is",today)
distance=16637000000
speed=38241*24
km=1.609344
AU=92955887.6
hourradio=(((299792458/1000)/km)*60)*60
days=int(input("How many days since September 25th, 2009? "))
result3=((days*speed)+distance)
print("The Voyager is",result3,"miles from the sun.")
print("The Voyager is",result3*km,"kilometers from the sun.")
print("The Voyager is",result3/AU,"Astronomical Units from the sun.")
print("It would take",(result3*2)/hourradio,"hours for a radio transmission to be sent and recieved from Voyager.")