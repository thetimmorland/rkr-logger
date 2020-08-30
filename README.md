# Starting the dev environment
Dependencies are managed with [pipenv](https://pipenv-fork.readthedocs.io/en/latest/).

```shell
pipenv install # install dependencies
pipenv run dev # start dev environment
```

# Other dependencies
The apt package can-utils must also be installed

```
sudo apt install can-utils
sudo reboot
```

# /boot/config.txt
The Waveshare CAN hat uses spi to communicate with the RPi, so the following line must be uncommented in `/boot/config.txt`

```
dtparam=spi=on
```

To to load the CAN driver at boot the following lines must be appended to `/boot/config.txt`
```
dtoverlay=mcp2515-can0
dtparam=oscillator=12000000
dtparam=interrupt=25
dtparam=spimaxfrequency=2000000
```

# ip link
The Waveshare CAN hat 