### Transfer files from Linux to iPhone
 
Install dependencies: `apt install samba samba-client cifs-utils`

Add a samba user:\
`smbpasswd -a <user>`

Verify the user is active:\
`pdbedit -w -L`

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

Verify the samba service is serving local connections with `nmblookup WORKGROUP`. The output should look like this:

```
<localhost> WORKGROUP<00>
```

Connect to the local host I.P. address in the iPhone files app.

Files > "..." > Connect to Server

### Accessing Wi-Fi with no dependencies

Issue: Wi-Fi disabled, airplane/bluetooth are enabled inverse of each other.

If this returns "0":\
`sysctl net.ipv4.ip_forward`

Run:\
`sysctl -w net.ipv4.ip_forward=1`

ls /sys/class/net
 
    enp6s0f0 lo wlp4s0

Assuming wpa_supplicant and iw is installed.

To connect to wifi through wpa_supplicant you need to create a wpa_supplicant.conf file

`nano /etc/wpa_supplicant.conf`

with the following lines:

    network={
             ssid="<ssid>"
             psk="<password>"
    }

Or you can use wpa_passphrase to create the configuration file (copy and past):

wpa_passphrase "<ssid>" "<password>" 

Also you can write the wpa_supplicant.conf directly through:

wpa_passphrase "<ssid>" "<password>" > /etc/wpa_supplicant.conf

to connect type the following command:

`ip link set wlp4s0 down`\
`ip link set wlp4s0 up`\
`wpa_supplicant -B -iwlp4s0 -c /etc/wpa_supplicant.conf -Dnl80211,wext`\
`dhclient wlp4s0`

Note: Multiple comma separated driver wrappers in option -Dnl80211,wext makes wpa_supplicant use the first driver wrapper that is able to initialize the interface (see wpa_supplicant(8)). This is useful when using mutiple or removable (e.g. USB) wireless devices which use different drivers.

You can connect through wpa_supplicant without wpa_supplicant.conf file:

wpa_supplicant -B -i wlp4s0 -c wpa_passphrase "<ssid>" "<password>" && dhclient wlp4s0

# Notes

Most modern computers have at least two modes: privileged mode and user mode. In privileged mode, a program can see the actual addresses of all the memory in the system (unless there's a hypervisor, but that's another topic). In user mode, a program uses different addresses to refer to memory. The OS tells the MMU how to translate the addresses, so then the MMU can translate every memory address that the user program works with into actual memory addresses.
