from weather import Weather()
loc=input("enter the location ")
location = weather.lookup_by_location(loc)
condition = location.condition()

# Get weather forecasts for the upcoming days.
for forecasts in location.forecast():
    print (forecasts['text'])
    print (forecasts['date'])
    print (forecasts['high'])
    print (forecasts['low'])

