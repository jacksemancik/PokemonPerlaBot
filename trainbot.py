import sys
from perlabot import perla

number_of_minutes = float(sys.argv[1])
try:
	wait_minutes = float(sys.argv[2])
except IndexError:
	wait_minutes = 1
	switch = None
except ValueError:
	wait_minutes = 1
	try:
		switch = str(sys.argv[2])
	except:
		switch = None
else:
	switch = str(sys.argv[3])


perla(number_of_minutes, wait_minutes, switch)



