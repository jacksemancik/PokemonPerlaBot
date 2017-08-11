import pyautogui, time
from color import color_from_mouse

def keypress(key):
	pyautogui.keyDown(key)
	time.sleep(.5)
	pyautogui.keyUp(key)

def save():
	keypress('enter')
	keypress('up')
	keypress('up')
	keypress('up')
	keypress('x')
	keypress('x')
	keypress('x')
	keypress('x')#spams x to assure that the saving process screens have ended
	keypress('x')
	keypress('x')
	keypress('x')
	keypress('x')
	keypress('x')
	keypress('x')
	keypress('x')
	keypress('x')
	keypress('x')
	keypress('x')
	keypress('x')
	keypress('x')
	keypress('enter')#resets menu cursor
	keypress('down')#resets menu cursor
	keypress('down')#resets menu cursor
	keypress('down')#resets menu cursor
	keypress('enter')
	print('Game saved!')
	return

def perla(maxmin, wait, swi, ver, gen):
	pyautogui.FAILSAFE = True
	if wait:
		wait_time = wait * 60
		time.sleep(wait_time)
	if (swi == True):
		switchpos()
	save()
	red = 1
	endtime = time.time() + 60 * maxmin
	pyautogui.PAUSE = .5
	standard_color = game_color(ver,gen)
#Perla male standard color: (206, 170, 99)
	move_changes = 0
	while time.time() < endtime:
		while color_from_mouse() == standard_color:
			keypress('right')
			keypress('left')
			print('Performed task %s times!' % red)
			red += 1
		limit = time.time() + 180
		while not color_from_mouse() == standard_color:
			if time.time() < limit:
				keypress('x')
				keypress('x')
				print('Performed task %s times!' % red)
				red += 1
			else:
				move_changes = exit_battle(move_changes)
				print('Performed task %s times!' % red)
				red += 1



	limit = time.time() + 180
	move_changes = 5				
	while not color_from_mouse() == standard_color:
		keypress('x')
		if time.time() > limit:
			move_changes = exit_battle(move_changes)
	save()
	return

def switchpos():
	#pyautogui.PAUSE = 1.5
	keypress('enter')
	keypress('down')
	keypress('x')
	time.sleep(2)
	keypress('x')
	time.sleep(1)
	keypress('down')
	time.sleep(2)
	keypress('x')
	keypress('right')
	keypress('right')
	keypress('x')
	time.sleep(2)
	keypress('z')
	time.sleep(2)
	keypress('up')
	keypress('enter')
	print('Positions switched!')
	return

def exit_battle(move_changes):
	keypress('z')
	keypress('z')
	keypress('z')
	keypress('z')
	keypress('down')
	keypress('right')
	keypress('x')
	keypress('x')
	keypress('x')
	keypress('x')
	keypress('x')
	return switch_move(move_changes)

def switch_move(move_changes):
	move_changes += 1
	diff = 3 - move_changes
	if move_changes > 3:
		pass
	else:
		keypress('enter')
		keypress('down')
		keypress('x')
		time.sleep(2)
		keypress('x')
		time.sleep(1)
		keypress('x')
		time.sleep(2.5)
		keypress('right')
		time.sleep(1)
		keypress('right')
		time.sleep(2)
		keypress('x')
		time.sleep(1)
		keypress('x')
		keypress('down')
		time.sleep(1)
		keypress('x')
		time.sleep(1)
		keypress('x')
		for x in range(0,diff):
			keypress('down')
			time.sleep(1)
		keypress('x')
		keypress('z')
		keypress('z')
		time.sleep(1)
		keypress('z')
		keypress('z')
		time.sleep(2)
		keypress('up')
		keypress('enter')
	return move_changes

def game_color(v,g):
	if v == 'Chaos' or v == 'Fire' or v == 'Leaf':
		if g == 'Female':
			return (239, 235, 255)
		else:
			return (255, 105, 74)
	elif v == 'Emerald':
		if g == 'Female':#Must place mouse cursor over hair not over hat!!
			return (165, 105, 82)
		else:#Must place cursor over hair not headband!!
			return (252, 248, 253)
	elif v == 'Sapphire' or v == 'Ruby':
		if g == 'Female':
			return (165, 105, 82)#Placeholder, may not be accurate
		else:
			return (252, 248, 253)#Placeholder, may not be accurate
	elif v == 'Perla':
		return (206, 170, 99)#Same color for both characters, oddly enough
	
		
			
		
	
