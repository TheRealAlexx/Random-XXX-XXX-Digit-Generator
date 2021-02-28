import random, time

#LOOP THAT MAKES RANDOM XXX - XXX DIGITS EVERY 20 SECS
while True:
    random1 = str(random.randint(100, 999))
    random2 = str(random.randint(100, 999))
    print ( random1 + " - " + random2 )
    time.sleep(20) #Period of Seconds Between Digit Change

