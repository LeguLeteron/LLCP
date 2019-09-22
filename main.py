import argparse
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


# Show help when an error happens
class HelpParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


# Initialise argument parser
parser = HelpParser()

# Add arguments
parser.add_argument("-c", "--cursor", type=bool, default=False, help="Cursor Grab Status")
parser.add_argument("-v", "--vibrate", type=bool, default=False, help="Vibrate Feedback Status")
parser.add_argument("-t", "--vibrate-text", type=bool, default=False, help="Vibrate Feedback via Text Status")
parser.add_argument("-i", "--vibrate-image", type=bool, default=False, help="Vibrate Feedback via Image Status")
parser.add_argument("-o", "--output", type=bool, default=False, help="Physical Braille Output Status")
parser.add_argument("-s", "--string", type=str, help="String that will be converted to braille")
parser.add_argument("-d", "--debug", type=bool, default=False, help="Debug Mode Status")

# Parse arguments
args = parser.parse_args()

# Set configurations in protocol
p.rx_cursor = args.cursor
p.rx_vibrate = args.vibrate
p.rx_vibrate_text = args.vibrate_text
p.rx_vibrate_image = args.vibrate_image
p.rx_output = args.output
p.debug = args.debug

# If none were given
if len(sys.argv) > 1:
    jsonString = sys.stdin.read().strip("\n")
    dict = json.loads(jsonString)


# Send data to the hardware
try:
    try:
        string = p.beautify(p.create(args.string))
        for i in string:
            raw_go_hw = p.RX(data=i).raw()
            p.send(raw_go_hw)
    except:
        raw_go_hw = p.RX().raw()
        p.send(raw_go_hw)
except:
    parser.error("incorrect configuration")