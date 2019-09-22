from braille import *
from braille_support import ON, OFF
import serial

debug = True
com_port = ""

# 커서 그랩 상태 : 사용자가 소프트웨어 단에서 커서 그랩을 ON한 상태라면 1, OFF한 상태라면 0
rx_cursor = ON
# 진동피드백 상태 : 사용자가 소프트웨어단에서 진동피드백을 ON한 상태라면 1, OFF한 상태라면 0
rx_vibrate = ON
# 진동피드백 Text 상태 : 마우스 커서가 Text에 닿은 상태라면 1, 그렇지 않은 상태라면 0
rx_vibrate_text = ON
# 진동피드백 Image 상태 : 마우스 커서가 Image에 닿은 상태라면 1,: 그렇지 않은 상태라면 0
rx_vibrate_image = ON
# 점자 출력 상태 : 점자를 출력해야되는 상태라면 1, 그렇지 않은 상태라면 0
rx_output = ON

# 커서 그랩 상태: 디바이스의 실재 커서 그랩 상태 알림. 1이면 커서그랩 ON이고 0이면 커서그랩 OFF
tx_cursor = None
# 진동피드백 Text 출력 상태 : 디바이스의 실재 진동피드백 Text 출력 알림. 1이면 진동을 출력한것이고 0이면 진동출력을 안한 상태
tx_vibrate_text = None
# 진동피드백 Image 출력 상태 : 디바이스의 실재 진동피드백 Image 출력 알림. 1이면 진동을 출력한것이고 0이면 진동출력을 안한 상태
tx_vibrate_image = None
# 점자 출력 상태 : 디바이스의 실재 점자출력 알림. 1이면 점자를 출력한 것이고 0이면 점자출력을 안한 상태
tx_output = None
# 디바이스 주소 : 디바이스 주소를 전달. 소프트웨어에서 디바이스가 연결되었는지 확인할 수 있음. 설정된 주소는 1001(0x9)임.
tx_device = None

class RX:
    def __init__(self, cursor=rx_cursor, vibrate=rx_vibrate, vibrate_text=rx_vibrate_text,
                 vibrate_image=rx_vibrate_image, output=rx_output, data=(0,0,0,0,0,0)):
        self.cursor = ON if cursor else OFF
        self.vibrate = ON if vibrate else OFF
        self.vibrate_text = ON if vibrate_text else OFF
        self.vibrate_image = ON if vibrate_image else OFF
        self.output = ON if output else OFF
        self.data = data

    def raw(self):
        ret = bytearray()

        for i in range(5):
            ret.append(0)

        # Compatibility with hardware
        # 1 4
        # 2 5
        # 3 6
        ret.append(self.data[0])
        ret.append(self.data[3])
        ret.append(self.data[1])
        ret.append(self.data[4])
        ret.append(self.data[2])
        ret.append(self.data[5])

        ret.append(self.output)
        ret.append(self.vibrate_image)
        ret.append(self.vibrate_text)
        ret.append(self.vibrate)
        ret.append(self.cursor)

        return bytes(ret)


class TX:
    def __init__(self, cursor, vibrate_text, vibrate_image, output, device):
        self.cursor = ON if cursor else OFF
        self.vibrate_text = ON if vibrate_text else OFF
        self.vibrate_image = ON if vibrate_image else OFF
        self.output = ON if output else OFF
        self.device = str(device)

    def raw(self):
        ret = bytearray()

        for i in self.device:
            ret.append(int(i))

        ret.append(self.output)
        ret.append(self.vibrate_image)
        ret.append(self.vibrate_text)
        ret.append(self.cursor)

        return bytes(ret)


# 현재 설정된 데이터 변수들의 값을 콘솔에 출력하는 함수이다.
def report():
    print(rx_cursor, rx_vibrate, rx_vibrate_text, rx_vibrate_image, rx_output)
    print(tx_cursor, tx_vibrate_text, tx_vibrate_image, tx_output, tx_device)


# TODO: 기기에 UART로 패킷을 전송하는 함수이다.
def send(packet):
    if debug:
        print("Sending packet: ", packet)

    # TODO: 패킷 송신 기능 구현

    # 송신 완료(ACK) 패킷이 올 때까지
    while not receive():
        pass


# TODO: 기기로부터 UART로 패킷을 전송받는 함수이다.
def receive():
    global tx_cursor, tx_vibrate_text, tx_vibrate_image, tx_output, tx_device
    # TODO: 패킷 수신 기능 구현
    # EXAMPLE:
    raw_go_sw = TX(rx_cursor, 0, 0, rx_output, 1001).raw()
    # 수신 성공 시 True, 실패 시 False
    status = True

    if debug:
        print("Receiving packet: ", raw_go_sw)

    if type(raw_go_sw) is not bytes:
        raise RuntimeError

    # 수신된 바이트 형태의 패킷을 정수로 치환하여 리스트에 넣는다.
    packet = [i for i in raw_go_sw]
    # 역으로 수신된 패킷을 올바른 상태로 바꾼다.
    packet.reverse()

    tx_cursor = packet[0]
    tx_vibrate_text = packet[1]
    tx_vibrate_image = packet[2]
    tx_output = packet[3]
    tx_device = ''.join(str(i) for i in packet[4:])

    if debug:
        report()

    return status