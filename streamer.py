from torrentool.api import Torrent
import os
#filename="KaanMasti\ is\ Live\ again\ -\ -\ yeh\ saare\ milke\ humko\ ..-.mp4 "
from qbittorrentapi import Client
import requests
import subprocess
import sys

filename = input("enter the file name ")
magnew = input("enter the magnet link to stream ")

print("initiating stream ...")

def main():
	webtorrent_stream(magnew+'&dn='+filename)
        

# Handle Streaming

def webtorrent_stream(magnet_link: str):
    cmd = []
    cmd.append("webtorrent")
    cmd.append(magnet_link)
    
    cmd.append('--vlc')

    if sys.platform.startswith('linux'):
        subprocess.call(cmd)
    elif sys.platform.startswith('win32'):
        subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    main()