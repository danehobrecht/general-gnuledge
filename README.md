### Transfer files from Linux to iPhone
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
Connect to the server with said I.P. in the iPhone files app: Files > "..." > Connect to Server

Download files as needed.

### Accessing Wi-Fi with no dependencies

...assuming "wpa_supplicant" and "iw" is are pre-installed, which should be the case.

If `sysctl net.ipv4.ip_forward` returns "0", run `sysctl -w net.ipv4.ip_forward=1`.

Verify a wireless driver (i.e. `wlp4s0`) is available:\
`ls /sys/class/net`\
A common output looks like:
```
enp6s0f0 lo wlp4s0
```

Create a wpa_supplicant.conf file with `nano /etc/wpa_supplicant.conf` and append the following lines:
```
network={
	ssid="<ssid>"
	psk="<password>"
}
```
Connect to the previously specified S.S.I.D. by running the following commands in order:\
`ip link set wlp4s0 down`\
`ip link set wlp4s0 up`\
`wpa_supplicant -B -iwlp4s0 -c /etc/wpa_supplicant.conf -Dnl80211,wext`\
`dhclient wlp4s0`

Verify that a connection has been established.

# Notes
Most modern computers have at least two modes: privileged mode and user mode. In privileged mode, a program can see the actual addresses of all the memory in the system (unless there's a hypervisor, but that's another topic). In user mode, a program uses different addresses to refer to memory. The OS tells the MMU how to translate the addresses, so then the MMU can translate every memory address that the user program works with into actual memory addresses.
