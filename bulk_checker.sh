#!/bin/bash
for i in {1..254}
do
   python /root/exploits/MS17-010/checker.py 10.11.1.$i	
done
