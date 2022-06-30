#!/bin/bash
echo "how do you install packages? example= pacman -S"
echo "Sometimes doas is called opendoas, make sure to do pacman -S opendoas then"
read pkgmanager
$pkgmanager doas 

echo "what is your user name?"
read name
echo permit nopass $name as root > /etc/doas.conf
ln -s /bin/doas /bin/sudo

