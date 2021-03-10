Read documentation. Do not be a help vampire. Yes, you can do it.

# Commands
### rm ###
Remove file:\
`rm filename`

Remove empty directories:\
`rm -d <filename>`

Remove directories:\
`rm -rf <filename>`

Move files:\
`mv <source> <destination>`

Add sudo user:\
`usermod -aG adduser sudo <username>`

Encrypt drive:\
`sudo cryptsetup --verbose --verify-passphrase luksFormat /dev/<partiton>`

Clear terminal history:\
`history -c`

Kill all processes:\
`kill -9 -1`

Running a file:\
`./<filename>`

Installing all debian packages in a directory:\
`sudo dpkg -i *.deb`

Start apache2 web server:\
`sudo systemctl start apache2`

# Locations
Display server:\
`/etc/gdm3/daemon.conf`

# Python

Installing django:\
`pip3 install django`

Creating new django project in a directory:\
`django-admin startproject <projectname>`
