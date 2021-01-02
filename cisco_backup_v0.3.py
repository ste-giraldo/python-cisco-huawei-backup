import sys
import time
import paramiko 
import getpass
import os
import cmd
import datetime

#set date and time
now = datetime.datetime.now()

#Comment or uncommend lines in static or prompted authentication to use preferred auth mode
#Static authentication
#USER = ''
#PASSWD = ''
#SECRET = ''
#End Static authentication

#Prompted authentication
USER = raw_input("Username: ")
PASSWD = getpass.getpass("Password: ")
print ('If your device does not use an enable password, just press Enter')
SECRET = getpass.getpass("Enable Password: ")
#End Prompted authentication

#start FOR ...in 
f = open('cisco_hosts')
for ip in f.readlines():
	ip = ip.strip()
	#prefix files for backup
	filename_prefix ='config_backup-' + ip

	#session start
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, username=USER, password=PASSWD)

	#ssh shell
	chan = client.invoke_shell()
	time.sleep(0.5)
	#enter enable secret
	chan.send('enable\n')
	time.sleep(0.5)
	chan.send(SECRET +'\n')
	#terminal lenght for no paging 
	chan.send('term len 0\n')
	time.sleep(0.5)
	#show running-config and write output in a file
	chan.send('show run\n')
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
