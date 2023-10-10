
### Description:
Let's say you have generated several hundred files and you need to group them into separate unique archives and not spend more than one minute of time.

Let's say your files look like this:

```
vpn-peer-2.NY.conf
vpn-peer-2.NY.png
vpn-peer-2.LO.conf
vpn-peer-2.LO.png
vpn-peer-2.FR.conf
vpn-peer-2.FR.png
vpn-peer-3.NY.conf
vpn-peer-3.NY.png
vpn-peer-3.LO.conf
vpn-peer-3.LO.png
vpn-peer-3.FR.conf
vpn-peer-3.FR.png
.
.
.
vpn-peer-124.NY.conf
vpn-peer-124.NY.png
vpn-peer-124.LO.conf
vpn-peer-124.LO.png
vpn-peer-124.FR.conf
vpn-peer-124.FR.png
```

Enter the files name: [vpn-peer-]
Enter the first number: [2]
Enter the last number: [124]

The script will collect it into separate archives, in the end you will get:
```
vpn-peer-2.zip containing files: vpn-peer-2.NY.conf vpn-peer-2.NY.png vpn-peer-2.LO.conf vpn-peer-2.LO.png vpn-peer-2.FR.conf vpn-peer-2.FR.png
vpn-peer-3.zip containing files: vpn-peer-3.NY.conf vpn-peer-3.NY.png vpn-peer-3.LO.conf vpn-peer-3.LO.png vpn-peer-3.FR.conf vpn-peer-3.FR.png
.
.
.
vpn-peer-124.zip containing files: vpn-peer-124.NY.conf vpn-peer-124.NY.png vpn-peer-124.LO.conf vpn-peer-124.LO.png vpn-peer-124.FR.conf vpn-peer-124.FR.png
```
The number of files does not matter.

**Be careful - correctly indicate file names, numbers and special attention to the dot (.) after the number in the original files.**


### Requirements & Dependencies:
+ Python v.3.11
+ Zip v.3.0


### How to use:
1. install all Requirements & Dependencies
2. git clone https://github.com/NDalV/zip-loops
3. cd zip-loops/
4. python3 zip-loop.py

