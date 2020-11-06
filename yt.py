from __future__ import unicode_literals
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

import os
import youtube_dl
import sys
import datetime

link = {
'https://www.youtube.com/watch?v=9ZfN87gSjvI': 'P1',
'https://www.youtube.com/watch?v=jCAwNxhqGVE': 'P2',
'https://www.youtube.com/watch?v=3ymvdQRDHB4': 'P3',
'https://www.youtube.com/watch?v=huqJUghX26Y': 'P4',
'https://www.youtube.com/watch?v=R9vcSWb6mug': 'P5',
'https://www.youtube.com/watch?v=MozX3qFIkpQ': 'P6',
'https://www.youtube.com/watch?v=1_5n1EfcWyM': 'P7',
'https://www.youtube.com/watch?v=6pxRHBw-k8M': 'P8',
'https://www.youtube.com/watch?v=GzxlyTJD66Q': 'P9',
'https://www.youtube.com/watch?v=HLmOkDBfxv0': 'P10',
'https://www.youtube.com/watch?v=U76OX0M6f4w': 'P11',
'https://www.youtube.com/watch?v=NCTd1IHChug': 'P12',
'https://www.youtube.com/watch?v=E88TlEyTvkc': 'P13',
'https://www.youtube.com/watch?v=00VaKcv47HA': 'P14',
'https://www.youtube.com/watch?v=Bzin4pigkoM': 'P15',
'https://www.youtube.com/watch?v=5uv5FVJb-iA': 'P16',
'https://www.youtube.com/watch?v=lIWKlLZh4yQ': 'P17',
'https://www.youtube.com/watch?v=ZuaaId1s5qU': 'P18',
'https://www.youtube.com/watch?v=8HJ7mGUmlO4': 'P19',
'https://www.youtube.com/watch?v=oSEaPfnQKFI': 'P20',
'https://www.youtube.com/watch?v=qrT7rAY4IpU': 'P21',
'https://www.youtube.com/watch?v=91Js5bdjc34': 'P22',
'https://www.youtube.com/watch?v=HLFI88AEHpY': 'P23',
'https://www.youtube.com/watch?v=57W8GBUzWew': 'P24',
'https://www.youtube.com/watch?v=dm6nBhHK0-M': 'P25',
'https://www.youtube.com/watch?v=o1C9G4WNbnI': 'P26',
'https://www.youtube.com/watch?v=o8Qrv0dTYAU': 'P27',
}

path="/content/TecoGAN/videos/"
os.path.isdir(path) or os.makedirs(path)
for (k, v) in link.items():
  os.path.isdir(os.path.join(path,v)) or os.makedirs(os.path.join(path,v))
  dir_out='/content/TecoGAN/videos/'+v+'.webm'
  ydl_opts = {
    'format': 'bestvideo/best',
    'outtmpl': (dir_out)
  }
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([k])
    print(k)
    dir_target='/content/TecoGAN/fragmento/'+v+'.'
    os.path.isdir(dir_target) or os.makedirs(dir_target)

  ffmpeg_extract_subclip(dir_out,5, 10, targetname=dir_target+'1.webm') 
  ffmpeg_extract_subclip(dir_out,11, 16, targetname=dir_target+'2.webm') 
  ffmpeg_extract_subclip(dir_out,21, 27, targetname=dir_target+'3.webm') 
  ffmpeg_extract_subclip(dir_out,28, 33, targetname=dir_target+'4.webm') 
  ffmpeg_extract_subclip(dir_out,34, 39, targetname=dir_target+'5.webm') 
  ffmpeg_extract_subclip(dir_out,40, 45, targetname=dir_target+'6.webm') 
  ffmpeg_extract_subclip(dir_out,46, 51, targetname=dir_target+'7.webm') 
  ffmpeg_extract_subclip(dir_out,52, 57, targetname=dir_target+'8.webm') 
  ffmpeg_extract_subclip(dir_out,58, 63, targetname=dir_target+'9.webm') 
  ffmpeg_extract_subclip(dir_out,64, 69, targetname=dir_target+'10.webm') 
  ffmpeg_extract_subclip(dir_out,70, 75, targetname=dir_target+'11.webm') 
  ffmpeg_extract_subclip(dir_out,65, 70, targetname=dir_target+'12.webm') 
  from shutil import rmtree
  rmtree('/content/TecoGAN/videos/'+v)
