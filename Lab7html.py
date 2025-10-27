import socket
import RPi.GPIO as gpio
import threading
from time import sleep

gpio.setmode(gpio.BCM)

pins = (19,21,22)
for p in pins:
	gpio.setup(p,gpio.OUT)

def web_page():
	html = """
		<html>
			<style>
  				body {
					border: 1px solid black; /* Sets a 5px solid blue border */
				}
			</style>

			<body>
				Brightness: <br>
				<input type="range" id="myRange" name="brightnessRange" min="0" max="100" value="0"> <br>
				<br>

				Select LED: <br>
				<input type="radio" id="led1" name="led" value="HIGH">
				<label for="led1">LED 1</label> <br>

				<input type="radio" id="led2" name="led" value="HIGH">
				<label for="led2">LED 2</label> <br>

				<input type="radio" id="led3" name="led" value="HIGH">
				<label for="led3">LED 3</label> <br>

				<br>
				<input type="submit" id="submit" name="submit" value="Change Brightness"
			</body>
		</html>
	"""
	return(bytes(html, 'utf-8'))

def parsePOSTdata(data):
	data_dict = {}
	idx = data.find('\r\n\r\n')+4
	data = data[idx:]
	data_pairs = data.split('&')
	for pair in data_pairs:
		key_val = pair.split('=')
		if len(key_val) == 2:
			data_dict[key_val[0]] = key_val[1]
	return data_dict

def serve_web_page():
    while True:
		print('Waiting for connection...')
		conn, (client_ip, client_port) = s.accept()     # blocking call
		message = parsePOSTdata(conn.recv(1024))               # read request (required even if none)
		print(message)
				
		conn.send(b'HTTP/1.1 200 OK\n')         # status line
		conn.send(b'Content-type: text/html\n') # header (content type)
		conn.send(b'Connection: close\r\n\r\n') # header (tell client to close at end)
		# send body in try block in case connection is interrupted:
		try:
			conn.sendall(web_page())                  # body
		finally:
			conn.close()
        
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP-IP socket
s.bind(('', 8080))
s.listen(3)  # up to 3 queued connections
    
webpageThread = threading.Thread(target=serve_web_page)
webpageThread.daemon = True
webpageThread.start()

try:
	while True:
		pass
except:
	print('Joining webpageTread')
	webpageTread.join()
	print('Closing socket')
	s.close()
