import socket
import time

# Configurable settings
MY_CALLSIGN = 'MYCALLSIGN-15'  # Replace with your own callsign
DESTINATION_CALLSIGN = 'APRS'  # Destination callsign
APRSIS_SERVER = 'rotate.aprs2.net'  # APRS-IS server to connect to
APRSIS_PORT = 14580  # APRS-IS server port
BEACON_INTERVAL = 60  # Beacon interval in seconds
LATITUDE = 37.7749  # Replace with your own latitude
LONGITUDE = -122.4194  # Replace with your own longitude

# Connect to APRS-IS server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((APRSIS_SERVER, APRSIS_PORT))
print('Connected to APRS-IS server')

# Send login information
login_info = 'user {} pass -1 vers python-aprs 1.0'.format(MY_CALLSIGN)
sock.sendall(login_info.encode())
print('Sent login information')

# Start beacon loop
while True:
    # Generate APRS packet
    timestamp = time.strftime('%d%H%M', time.gmtime())
    latitude = '{:.4f}{}'.format(abs(LATITUDE), 'N' if LATITUDE >= 0 else 'S')
    longitude = '{:.4f}{}'.format(abs(LONGITUDE), 'E' if LONGITUDE >= 0 else 'W')
    packet = '{}>APRS,TCPIP*:={}/{}{}'.format(MY_CALLSIGN, timestamp, latitude, longitude)
    print('Sending APRS packet:', packet)

    # Send APRS packet
    sock.sendall(packet.encode())

    # Wait for beacon interval
    time.sleep(BEACON_INTERVAL)
