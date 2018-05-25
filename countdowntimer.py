from datetime import datetime as dt #datetime is a thing in a package also calleddatetime
from datetime import timedelta
import time
import replit
print(4%12)
while True:
  current=dt.now()-timedelta(hours=6)
  print(str(24-current.day)+" days\n" +
  str(23-current.hour)+" hours\n"+str(60-current.minute)+" minutes\n"
  +str(60-current.second)+" seconds")
  time.sleep(1)
  replit.clear()
