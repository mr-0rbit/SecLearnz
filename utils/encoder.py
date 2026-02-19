import base64
import urllib.parse


def encode_payload(payloads, mode):

    encoded = []

    for p in payloads:

        if mode == "url":
            encoded.append(urllib.parse.quote(p))

        elif mode == "base64":
            b = base64.b64encode(p.encode())
            encoded.append(b.decode())

        elif mode == "hex":
            encoded.append(p.encode().hex())

    return encoded
