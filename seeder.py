#creating torrent
from torrentool.api import Torrent
import os
from qbittorrentapi import Client
import requests
import subprocess
import sys

filename = input("please enter the file name to be seeded ")

#filename="a1.mkv"
#creating torrent for sharing
os.system("py3createtorrent "+ filename)
#seeding and DHT formation
client = Client(host = "http://192.168.1.5:8080/",username='admin',password='adminadmin')
tor = client.torrents.info()
#client.torrents_add(torrent_files = '/home/silver/Desktop/torflix/seed/a1.mkv.torrent')
#Added the file file to the torrent list

client.torrents_add(torrent_files = filename +'.torrent')

print("successfully added the torrent and the magnet link for sharing is:")
my_torrent = Torrent.from_file(filename+'.torrent')
magb = my_torrent.magnet_link
print(magb)