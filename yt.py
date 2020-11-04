from __future__ import unicode_literals
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

import youtube_dl
import os
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

for (k, v) in link.items():
  ydl_opts = {
    'format': 'bestvideo/best',
    'outtmpl': os.path.join('/content/TecoGAN/videos',  v + '/%(title)s.%(ext)s',
  }
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([k])
    print(k)
    ffmpeg_extract_subclip("/content/TecoGAN/videos/P1/Landscapes - Volume 4K (UHD).webm",65, 70, targetname="/content/TecoGAN/videos/P1/1/2000.webm") 
    ffmpeg_extract_subclip("/content/TecoGAN/videos/P2/Panasonic 4K World - Rio de Janeiro, Brazil.webm",65, 70, targetname="/content/TecoGAN/videos/P2/1/2002.webm") 
