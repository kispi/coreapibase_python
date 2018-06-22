import threading, time

def wrapper(interval, foo):
    while True:
        foo()
        time.sleep(interval)        

def cron(interval, foo):
    t = threading.Thread(target=wrapper, args=(interval, foo))
    t.start()