# get the dominant color of an image

import urllib.request, io, requests, colorthief
from colorthief import ColorThief
from PIL import Image

url = URL
data = requests.get(url).content
img = io.BytesIO(data)
ctimg = ColorThief(img)
dominant_color = ctimg.get_color(quality=1)
r, g, b = dominant_color[0], dominant_color[1], dominant_color[2]
