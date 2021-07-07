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

ls /sys/class/net
example output: 
enp6s0f0 the wlp4s0

Assuming wpa_supplicant and iw is installed.

    To connect to wifi through wpa_supplicant you need to create a wpa_supplicant.conf file

    nano /etc/wpa_supplicant.conf

    with the following lines:

    network={
             ssid="wifi_name"
             psk="wifi_key"
    }

Or you can use wpa_passphrase to create the configuration file (copy and past):

wpa_passphrase "Your_SSID" Your_passwd 

Also you can write the wpa_supplicant.conf directly through:

wpa_passphrase "Your_SSID" Your_passwd > /etc/wpa_supplicant.conf

to connect type the following command:

`sudo ip link set wlp4s0 down`\
`sudo ip link set wlp4s0 up`\
`sudo wpa_supplicant -B -iwlp4s0 -c /etc/wpa_supplicant.conf -Dnl80211,wext`\
`sudo dhclient wlp4s0`\

    Note: Multiple comma separated driver wrappers in option -Dnl80211,wext makes wpa_supplicant use the first driver wrapper that is able to initialize the interface (see wpa_supplicant(8)). This is useful when using mutiple or removable (e.g. USB) wireless devices which use different drivers.

You can connect through wpa_supplicant without wpa_supplicant.conf file:

wpa_supplicant -B -i wlp4s0 -c <(wpa_passphrase "Your_SSID" Your_passphrase) && dhclient wlp4s0

### Git

Initalize current directory as local repository:\
`git init`

Establish username:\
`git config user.name "someone"`

Establish email:\
`git config user.email "someone@someplace.com"`

Add all files to local repository:\
`git add .git clone https://github.com/eromoe/test2`

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

Commit all tracked files:\
`git commit --amend`

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
