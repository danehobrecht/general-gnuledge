Read documentation. Do not be a help vampire. Yes, you can do it.

### General terminal ###
Add sudo user:\
`usermod -aG adduser sudo <username>`

Clear terminal history:\
`history -c`

Kill all processes:\
`kill -9 -1`

Running a file:\
`./<filename>`

# Locations
Local display server:\
`/etc/gdm3/daemon.conf`

# Commands
### rm ###
Remove file:\
`rm filename`

Remove empty directories:\
`rm -d <filename>`

Remove directories:\
`rm -rf <filename>`

### mv ###
Move files:\
`mv <source> <destination>`

### crypsetup ###
Encrypt drive:\
`cryptsetup --verbose --verify-passphrase luksFormat /dev/<partiton>`

### dpkg ###
`dpkg -i *.deb`

### apache2 ###
Start apache2 web server:\
`systemctl start apache2`

### django ###
Installing django:\
`pip3 install django`

Creating new django project in a directory:\
`django-admin startproject <projectname>`
