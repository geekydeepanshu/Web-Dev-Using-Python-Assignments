from datetime import datetime

dt=datetime.today()
print(dt)

#Format-1:
d1=dt.strftime("%d-%m-%Y")  #uppercase %Y for 2022
print(d1)
#Format-2:
d1=dt.strftime("%d/%m/%y")    # lowercase %y for 22 
print(d1)
#Format-3:
d1=dt.strftime("%B-%d-%Y")  # %B for August 
print(d1)
#Format-4:
d1=dt.strftime("%d-%b-%Y")  # %B for August 
print(d1)
#Format-5:
d1=dt.strftime("%I:%M %p")  # %I for Hours in 12 hr format and %p for am or pm
print(d1)
#Format-6:
d1=dt.strftime("%H:%M:%S") # %H for 24 hr format
print(d1)
#Format-7:
d1=dt.strftime("%d-%m-%Y and %I:%M %p")   
print(d1)
 
