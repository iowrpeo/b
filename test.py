# encoding: utf-8
import io
import json
import shutil
import smtplib
import sys
import threading
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from client import Pica
from util import *
import os 

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

p = Pica()
p.login()
p.punch_in()

with open("downloaded.txt","r") as f:
    ids = f.read().split('\n')
    for i in ids:
        #print(list(p.episodes(i).json()["data"]["eps"]["docs"]))
        print(r"{}->{}".format(i,p.comic_info(i)["data"]["comic"]["title"]))
        info = p.comic_info(i)
        if not info["data"]['comic']['isFavourite']:
            #if info["data"]['comic']['isFavourite']:
            p.favourite(i)
