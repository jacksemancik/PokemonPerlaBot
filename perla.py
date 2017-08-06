import argparse
from views import perla

parser = argparse.ArgumentParser(prog="perla")
parser.add_argument("run_time", metavar="N", type=float, nargs=1, help="The amount of time (in minutes) that perla runs for")
parser.add_argument("-w","--wait",type=float, default=1, nargs=1,help="The amount of time (in minutes) that perla waits before running")
parser.add_argument("-s","--switch",action="store_true",default=False,help="Switches the first and second Pokemon in your party")
#parser.add_argument("-g","--game",)
args = vars(parser.parse_args())
number_of_minutes = 0
for each in args['run_time']:
	number_of_minutes += float(each)
wait_minutes = 0
for each in args['wait']:
	wait_minutes += float(each)
switch = args['switch']
perla(number_of_minutes, wait_minutes, switch)



