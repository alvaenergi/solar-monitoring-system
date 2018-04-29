# initiate nova modem

logfile="/home/pi/alva/log/nova.log"

echo $(date) "init nova" >> $logfile
sudo hologram modem connect 2>> $logfile
#sudo python /home/pi/alva/connectInet.py >> $logfile
