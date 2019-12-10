import os
import random
import time


while True:
	x = random.randrange(0, 100, 2)
	with open("dump.txt", "a+") as dump:
		dump.write(str(x)+'\n')
		time.sleep(1)
		dump.close()