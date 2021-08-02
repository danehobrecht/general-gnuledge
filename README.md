## Wirelessly transfer files from GNU/Linux to iPhone without third-party iOS applications.
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
```
Restart the samba service:\
`systemctl restart smbd`

Fetch the local host I.P. with `nmblookup WORKGROUP`. The output should look like this:
```
<localhost> WORKGROUP<00>
```

Install the first-party "Files" app from the iOS App Store:\
https://apps.apple.com/us/app/files/id1232058109

Connect to the `<localhost>` in the iPhone files app:\
Files > "..." > Connect to Server

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

# Notes
"Most modern computers have at least two modes: privileged mode and user mode. In privileged mode, a program can see the actual addresses of all the memory in the system (unless there's a hypervisor, but that's another topic). In user mode, a program uses different addresses to refer to memory. The OS tells the MMU how to translate the addresses, so then the MMU can translate every memory address that the user program works with into actual memory addresses." - Unknown
