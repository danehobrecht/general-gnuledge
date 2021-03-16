***Commands may need to be called in specific directorys and with elevated privelages

# General terminal
### Commands ###
Add sudo user:\
`usermod -aG adduser sudo <username>`

Clear terminal history:\
`history -c`

Kill all processes:\
`kill -9 -1`

Running a file:\
`./<filename>`

### Locations ###
Local display server:\
`/etc/gdm3/daemon.conf`

Apache2 error log:\
`/var/log/apache2/error.log`

# Packages
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

### flask ###

Establish flask script:\
`export FLASK_APP=<filename>.py`

Run flash script:\
`flask run`

### apache2 ###
Start apache2 web server:\
`systemctl start apache2`

Enable cgi:\
`a2enmod cgid`

### django ###
Installing django:\
`pip3 install django`

Creating new django project:\
`django-admin startproject <projectname>`
