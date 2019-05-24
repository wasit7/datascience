#! /bin/bash

for i in {1..10}; do
  u="user$i"
  useradd -m $u
  echo "$u:$u" | chpasswd
  chown -R $u:$u /home/$u
done;

chmod -R 777 /data