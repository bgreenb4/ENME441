import socket
import RPi.GPIO as gpio
import threading
from time import sleep

gpio.setmode(gpio.BCM)
brightnessArray = [0,0,0]
pinArray = [17, 27, 22]
pwmArray = []

for i in range(3):
	gpio.setup(pinArray[i], gpio.OUT)

for i in range(3):
	pwmTemp = gpio.PWM(pinArray[i], 500)
	pwmArray.append(pwmTemp)

for i in range(3):
	pwmArray[i].start(0)

def web_page(brightnessArray):
	html =  """
	<html>
		<head>
			<title>LED Controller</title>
			<style>
				body {
					font-family: sans-serif;
					background-color: #f8f8f8;
				}
				.container {
					border: 3px solid black;  /* twice as thick as before */
					border-radius: 12px;
					padding: 20px;
					width: 300px;
					margin: 40px auto;
					background-color: white;
					box-shadow: 2px 2px 8px rgba(0,0,0,0.15);
				}
				.led-control {
					margin-bottom: 15px;
				}
				input[type="range"] {
					width: 100%;
				}
				.label-line {
					display: flex;
					align-items: center;
					justify-content: space-between;
					gap: 10px;
				}
				.label-line input[type=range] {
					flex-grow: 1;
				}
				.label-line span {
					width: 40px;
					textalign: right;
				}
			</style>
		</head>

		<body>
			<div class="container">
				<h3>LED Brightness Control</h3>

				<div class="led-control">
					<div class="label-line">
						<label>LED 1</label>
						<input type="range" id="led1" min="0" max="100" value="0"
							oninput="updateLED(0,this.value)">
						<span id="val1">0%</span>
					</div>
				</div>

				<div class="led-control">
					<div class="label-line">
						<label>LED 2</label>
						<input type="range" id="led2" min="0" max="100" value="0"
							oninput="updateLED(1,this.value)">
						<span id="val2">0%</span>
					</div>
				</div>

				<div class="led-control">
					<div class="label-line">
						<label>LED 3</label>
						<input type="range" id="led3" min="0" max="100" value="0"
							oninput="updateLED(2,this.value)">
						<span id="val3">0%</span>
					</div>
				</div>
			</div>
			<script>
				function updateLED(ledIndex, brightness) {

				document.getElementById("val" + (ledIndex + 1)).innerText = brightness + "%";

				fetch("/set?led=" + ledIndex + "&brightness=" + brightness)
					.catch(err => console.error('Error:', err));
				}
			</script>
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
		conn, (client_ip, client_port) = s.accept()
		client_message = conn.recv(2048).decode('utf-8')
		print(f'Message from client:\n{client_message}')
		data_dict = parsePOSTdata(client_message)
		
		if "GET /set?" in client_message:
			params = client_message.split(" ")[1].split("?")[1]
			pairs = dict(p.split("=") for p in params.split("&"))
			led = int(pairs.get("led", 0))
			brightness = int(pairs.get("brightness", 0))
			pwmArray[led].ChangeDutyCycle(brightness)
			conn.send(b"HTTP/1.1 204 No Content\r\n\r\n")
			conn.close()
			continue

		conn.send(b'HTTP/1.1 200 OK\r\n')
		conn.send(b'Content-type: text/html\r\n')
		conn.send(b'Connection: close\r\n\r\n')
		
		try:
			conn.sendall(web_page(brightnessArray))
		finally:
			conn.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8080))
s.listen(3)

webpageThread = threading.Thread(target=serve_web_page)
webpageThread.daemon = True
webpageThread.start()

try:
	while True:
		pass
except:
	print('Joining webpageTread')
	webpageThread.join()
	print('Closing socket')
	gpio.cleanup()
	s.close()
