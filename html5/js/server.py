import websocket

class server:
	
	conn=0
	users=[]
	socket=0
	uid=0
	
	def __init__(self,address,port,connections):
		# Point Of No Return!!!
		self.socket = websocket.WebSocket((address, port), connections, self)
 
if __name__ == "__main__":
	websocketServer = server(address="127.0.0.1", port=1234, connections=1000)