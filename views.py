import pyautogui, sys, time

def save():
	time.sleep(1)
	pyautogui.press('enter')
	time.sleep(3)
	pyautogui.press('up')
	time.sleep(3)
	pyautogui.press('up')
	time.sleep(3)
	pyautogui.press('up')
	time.sleep(3)
	pyautogui.press('x')
	time.sleep(5)
	pyautogui.press('x')
	time.sleep(5)
	pyautogui.press('x')
	time.sleep(5)
	pyautogui.press('x')#spams x to assure that the saving process screens have ended
	time.sleep(3)
	pyautogui.press('x')
	time.sleep(3)
	pyautogui.press('x')
	time.sleep(3)
	pyautogui.press('x')
	time.sleep(3)
	pyautogui.press('x')
	time.sleep(3)
	pyautogui.press('x')
	time.sleep(3)
	pyautogui.press('x')
	time.sleep(3)
	pyautogui.press('x')
	time.sleep(3)
	pyautogui.press('x')
	time.sleep(3)
	pyautogui.press('x')
	time.sleep(3)
	pyautogui.press('x')
	time.sleep(3)
	pyautogui.press('x')
	time.sleep(3)
	pyautogui.press('x')
	time.sleep(3)
	pyautogui.press('enter')#resets menu cursor
	time.sleep(3)
	pyautogui.press('down')#resets menu cursor
	time.sleep(3)
	pyautogui.press('down')#resets menu cursor
	time.sleep(3)
	pyautogui.press('down')#resets menu cursor
	print('Game saved!')
	print('(Unless, of course, you were in a battle. Oops!)')
	return

def perla(maxmin, wait, swi):
	if wait:
		wait_time = wait * 60
		time.sleep(wait_time)
	if (swi == 'switch'):
		switchpos()
	save()
	red = 1
	endtime = time.time() + 60 * maxmin
	while time.time() < endtime:
		pyautogui.press(['right','right','right','left','left','left','x'])
		print('Performed task %s times!' % red)
		red += 1
	save()
	return

def switchpos():
	pyautogui.press(['enter','down','x'])
	time.sleep(5)
	pyautogui.press(['x','down','x','left','x','z'])
	time.sleep(5)
	pyautogui.press(['up','enter'])
	print('Positions switched!')
	return
	

		
	
