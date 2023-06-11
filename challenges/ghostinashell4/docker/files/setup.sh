#!/usr/bin/env bash
set -e

# set password
echo "blinky:blinkblink" | chpasswd

# disable history
echo 'set +o history' >> /home/blinky/.bashrc

# disable password change
passwd -n 9999 blinky

# make home dir readonly
chown -R root:root /home/blinky
chmod -R 755 /home/blinky

# make some dirs readonly and disable messaging.
chmod -R 755 /tmp
chmod -R 755 /var/tmp
chmod -R 700 /dev/shm
chmod -R 700 /dev/mqueue

# remove the file
rm -f /etc/entrypoint.d/setup.sh

# remove su
rm -f /bin/su
