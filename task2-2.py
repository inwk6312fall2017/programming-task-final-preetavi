from weather import Weather
weather = Weather()
loc=input("enter the location ")
location = weather.lookup_by_location(loc)
condition = location.condition()
a=[]
# Get weather forecasts for the upcoming days.
lowestTemp=100
coolestDay=0
i=0
for forecasts in location.forecast():
 if i<5:
   b=[]    
   b.append(forecasts['text'])
   b.append(forecasts['date'])
   b.append(forecasts['high'])
   b.append(forecasts['low'])
   a.append(b)
   i+=1

for i in range(5):
 j=int(a[i][3])
 if j<lowestTemp:
  lowestTemp=j
  coolestDay=a[i][1]
print("coolest day is  ",coolestDay," with a temperature of ",lowestTemp)

