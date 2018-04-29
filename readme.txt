cd /lib/systemd/system/
sudo nano initNova.service

cronjob
* */1 * * * /home/pi/alva/novaInit.sh
#* * * * * /home/pi/alva/novaInit.sh

---
[Unit]
Description=Initiate Nova 3G Modem
After=multi-user.target

[Service]
Type=idle
ExecStart=/bin/bash /home/pi/alva/novaInit.sh

[Install]
WantedBy=multi-user.target
---
