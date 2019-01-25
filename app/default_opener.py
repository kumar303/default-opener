#!/usr/bin/env python3

# Copied and simplified for Python 2 from:
# https://github.com/mdn/webextensions-examples/tree/master/native-messaging
#import subprocess
import sys
import json
import struct
import webbrowser

# Python 2.x version (when sys.stdin.buffer is not defined)
# Read a message from stdin and decode it.
def getMessage():
    rawLength = sys.stdin.read(4).encode()
    if len(rawLength) == 0:
        return None
    messageLength = struct.unpack('@I', rawLength)[0]
    message = sys.stdin.read(messageLength)
    return json.loads(message)

# Encode a message for transmission,
# given its content.
def encodeMessage(messageContent):
    encodedContent = json.dumps(messageContent)
    encodedLength = struct.pack('@I', len(encodedContent))
    return {'length': encodedLength, 'content': encodedContent}

# Send an encoded message to stdout
# Not used anymore
def sendMessage(encodedMessage):
    #sys.stdout.write(encodedMessage['length'])
    #sys.stdout.write(encodedMessage['content'])
    sys.stdout.flush()

while True:
    receivedMessage = getMessage()
    if not receivedMessage:
         continue
    webbrowser.open_new_tab(receivedMessage['link'])
