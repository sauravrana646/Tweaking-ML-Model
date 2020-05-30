import os

with open('/root/task3/accuracy.txt', 'r') as f:
    acc = f.read()


if float(acc) > 95 :
    os.system('curl --user admin:redhat http://192.168.43.200:8080/view/Task3/job/Build%20Status/build?token=success')
else :
    os.system('curl --user admin:redhat http://192.168.43.200:8080/view/Task3/job/Tweaking/build?token=failed')
