import sys
import time
import random
import csv
import datetime

from csv import unix_dialect
sys.stdout.write(
    'Insert the number of process you want to generate logs for : ')
numberOfProcess = int(input())
sys.stdout.write('Creating logs for '+str(numberOfProcess)+' process ...')
headers = ['timestamp', 'LOG ENTRY ID', 'ID CORRELATION',
           'Station ID', 'Process Step ID', 'Activity Status', 'Message','FileName']
states = ['OK', 'WARNING', 'ERREUR']
steps = 5
dataList = []
countLogs = 1
for process in range(numberOfProcess):
    lastMessage = ''
    dateRow = datetime.datetime.today()
    for step in range(steps):
        message = ''
        if lastMessage != 'ERREUR' :
            activityStatus = states[random.randint(0, len(states)-1)]
            if activityStatus == 'WARNING':
                message = 'Warning message'
            elif activityStatus == 'ERREUR':
                message = 'Error message'
            else:
                message = ''
            date = dateRow + datetime.timedelta(step)
            dataList.append([date,countLogs,process+1,'?',step+1,activityStatus,message,'File_process_'+str(process+1)+'_step_'+str(step+1)])
            lastMessage = activityStatus
            countLogs += 1

path = './files/logs.csv'

with open(path, 'w', newline='') as f:
    writer = csv.writer(f,dialect=unix_dialect)
    csvHeaders = []
    for header in headers :
        csvHeaders.append(header)
    writer.writerows([csvHeaders])
    writer.writerows(dataList)
