# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

from fastbook import *
from fastai.vision.widgets import *

key = os.environ.get('AZURE_SEARCH_KEY', 'XXX')

key

results = search_images_bing(key, 'grizzly bear')
ims = results.attrgot('content_url')
len(ims)

??search_images_bing

dest = 'images/alpaca.jpg'
download_url(ims[0], dest)

ims



# +
# !pip install bing-image-downloader
from bing_image_downloader import downloader

downloader.download("alpaca", limit=150, output_dir='alpakas', adult_filter_off=True, force_replace=False, timeout=5)

path = Path('alpakas/alpaca')
# -


