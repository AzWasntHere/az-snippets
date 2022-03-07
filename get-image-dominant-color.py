# get the dominant color of an image

import urllib.request, io, requests, colorthief
from colorthief import ColorThief
from PIL import Image

#replace URL with a valid image url (the ones ending in something like .png or .jpg (MAYBE gifs))

url = URL
data = requests.get(url).content
img = io.BytesIO(data)
ctimg = ColorThief(img)
dominant_color = ctimg.get_color(quality=1)

# or if your not using an url
color_thief = ColorThief('/path/to/image')
dominant_color = color_thief.get_color(quality=1)
