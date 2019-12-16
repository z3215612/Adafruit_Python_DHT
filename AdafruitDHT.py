#!/usr/bin/python3
humidity,temperture=Adafruit DHT.read retry(sensor,pin)
if humidity is not None and temperature is not None:
	print('Temp={0:0.1f}*Humidity={1:0.1f}%'.format(temperture,humidity))
else:
	print('Failed to get reading.Try again!')
	sys.exit(1)
