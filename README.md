***Commands may need to be called in specific directories and with elevated privelages***

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

Previous folder:\
`cd ..`

Copy file:\
`cp <filename-source> <filename-destination>`

### Locations ###
Local display server:\
`/etc/gdm3/daemon.conf`

Apache2 error log:\
`/var/log/apache2/error.log`

### Troubleshooting

Issue: Wi-Fi disabled, airplane/bluetooth are enabled inverse of each other.

If this returns "0":\
`sysctl net.ipv4.ip_forward`

Run:\
`sysctl -w net.ipv4.ip_forward=1`

### Git

Initalize current directory as local repository:\
`git init`

Establish username:\
`git config user.name "someone"`

Establish email:\
`git config user.email "someone@someplace.com"`

Add all files to local repository:\
`git add *`

Commit:\
`git commit -m "<commit-text>"`

Purge local origin:\
`git remote prune origin`

Remove upstream:\
`git branch --unset-upstream`

Remove file:\
`git rm <filename>`

Remove directory:\
`git rm -rf <foldername>`

# Packages
### rm ###
Remove file:\
`rm <filename>`

Remove empty directories:\
`rm -d <filename>`

Remove directories:\
`rm -rf <foldername>`

### mv ###
Move files:\
`mv <filename-source> <filename-destination>`

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

Enable module:\
`a2enmod <modulename>`

### django ###

Creating new django project:\
`django-admin startproject <projectname>`

# Notes

Most modern computers have at least two modes: privileged mode and user mode. In privileged mode, a program can see the actual addresses of all the memory in the system (unless there's a hypervisor, but that's another topic). In user mode, a program uses different addresses to refer to memory. The OS tells the MMU how to translate the addresses, so then the MMU can translate every memory address that the user program works with into actual memory addresses.
