import sys
from views import perla

number_of_minutes = float(sys.argv[1])

#old code: wait_minutes = float(sys.argv[2])
try:
	wait_minutes = float(sys.argv[2])
except:
	try:
		switch = str(sys.argv[2])
	except:
		switch = False
	else:
		if switch == "True" or switch == "true" or switch == "Switch" or switch == "switch":
			switch = True
		else:
			switch = False

	wait_minutes = 1
else:
	try:
		switch = str(sys.argv[3])
	except:
		switch = False
	else:
		if switch == "True" or switch == "true" or switch == "switch" or switch == "Switch":
			switch = True
		else:
			switch = False



perla(number_of_minutes, wait_minutes, switch)
