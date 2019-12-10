import linecache
import time
read = open ("dump.txt", 'r')
x = len(read.readlines())
read.close()
dump = open("log.txt" ,'a')
print(x)
time.sleep(10)
read = open ("dump.txt", 'r')
y = len(read.readlines())
read.close()
print(y)
while x != y:
    dump.write(linecache.getline('dump.txt',x))
    x = 1+x
dump.close()

	



	


	
