import time

x = 0
y = 1
z = 0


while True:
    
    x = y
    y = z
    z = x + y
    
    
    print(z)
    
    
    time.sleep(1)
    
