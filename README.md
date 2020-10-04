# pwm manage

This bunch of scripts populated on engine control via RPI

## Install

```shell script
./pwm.sh help
Usage: pwm.sh  [OPTION]
pwm manager (install|remove|update).
OPTION                   DESCRIPTION
install            install $PROJECT_NAME script
remove             stop and remove $PROJECT_NAME script from your system
update             update $PROJECT_NAME script on your system
help               show help message "
```

View pwm_manage daemon status:

```shell script
sudo systemctl status pwm_manage
```


### Static ip to WIFI interface

add  to /etc/dhcpcd.conf
```
interface wlan1
static ip_address=192.168.99.20
static routers=192.168.99.1
static domain_name_servers=8.8.8.8
```
### ROAD MAP 

[ ] make asymc function for the pwm manager 
[ ] make module from this bunch of scripts
[ ] add .toml config support 
