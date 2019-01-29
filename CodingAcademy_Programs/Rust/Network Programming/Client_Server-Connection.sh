#!/usr/bin/env bash

# Run the server first with a port number as a command line argument:
ozzycodes@ozzycodes-ML-LIQUID:~$ ./echoServer 1234
Read: 14 chars
About to send data!


# When the client server is run on the same port, it will receive characters and read them out:
ozzycodes@ozzycodes-ML-LIQUID:~$ ./echoClient 1234
stream info: Ok(TcpStream { addr: V4(127.0.0.1:33046), peer: V4(127.0.0.1:1234), fd: 3 })
Read: 12 chars
[72, 101, 108, 108, 111, 32, 116, 111, 111, 33, 13, 10, 0, 0, 0, 0, 0, 0, 0, 0]

#################################################################################################

# Compiling the UDP server with a given port in the terminal
ozzycodes@ozzycodes-ML-LIQUID:~$ ./UDPServer 1234
Got 1 bytes from 127.0.0.1:34595.
X
Got 1 bytes from 127.0.0.1:34595.
X
Got 1 bytes from 127.0.0.1:34595.
X
Got 1 bytes from 127.0.0.1:34595.
X
Got 1 bytes from 127.0.0.1:34595.
X

# Then use the 'netcat' function for connecting to the UDP server and relay any information
ozzycodes@ozzycodes-ML-LIQUID:~$ nc -vv -u localhost 1234
Connection to localhost 1234 port [udp/*] succeeded!
