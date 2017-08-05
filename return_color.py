import pyscreeze, pyautogui

def color_from_mouse():
	mouse_x, mouse_y = pyautogui.position()
	color = pyscreeze.pixel(mouse_x,mouse_y)
	return color
