import json
import protocol as p
import PySimpleGUI as sg
import sys

# Get port from the user via GUI
layout = [
    [sg.Text('레구레테론 하드웨어가 연결된 COM 포트 값을 입력하세요.')],
    [sg.InputText()],
    [sg.Submit('확인')]
]

window = sg.Window("LeguLeteron").Layout(layout)
button, values = window.Read()

p.com_port = values[0]

window.Disappear()

jsonString = sys.stdin.read().strip("\n")
dict = json.loads(jsonString)

# Set configurations in protocol
p.rx_cursor = bool(dict['cursor'])
p.rx_vibrate = bool(dict['vibrate'])
p.rx_vibrate_text = bool(dict['vibrate_text'])
p.rx_vibrate_image = bool(dict['vibrate_image'])
p.rx_output = bool(dict['output'])
p.debug = bool(dict['debug'])


# # Send data to the hardware
# try:
#     string = p.beautify(p.create(dict['string']))
#     for i in string:
#         raw_go_hw = p.RX(data=i).raw()
#         p.send(raw_go_hw)
# except:
#     raw_go_hw = p.RX().raw()
#     p.send(raw_go_hw)

result = [
    [sg.Text("cursor: " + str(p.rx_cursor))],
    [sg.Text("vibrate: " + str(p.rx_vibrate))],
    [sg.Text("vibrate_text: " + str(p.rx_vibrate_text))],
    [sg.Text("vibrate_image: " + str(p.rx_vibrate_image))],
    [sg.Text("output: " + str(p.rx_output))],
    [sg.Text("debug: " + str(p.debug))],
    [sg.Text("string: " + dict['string'])],
    [sg.OK()]
]
result_window = sg.Window("LeguLeteron").layout(result)
result_window.Read()
