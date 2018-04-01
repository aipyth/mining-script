import os
import time
import threading
import win32gui, win32con

hide_stuff = win32gui.GetForegroundWindow()                                     # Hides window
win32gui.ShowWindow(hide_stuff , win32con.SW_HIDE)

class Countdown(threading.Thread):                                              # Thread for countdown
    def __init__(self, interval, start_time):
        threading.Thread.__init__(self)
        self.daemon = True
        self.interval = interval
        self.start_time = start_time
    def run(self):
        while True:
            if (time.time() - self.start_time) > self.interval:                 # Check what time has passed
                print('\n!!! SHUTDOWN !!!\n')
                os.system('shutdown -s -t 10')                                  # Shut everything down
                break
        return

with open('config.txt') as conf:
    conf = conf.read().split()

start_time = time.time()                                                        # Time when script was activated
cpu_cores = conf[1]                                                             # Number of cores active
gpu_intens = conf[2]                                                            # GPU instensivity
interval = int(conf[4])                                                         # Interval is a number in what time the pc would be shutten down. Must be 54000
CD = Countdown(interval, start_time)
CD.start()                                                                      # Start thread

print('(#) CPU cores active: ', cpu_cores)
print('(#) GPU instensivity: ', gpu_intens)
print('(#) Interval: ', interval)
print('(#) Countdown started! {} sec left'.format(interval))
print('(#) Running mining script!\n')

os.system('minergate-cli -user ipython10@gmail.com -fcn+xmr {} {}'.format(cpu_cores, gpu_intens))  # Start miner
