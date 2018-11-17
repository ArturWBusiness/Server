import socket
socket.setdefaulttimeout(0.01)
# ip = input("[@] IP: ")
ip_head = "192.168.0"
for ip_end in range(0, 24):
	ip = ip_head + "." + str(ip_end)
	for port in range(0, 256):
		try:
			s = socket.socket()
			s.connect((ip, port))
			print("    [!] Port found on " + ip + ":" + str(port))
		except:
			pass