#!/bin/bash
echo "how do you install packages? example= pacman -S"
read pkgmanager
$pkgmanager doas 

echo "what is your user name?"
read name
echo permit nopass $name as root > /etc/doas.conf
ln -s /bin/doas /bin/sudo

