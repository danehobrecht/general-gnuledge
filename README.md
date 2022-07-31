## Transfer files from Arch Linux to iOS
sudo pacman -S libimobiledevice # needed protocols to connect
yay -S ifuse # needed to mount
systemctl start usbmuxd.service # ensure service running
idevicepair pair # pair phone
mkdir /mnt/iphone # place to mount
sudo ifuse -o allow_other /mnt/iphone # mount phone
ls /mnt/iphone # go explore

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
`nano /etc/bash.bashrc`

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
Initialize ADB shell:\
`adb shell`

Uninstall:\
`pm uninstall -k --user 0 <package>`

Re-install:\
`pm install-existing <package>`

## View kernel information
Kernel release:\
`uname -r`

All available information:\
`uname -a`

## Remove lock icon from folders (change permissions)
Navigate to home folder:\
`cd`

Run `chmod`:\
`chmod -R a+rwx *`

## Adding a printer to cups from the command line
Add the printer's I.P. address via `lpadmin`:\
`lpadmin -p <printer_name> -E -v "ipp://<ip_address>/ipp/print" -m everywhere`

## Check RAM speed
Run `dmidecode`:\
`dmidecode --type 17`

## Grant user sudo privelages
Become super user:\
`su`

Open the `sudoers` file:\
`nano /etc/sudoers`

Append permission:\
`<username> ALL=(ALL) ALL`

## PDF Conversion
JPEG to PDF:\
`pdftoppm '<input.pdf>' '<output>' -jpeg -r 300`
PDF to JPEG:\
`pdftoppm -jpeg -r 300 <input.pdf> <output>`

## File encryption
Encrpt file with GPG:\
`gpg -c <filename>`

Decrypt file with GPG:\
`gpg -d <filename>`

# General notes
"Most modern computers have at least two modes: privileged mode and user mode. In privileged mode, a program can see the actual addresses of all the memory in the system (unless there's a hypervisor, but that's another topic). In user mode, a program uses different addresses to refer to memory. The OS tells the MMU how to translate the addresses, so then the MMU can translate every memory address that the user program works with into actual memory addresses." - Unknown
