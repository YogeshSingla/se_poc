Find file on a linux machine:
```
find /home -name "*.c"
```

Run pulseaudio daemon:
```
pulseaudio -D
```

### Configuring WiFi in VM
Host: Windows 10
VM : Ubuntu 18.04
1. Open virtual machine Settings-> Network, then choose adapter1 to NAT.
2. Now open Network and Sharing-Center in Windows, then go to change Adapter settings, then disable the virtual box host only adapter.
3. close the window and now you should be able to use internet in ubuntu.

Source: [askubuntu]( https://askubuntu.com/questions/379438/how-do-i-connect-to-the-wifi-in-ubuntu-within-my-virtual-machine?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)
