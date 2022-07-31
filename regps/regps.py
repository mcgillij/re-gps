# AUTOGENERATED! DO NOT EDIT! File to edit: ../03_regps.ipynb.

# %% auto 0
__all__ = ['regps']

# %% ../03_regps.ipynb 2
import glob

from .json_explorer import *
from .exif_explorer import *
from .date_compare import *

# %% ../03_regps.ipynb 3
def regps(image_path, # "sample-data/*.jpg"
         location_data, # "sample-data/sample.json"
         output_path # "output"
    ):
    """Take Google Location data, and map it to an image folder based on date detals"""
    images = glob.glob(image_path)
    image_list = extract_exif(images)
    locations = build_location_history(get_locations(location_data))

    deltas = get_smallest_deltas(image_list, locations)
    imgs_w_data = de_google_gps_info(deltas, image_list, locations)

    write_gps_info_to_images(imgs_w_data, output_path)
