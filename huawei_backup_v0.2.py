import sys
import time
import paramiko 
import os
import cmd
import datetime

#set date and time
now = datetime.datetime.now()

#authentication
USER = ''
PASSWORD = ''

#start FOR ...in 
f = open('huawei_hosts')
for ip in f.readlines():
	ip = ip.strip()
	#prefix files for backup
	filename_prefix ='config_backup-' + ip
	
	#session start
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, username=USER, password=PASSWORD)

	#ssh shell
	chan = client.invoke_shell()
	time.sleep(0.5)
	#terminal lenght for no paging 
	chan.send('screen-length 0 temp\n')
	time.sleep(0.5)
	#check software version
	chan.send('dis ver\n')
	time.sleep(0.5)
	#show running-config and write output in a file
	chan.send('dis cur\n')
	time.sleep(3)
	output = chan.recv(99999999)
	#show output config and write file with prefix, date and time
	print output
	#choose file format by commenting or decommenting lines below
#	filename = "%s_%.2i-%.2i-%i_%.2i-%.2i-%.2i" % (filename_prefix,now.day,now.month,now.year,now.hour,now.minute,now.second)
	filename = "%s_%.2i-%.2i-%i" % (filename_prefix,now.year,now.month,now.day)
	ff = open(filename, 'a')
	ff.write(output)
	ff.close()
	#close ssh session
	client.close() 
	
	print ip
	f.close()

