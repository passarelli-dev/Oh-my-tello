import subprocess
import ipaddress
from subprocess import Popen, PIPE

ip_net = ipaddress.ip_network(u'192.168.0.1/24', strict=False) # Cambiare IP in base alla rete

# Verifica se ogni host (1-254) è online
for ip in ip_net.hosts():

    # Converti IP a Stringa per il PING
    ip = str(ip)
    
    # Ping singolo
    toping = Popen(['ping', '-c', '1', '-W', '50', ip], stdout=PIPE)
    output = toping.communicate()[0]
    hostalive = toping.returncode
    
    # Se l'host è online, stampalo
    if hostalive == 0:
        print(ip, "online")