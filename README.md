# HTTP(S) Honeypot

This is a simple HTTP(S) honeypot.

## How to Run

1. Ensure you have Python installed.
2. Run the honeypot script with:
   ```bash
   sudo python3 http_https_honeypot.p

The honeypot will start listening on:
HTTP: Port 8080
HTTPS: Port 8443y
To test the honeypot, open a web browser on a remote machine and visit:

HTTP: http://192.168.100.153:8080
HTTPS: https://192.168.100.153:8443 (Accept the SSL warning)
All activities are  logged for analysis. You can find the logs in honeypot_log.txt.

Below are sample screenshots of the honeypot in action:

