## CoPing

A Cisco style ping tool, written in Python.  This style of pinging is
much more suited to large, fast timeout pings; ideal for testing a link's
stability and consistency.

## Installing
sudo pip install coping

## Example
```
sudo coping 10.0.0.1
Type escape sequence CTRL + C to abort. 
Sending 5, 100-byte ICMP Echos to 10.0.0.1, timeout is 2 seconds: 
!!!!! 
Success rate is 100 percent (5/5), round-trip min/avg/max = 4/6/8 ms 
```
