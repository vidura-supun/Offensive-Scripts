# Offensive-Scripts
Collection of Offensive Tools coded to make life easier

## Shell Encoder 

This script will powershell encode the revershell command for ommiting  special characters to be used with RCEs and injecttion attacks with high success rate.

### External Scripts Used
**CONPTY shell** - https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1

**Powercat** - https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1

### Setup

1. Clone the repo to KALI and run setup.sh

2. Start a Simple webserver on a desired port
```sh
sudo python3 -m http.server 443 
```
3. Run the script
```sh
python shell_encoder.py
```
