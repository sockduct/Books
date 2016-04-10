# Imports
#import thread
from threading import Thread
import time
import os

def calltcli(arg0,arg1='',arg2=''):
    print 'Entered calltcli at ' + str(time.ctime(time.time())) + '\n'
    syscallstr = str(arg0) + ' ' + str(arg1) + ' ' + str(arg2)
    # Debugging
    #print 'System call:  ' + syscallstr
    os.system(syscallstr)

for i in range(200):
    Thread(target=calltcli,args=('tcp_sixteen','client')).start()
# Using thread module - supposedly harder
#thread.start_new_thread(calltcli,('tcp_sixteen','client'))
# Using Thread from threading module, supposedly easier
#Thread(target=calltcli,args=('tcp_sixteen','client')).start()

# Testing
#calltcli('tcp_sixteen','client','')
#calltcli('tcp_sixteen','client')

