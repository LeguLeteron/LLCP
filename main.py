import argparse
import protocol as p
import sys


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

# Send data to the hardware
try:
    try:
        string = p.beautify(p.create(args.string))
        for i in string:
            raw_go_hw = p.RX(i).raw()
            p.send(raw_go_hw)
    except:
        raw_go_hw = p.RX().raw()
        p.send(raw_go_hw)
except:
    parser.error("incorrect configuration")