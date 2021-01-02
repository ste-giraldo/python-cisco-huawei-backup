# Original script written by Mike Ivanov - https://github.com/mikonoid/python-cisco-backup
# Fork by Stefano Giraldo - https://github.com/ste-giraldo

# python-cisco-backup
script for backup cisco configs
Tested on python 2.7 with paramiko lib

#cisco_backup_v0.1.py
version for simple backup for one device

#cisco_backup_v0.2.py 
version for multiple backup from list of host from file hosts

#cisco_backup_v0.3.py 
version with hosts list from external file "cisco_backup_hosts". It also use static (in script) or prompted authentication.

#huawei_backup_v0.3py
version with hosts list from external file "huawei_backup_hosts". It also use static (in script) or prompted authentication.
To avoid error "CryptographyDeprecationWarning" during SSH against Huawei devices use python-paramiko >= 2.5
For Debian users: python-paramiko_2.6.0-1~bpo10+1_all.deb works fine.
