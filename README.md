## Wirelessly transfer files from GNU/Linux to iOS without third-party iOS applications
Install dependencies:\
`apt install samba samba-client cifs-utils`

Add a samba user with  `smbpasswd -a <user>` and verify said user is active with `pdbedit -w -L`.

Append the following information to the samba configuration file located at `/etc/samba/smb.conf`:
```
[Public]
   path = /path/you'd/like/to/make/public
   browseable = yes
   read only = no
   guest ok = yes
   writeable = yes
```
Restart the samba service:\
`systemctl restart smbd`

Fetch the local host I.P. with `nmblookup WORKGROUP`. The output should look like this:
```
<localhost> WORKGROUP<00>
```
If you haven't already, install the first-party "Files" app from the iOS App Store:\
https://apps.apple.com/us/app/files/id1232058109

Connect to the server in the iPhone files app with the `smb://<localhost>` format:\
>Files > "..." > Connect to Server

Access files as needed.

## Establishing a Wi-Fi connection with no dependencies

**...assuming "wpa_supplicant" and "iw" is are available, which should be the case.**

Run:\
`sysctl -w net.ipv4.ip_forward=1`

Verify a wireless driver (i.e. `wlp4s0`) is available with `ls /sys/class/net`. A common output looks like:
```
enp6s0f0 lo wlp4s0
```
Create a temporary configuration file with `nano /etc/wpa_supplicant.conf` and append the following lines:
```
network={
	ssid="<ssid>"
	psk="<password>"
}
```
Connect to the previously specified `<ssid>` by running the following commands in order:\
`ip link set wlp4s0 down`\
`ip link set wlp4s0 up`\
`wpa_supplicant -B -i wlp4s0 -c /etc/wpa_supplicant.conf -D nl80211,wext`\
`dhclient wlp4s0`

Verify that a connection has been established. There are several ways of doing this, put a simple ping will be sufficient:\
`ping www.searx.be`

You may now purge the temporary configuration file with `rm /etc/wpa_supplicant.conf`.

Access internet as needed.

## Adding executables to Debian PATH
Edit `.bashrc` file:\
`sudo nano /etc/bash.bashrc`

Append text to the end of the file:\
`PATH=${PATH}:/<path>/<to>/<directory>`\
OR\
`export PATH=/<path>/<to>/<directory>/bin:$PATH`

Re-load `.bashrc` file:\
`source /etc/bash.bashrc`

Attempt to execute a binary. For elevated privelages with said binaries, enter super user mode (`su`):\
`fastboot`

## Accept an Android tether
Set up USB:\
`ip link set usb0 up`

Enable USB network utilization:\
`dhclient usb0`

## Manage Android applications with ADB
Uninstall:\
`pm uninstall -k --user 0 <package>`

Re-install:\
`pm install-existing <package>`

# General notes
"Most modern computers have at least two modes: privileged mode and user mode. In privileged mode, a program can see the actual addresses of all the memory in the system (unless there's a hypervisor, but that's another topic). In user mode, a program uses different addresses to refer to memory. The OS tells the MMU how to translate the addresses, so then the MMU can translate every memory address that the user program works with into actual memory addresses." - Unknown
