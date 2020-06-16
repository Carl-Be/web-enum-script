#!/usr/bin/python

import subprocess as sp
import os

# Enter Target IP Address
target = raw_input("Enter Target: ")

os.putenv("TARGET", target)

sp.call("xdotool key \"ctrl+shift+t\"; xdotool type \" gobuster dir -t 90 -w /usr/share/dirb/wordlists/common.txt -u $TARGET\"; xdotool key Return", shell=True)

sp.call("xdotool key \"ctrl+shift+t\"; xdotool type \" gobuster dir -t 90 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -u $TARGET\"; xdotool key Return", shell=True)

sp.call("xdotool key \"ctrl+shift+t\"; xdotool type \" nikto -h $TARGET\"; xdotool key Return", shell=True)

sp.call("xdotool key \"ctrl+shift+t\"; xdotool type \" sudo nmap -A -T4 -oX nmap.xml -vv $TARGET && xsltproc nmap.xml -o nmap.html\"; xdotool key Return", shell=True)
