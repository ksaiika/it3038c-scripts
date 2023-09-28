import socket

#defining array of host names
hosts = ['www.uc.edu', 'www.google.com', 'www.bing.com']

#socket.getfqdn wilh no parameters will display the current hosts information
print('Working from host: ' + socket.getfqdn())

#iterating through host list with a FOR loop
for h in hosts:
    print(socket.gethostbyname(h))




