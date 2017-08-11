import argparse
from views import perla
from sanitise import Sanitise

parser = argparse.ArgumentParser(prog="perla")
parser.add_argument("run_time", metavar="N", type=float, nargs=1, help="amount of time (in minutes) that perla runs for")
parser.add_argument("-w","--wait",type=float, default=1, nargs=1,help="amount of time (in minutes) that perla waits before running")
parser.add_argument("-s","--switch",action="store_true",default=False,help="switch the first and second Pokemon in your party")
parser.add_argument("-g","--game",type=str,default='Perla',nargs=1,help="game version for which you want to use PerlaBot (either Sapphire, Ruby, Emerald, Perla, FireRed, LeafGreen, or ChaosBlack)")
parser.add_argument("-x","--sex",type=str,nargs=1,required=True,help="gender of the in-game character (either Male or Female)")
#parser.add_argument("-g","--game",)
args = vars(parser.parse_args())
gender = Sanitise.gender(args['sex'])
game = Sanitise.game(args['game'])
number_of_minutes = 0
for each in args['run_time']:
	number_of_minutes += float(each)
wait_minutes = 0
for each in args['wait']:
	wait_minutes += float(each)
switch = args['switch']
perla(number_of_minutes, wait_minutes, switch, game, gender)



