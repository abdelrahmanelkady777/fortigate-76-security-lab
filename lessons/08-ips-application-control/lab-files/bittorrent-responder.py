#!/usr/bin/env python3
"""One-shot BitTorrent-handshake responder for the isolated Lesson 08 lab."""

import socket

HOST = "10.60.60.100"
PORT = 80

HANDSHAKE = (
    b"\x13BitTorrent protocol"
    + b"\x00" * 8
    + b"A" * 20
    + b"-AL0001-"
    + b"B" * 12
)

with socket.socket() as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Waiting for controlled BitTorrent handshake on {HOST}:{PORT}...", flush=True)

    client, address = server.accept()
    with client:
        request = client.recv(1024)
        print(f"Received {len(request)} bytes from {address}", flush=True)
        client.sendall(HANDSHAKE)
