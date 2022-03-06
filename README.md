# Input pepup by selenium

## Preparation

This script is tested on Ubuntu 20.04.
install selenium via apt and run selenium docker. (As for selenium docker image, see https://github.com/SeleniumHQ/docker-selenium)

```
$ tail -1 /etc/lsb-release 
DISTRIB_DESCRIPTION="Ubuntu 20.04.4 LTS"

$ sudo apt install python3-selenium

$ docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome:4.1.2-20220217
```

## How to use the script

Beofre executing the script, make sure the selenium docker(chrome) is running.

```
$ python3 pepup_auto_input.py --user user_name --password credentials
```
