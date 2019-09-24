#!/usr/bin/env python

import sys
import json
import struct
import protocol as p


# Python 3.x version
# Read a message from stdin and decode it.
def getMessage():
    rawLength = sys.stdin.buffer.read(4)
    if len(rawLength) == 0:
        sys.exit(0)
    messageLength = struct.unpack('@I', rawLength)[0]
    message = sys.stdin.buffer.read(messageLength).decode('utf-8')
    return json.loads(message)

# Encode a message for transmission,
# given its content.
def encodeMessage(messageContent):
    encodedContent = json.dumps(messageContent).encode('utf-8')
    encodedLength = struct.pack('@I', len(encodedContent))
    return {'length': encodedLength, 'content': encodedContent}

# Send an encoded message to stdout
def sendMessage(encodedMessage):
    sys.stdout.buffer.write(encodedMessage['length'])
    sys.stdout.buffer.write(encodedMessage['content'])
    sys.stdout.buffer.flush()

def loadProtocol(dict):
    p.com_port = bool(dict['com_port'])
    p.rx_cursor = bool(dict['cursor'])
    p.rx_vibrate = bool(dict['vibrate'])
    p.rx_vibrate_text = bool(dict['vibrate_text'])
    p.rx_vibrate_image = bool(dict['vibrate_image'])
    p.rx_output = bool(dict['output'])
    p.debug = bool(dict['string'])

while True:
    receivedMessage = getMessage()
    with open("debug.txt", "wt") as f:
        f.write(receivedMessage)
    sendMessage(encodeMessage(receivedMessage))