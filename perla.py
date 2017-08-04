import sys
from views import perla

number_of_minutes = float(sys.argv[1])

#old code: wait_minutes = float(sys.argv[2])
try:
	wait_minutes = float(sys.argv[2])
except:
	try:
		switch = bool(sys.argv[2])
	except:
		switch = False

	wait_minutes = 1
else:
	try:
		switch = bool(sys.argv[3])
	except:
		switch = False



perla(number_of_minutes, wait_minutes, switch)



