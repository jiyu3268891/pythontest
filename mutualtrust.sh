#!/bin/bash
#mutual trust
mkdir -p /home/`whoami`/.ssh
cd /home/`whoami`/.ssh
if [ ! -f id_rsa.pub ]
then
ssh-keygen -t rsa
fi
#mutual trust ip list
iplist=`cat /apps/adf/install/ip.list`
while read -r line
do
	ip=`echo $line | awk '{print $1}'`
	user=`echo $line | awk '{print $2}'`
	passwd=`echo $line | awk '{print $3}'`
	/usr/bin/expect <<-EOF
	spawn ssh-copy-id -i /home/$user/.ssh/id_rsa.pub $user@$ip
	expect "*yes";
	send "yes\r";
	expect "password";
	send "$passwd\r";
	interact;
	expect eof
	EOF
done < /apps/adf/install/ip.list
