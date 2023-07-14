from server.getFixeData import return_random, return_sweets

"""
将所有的常量信息定义在Constant类中
"""


class Constant:
    def __init__(self, host='127.0.0.1', port=1234):
        self.host = host
        self.port = port
        self.start_msg = '正在运行...........'
        self.end_msg = '运行结束...........'
        self.polite = '正在为您获取数据，请稍等：'
        self.realTimeData = {
            '天气': 'weather',
            '股票': 'stock',
            '电影': 'movie',
            '音乐': 'music'
        }
        self.fixeData = {
            '随机数': str(return_random()),
            '小黑子': '唱、跳、Rap，篮球',
            '名字': '你不对劲',
            '土味情话': str(return_sweets())
        }


class ReturnData(Constant):
    def __init__(self, msg):
        super().__init__()
        self.response_info = msg  # 后续的response_info转义后再字符传出
        """
        需要修改，匹配规则有问题，现只能精准匹配
        可以将多个hash进行拼接，之后再进行匹配
        """
        if msg in self.realTimeData.keys():
            self.implement_def = self.real_return_data(msg)
        elif msg in self.fixeData.keys():
            self.implement_def = self.fixe_return_data(msg)
        else:
            self.implement_def = self.return_data(msg)

    def return_data(self, msg):
        self.response_info = msg
        return self.response_info

    def real_return_data(self, msg):
        for i in self.realTimeData.keys():
            if i in msg:
                self.response_info = self.polite + self.realTimeData.get(i)
                break
        return self.response_info

    def fixe_return_data(self, msg):
        for i in self.fixeData.keys():
            if i in msg:
                # 处理好返回的消息体
                self.response_info = self.fixeData.get(i)
                break
        return self.response_info
