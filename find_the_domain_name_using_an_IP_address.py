# 3. Find the domain name using an IP address

"""For this Python challenge, you'll want to import the Python socket library. That’s the only hint. 
Write a function that accepts an IP address, makes a DNS request, and returns the domain name that maps to that 
IP address using PTR DNS records."""


import socket

def get_domain_name(ip_address):

    return socket.gethostbyaddr(ip_address)[0]


print(get_domain_name("8.8.8.8"), "\t GOOGLE")
print(get_domain_name("207.46.170.123"), "\t MICROSOFT")

