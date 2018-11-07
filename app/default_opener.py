#!/usr/bin/env python2

# Copied and simplified for Python 2 from:
# https://github.com/mdn/webextensions-examples/tree/master/native-messaging
import subprocess
import sys
import json
import struct

# Python 2.x version (when sys.stdin.buffer is not defined)
# Read a message from stdin and decode it.
def getMessage():
    rawLength = sys.stdin.read(4)
    if len(rawLength) == 0:
        sys.exit(0)
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
def sendMessage(encodedMessage):
    #sys.stdout.write(encodedMessage['length'])
    #sys.stdout.write(encodedMessage['content'])
    sys.stdout.flush()

while True:
    receivedMessage = getMessage()
    subprocess.check_call(['/bin/chromium', receivedMessage['link']]);
    sendMessage(encodeMessage('OK'))
