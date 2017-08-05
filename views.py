import pyautogui, sys, time
from return_color import color_from_mouse

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

def perla(maxmin, wait, swi):
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
	while time.time() < endtime:
		standard_color = (206, 170, 99)
		if (color_from_mouse() == standard_color):
			keypress('right')
			keypress('left')
		else:
			keypress('x')
			keypress('x')
		print('Performed task %s times!' % red)
		red += 1
	while not color_from_mouse() == standard_color:
		keypress('x')
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
	

		
	
