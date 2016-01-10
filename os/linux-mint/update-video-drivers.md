# Video Driver in  Linux Mint
The video driver that comes with linux mint make the system unstable. It is necessary to update it with the proprietary driver.

### Add repository
- sudo apt-add-repository ppa:xorg-edgers/ppa 
- sudo apt-get update && sudo apt-get dist-upgrade

### Check what is the latest driver for your video card
- I am using a NVIDIA Quadro 600 GF108GL
- Go to http://www.nvidia.com/download/driverResults.aspx/95159/en-us to get to check the latest driver version


### Install driver
- aptitude search nvidia
- sudo apt-get install nvidia-352 nvidia-settings    (352 is the latest version for my video card)