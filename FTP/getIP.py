import socket
def get_host_name_ip():
    try:
        hostname = 'www.utc.edu.vn' #socket.gethostname()
        hostip = socket.gethostbyname (hostname)
        print("hostname:", hostname)
        print("IP: ", hostip)
    except :
        print("khong lay duoc ip")


# import ipaddress as ip
# if __name__ == '__main__':
#     net4 = ip.ip_network('10.0.1.0/24')   # định nghĩa mạng net4:
#     print(net4)
#     # tìm netmask, địa chỉ mạng, địa chỉ quảng bá từ net4
#     print(net4.netmask)
#     print(net4.network_address)
#     print(net4.broadcast_address)
#     print(net4.num_addresses)
#     print(net4.hosts)
#     print(net4.subnets())
#     print(net4.supernet())
