#!/bin/bash
cd /home/adaas/.ssh
ssh-keygen -t rsa
iplist=`cat /apps/adf/tmp/ip.list`
user=$1
passwd=$2
for ip in $iplist
do
/usr/bin/expect <<-EOF
spawn ssh-copy-id -i /home/adaas/.ssh/id_rsa.pub $user@$ip
expect "*yes";
send "yes\r";
expect "password";
send "$passwd\r";
interact;
expect eof
EOF
done