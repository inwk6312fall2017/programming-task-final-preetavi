from weather import Weather
weather = Weather()
loc=input("enter the location ")
location = weather.lookup_by_location(loc)
condition = location.condition()
a=[]
# Get weather forecasts for the upcoming days.
for forecasts in location.forecast():
  b=[]    
  b.append(forecasts['text'])
  b.append(forecasts['date'])
  b.append(forecasts['high'])
  b.append(forecasts['low'])
  a.append(b)
print(a)
