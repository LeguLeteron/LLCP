import argparse
import protocol as p

# Initialise argument parser
parser = argparse.ArgumentParser()

# Add arguments
parser.add_argument("-c", "--cursor", type=bool, default=False, help="Cursor Grab Status")
parser.add_argument("-v", "--vibrate", type=bool, default=False, help="Vibrate Feedback Status")
parser.add_argument("-t", "--vibrate-text", type=bool, default=False, help="Vibrate Feedback via Text Status")
parser.add_argument("-i", "--vibrate-image", type=bool, default=False, help="Vibrate Feedback via Image Status")
parser.add_argument("-o", "--output", type=bool, default=False, help="Physical Braille Output Status")
parser.add_argument("-s", "--string", type=str, help="String that will be converted to braille")

# Parse arguments
args = parser.parse_args()

# Set configurations in protocol
p.rx_cursor = args.cursor
p.rx_vibrate = args.vibrate
p.rx_vibrate_text = args.vibrate_text
p.rx_vibrate_image = args.vibrate_image
p.rx_output = args.output

# Send data to the hardware
string = p.beautify(p.create(args.string))
for i in string:
    raw_go_hw = p.RX(i).raw()
    p.send(raw_go_hw)