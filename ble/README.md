## Bluetooth theory

#### Background
1. From the hardware module up, we have preinstalled libraries that interface with it. **Bluez** is the official Bluetooth protocol stack for GNU/Linux. **Pybluez** is built on top of it as an extension library to use bluez inside python. [**BLESuite**](https://github.com/nccgroup/BLESuite) is built using pybluez and pygattlib(BLE support library with pybluez) to make bluetooth programming in python even easier.
2. Alternative to bluez is **Affix**, which is another bluetooth protocol stack having pyaffix extension library.  
*We will stick to bluez and pybluez in following document.*

#### Discovery
1. In Bluetooth, where there are no nameservers, a client will broadcast inquiries to see what other devices are nearby.
2. Query each detected device for its user-friendly name.
3. The client then chooses whichever device has a name that matches the one supplied by the user.  
[source](https://people.csail.mit.edu/albert/bluez-intro/x79.html)

#### Connection
1. Decide upon transport protocol. RFCOMM (Radio Frequency Communication) works like TCP in Internet programming. L2CAP (Logicial Link Control and Adaptation Protocol) in Bluetooth programming is similar to UDP in Internet programming.
2. Choose the port in a predefined manner (similar to how internal ports are used. For e.g 443 for HTTPS etc). Or else, use Service Discovery Protocol (SDP) to search for available services (ports) through Universally Unique Identifier (UUID) during runtime and connect to them. Second, option is relatively complex but scalable and recommended.

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

#### Install pybluez
###### (python Bluetooth library)
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

***
###### Sources:
* [Learning material](https://people.csail.mit.edu/albert/bluez-intro/c212.html)
* [Commands](https://gist.github.com/lexruee/fa2e55aab4380cf266fb)
* [pybluez-Google Code  (obsolete)](https://code.google.com/archive/p/pybluez/)
* [pybluez-Github (active)](https://github.com/karulis/pybluez)
