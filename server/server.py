from socket import *
from base.initial import Constant, ReturnData

constant_info = Constant()

socket_server = socket(AF_INET, SOCK_DGRAM)
host_port = (constant_info.host, constant_info.port)
socket_server.bind(host_port)

flag = True
print(constant_info.start_msg)

while flag:
    res_data = socket_server.recvfrom(1024000)  # 接收数据
    # res_data 分为两部分，消息+ip-端口
    information, src_address = res_data[0], res_data[1]
    rep_data = information.decode('utf-8')  # 将接受到的消息转义为字符
    print("接收到数据：%s" % rep_data)
    if rep_data == 'exit':
        flag = False
        print(constant_info.end_msg)

    # 将返回的消息传入到ReturnData中进行处理
    return_data = ReturnData(rep_data).implement_def
    socket_server.sendto(return_data.encode('utf-8'), src_address)      # 向客户端返回数据

socket_server.close()
