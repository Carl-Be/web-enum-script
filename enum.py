#!/usr/bin/python

import subprocess as sp

target = raw_input("Enter Target: ")
export = "export TARGET=" + target
sp.call(export, shell=True)

sp.call("xdotool key \"ctrl+shift+t\"; xdotool type \" nmap -T4 -oX nmap.xml -vv -p 80 10.0.2.15 && xsltproc nmap.xml -o nmap.html && firefox nmap.html\"; xdotool key Return", shell=True)

sp.call("xdotool key \"ctrl+shift+t\"; xdotool type \" gobuster dir -t 90 -w /usr/share/dirb/wordlists/common.txt -u $TARGET\"; xdotool key Return", shell=True)

"""
sp.call("xdotool key \"ctrl+shift+t\"; xdotool type \" nmap -T4 -oX nmap.xml -vv -p 80 10.0.2.15 && xsltproc nmap.xml -o nmap.html && firefox nmap.html\"; xdotool key Return", shell=True)

sp.call("xdotool key \"ctrl+shift+t\"; xdotool type \" nmap -T4 -oX nmap.xml -vv -p 80 10.0.2.15 && xsltproc nmap.xml -o nmap.html && firefox nmap.html\"; xdotool key Return", shell=True)
"""
