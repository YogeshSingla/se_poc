## Steps to configure BLE on new Raspberry Pi

#### Enable BLE
add `--experimental` flag to bluetooth.service
```
sudo geany /lib/systemd/system/bluetooth.service
```
Inside *bluetooth.service* make following changes:
```
#ExecStart=/usr/lib/bluetooth/bluetoothd
ExecStart=/usr/lib/bluetooth/bluetoothd --experimental
```

Reload the service again:
```
sudo systemctl daemon-reload
sudo systemctl restart bluetooth
```
You can check the status using `sudo systemctl status bluetooth` and verify that the flag is set.

#### Install Python BLE library
For some reason, `http://archive.raspberrypi.org/debian/` source is down. Hence, you might have to change the source.
```
cd /etc/apt/sources.list.d/
sudo geany raspi.list
```

Add a mirror to the sources. For example:  

`file:raspi.list`
```
#added mirror for pybluez library installation - libbluetooth-dev
deb http://raspbian.mirror.net.in/raspbian/raspbian/ stretch main ui
#default
#deb http://archive.raspberrypi.org/debian/ stretch main ui
```

Install bluetooth header files:
```
sudo apt-get install libbluetooth-dev
```
If the library installation fails you might have to downgrade libbluetooth3 to *5.43-2+deb9u1* from *5.43-2+rpt2+deb9u1*.
```
sudo apt install libbluetooth3=5.43-2+deb9u1
```

Install pybluez
```
sudo pip install pybluez
```

Source:
* [Learning material](https://people.csail.mit.edu/albert/bluez-intro/c212.html)
* [Commands](https://gist.github.com/lexruee/fa2e55aab4380cf266fb)
