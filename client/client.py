from socket import *
from base.initial import Constant

constant_info = Constant()
client_socket = socket(AF_INET, SOCK_DGRAM)
server_host_port = (constant_info.host, constant_info.port)
flag = True
while flag:
    res_data = input("请输入需要发送的数据：").encode('utf-8')
    client_socket.sendto(res_data, server_host_port)  # 发送消息
    rep_data = client_socket.recvfrom(1024000)[0]  # 接收消息
    response_data = rep_data.decode('utf-8')
    # 也可以将返回的数据进行处理后打印
    print("接收到的数据为：%s" % type(response_data))
    # 在客户端发送时，需要进行编码
    if res_data.decode('utf-8') == 'exit':
        flag = False
        print("运行结束...........")
client_socket.close()
