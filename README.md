# vto-ivy
ivy tools for vto users

-------------------------------------------------------------------------------
cd ivy-c-master/src
make
=> libivy.a
cd ivy-c-master/tools
make
=> ivyprobe
./ivyprobe -b 192.168.1.255

-------------------------------------------------------------------------------
cd ivy-python-master/examples
pyhello.py -b 255:2010
ivyprobe.py -b 255:2010 '(.*)'

-------------------------------------------------------------------------------
from paparazzi-uav launchpad:
- https://launchpad.net/~paparazzi-uav/+archive/ubuntu/ppa/+sourcefiles/ivy-c/3.15.1ubuntu1/ivy-c_3.15.1ubuntu1.tar.xz
- https://launchpad.net/~paparazzi-uav/+archive/ubuntu/ppa/+sourcefiles/ivy-python/3.3-0ppa2~jammy2/ivy-python_3.3.orig.tar.gz
