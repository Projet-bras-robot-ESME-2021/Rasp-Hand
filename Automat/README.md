
To lauch the script on launch of RaspberryPi
add this line in /etc/rc.local  before "exit 0" :
sudo bash /home/pi/runarm.sh &

the runarms.sh and connect.sh should be located in /home/pi/

the two files are scripts :
- connect.sh is to connect via bluetooth the PS4 controller
- runarm.sh activates the environment and lauch the main python program
