import time
import pywifi
from pywifi import const


class ConnectWifi:

    def __init__(self):
        wifi = pywifi.PyWiFi()  # 网卡接口
        self.iface = wifi.interfaces()[0]  # 第一个无线网卡
        self.iface.status()

    def test_connect(self):
        profile = pywifi.Profile()
        profile.ssid = "gisinfo_gt501"
        profile.auth = const.AUTH_ALG_OPEN  # wifi 状态
        profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi加密算法
        profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
        profile.key = "gisinfo_123"  # 密码

        self.iface.remove_all_network_profiles()  # 删除所有的wifi文件
        tmp_profile = self.iface.add_network_profile(profile)  # 设定新的链接文件
        self.iface.connect(tmp_profile)  # 链接
        time.sleep(5)
        if self.iface.status() == const.IFACE_CONNECTED:  # 判断是否连接上
            isOK = True
        else:
            isOK = False
        return isOK

    def test_disconnect(self):
        self.iface.disconnect()  # 断开所有连接
        time.sleep(3)
        assert self.iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]


try:
    instance = ConnectWifi()
    # print("无线网卡连接成功，请选择需要执行的功能(1/2)：\n 1 连接wifi \n 2 断开wifi")
    message = ""
    while message != "1" or message != "2":
        message = input("无线网卡连接成功，请选择需要执行的功能(1/2)：\n 1 连接wifi \n 2 断开wifi \n")
        if message == "1":
            print("正在连接，请稍后...")
            try:
                isOK = instance.test_connect()
                if isOK:
                    print("wifi连接成功!")
                else:
                    print("wifi连接失败...")
            except Exception as e:
                print("wifi连接失败...")
        elif message == "2":
            print("正在断开，请稍后...")
            try:
                instance.test_disconnect()
                print("wifi断开成功...")
            except Exception as e:
                print("wifi断开失败...")
        else:
            print("请输入正确的数字!")

        if message == "1" or message == "2":
            break
except Exception as e:
    print("无法连接到无线网卡...")
