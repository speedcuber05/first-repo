import inputimeout 
try:
	time_over = inputimeout.inputimeout(prompt='Name your best friend:', timeout=3) 
except Exception: 
	time_over = 'Your time is over!'
	print(time_over)  
else:
	print('nice')
