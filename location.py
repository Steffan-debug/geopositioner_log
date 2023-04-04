import socket
import geocoder

# Get the computer's hostname and IP address
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# Get the computer's location using the geocoder library
g = geocoder.ip('me')
location = g.latlng
print(location)

# Get the network information using the socket library
network_info = socket.gethostbyaddr(ip_address)



with open('computer_info.txt', 'w') as f:
    f.write(f'Hostname: {hostname}\n')
    f.write(f'IP address: {ip_address}\n')
    f.write(f'Latitude: {location[0]}\n')
    f.write(f'Longitude: {location[1]}\n')
    f.write(f'Network info: {network_info}\n')