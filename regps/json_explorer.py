# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_json_explorer.ipynb.

# %% auto 0
__all__ = ['Location', 'get_timestamp', 'get_locations', 'build_location_history']

# %% ../00_json_explorer.ipynb 4
from datetime import datetime
from collections import namedtuple
import json

# %% ../00_json_explorer.ipynb 5
# make a datastructure to hold location data
Location = namedtuple("Location", ["timestamp", "latitude", "longitude", "accuracy"])

# %% ../00_json_explorer.ipynb 7
def get_timestamp(timestamp): # Example: 2022-06-24T19:38:55.633Z or 2022-06-24T19:38:55Z
    """
    Google stores the timestamp in different formats, making this annoying
    """
    try:
        first_format = "%Y-%m-%dT%H:%M:%S.%fZ"
        timestamp=datetime.strptime(timestamp, first_format)
    except:
        second_format = "%Y-%m-%dT%H:%M:%SZ"
        timestamp=datetime.strptime(timestamp, second_format)
    return int(timestamp.timestamp())

# %% ../00_json_explorer.ipynb 13
def get_locations(file_to_open): 
    with open(file_to_open, 'r') as f:
        json_file = json.load(f)
        return [l for l in json_file["locations"]]    

# %% ../00_json_explorer.ipynb 18
# build up the location history
# due to the malformed google data, not all entries have latitudeE7/longitudeE7
# and the differing timestamps, best effort to parse those.

def build_location_history(locations):
    location_history = [Location(get_timestamp(l["timestamp"]), l["latitudeE7"], l["longitudeE7"], l["accuracy"]) for l in locations if l.get("latitudeE7")]
    # sort by timestamp
    location_history.sort(key=lambda location: location.timestamp)
    return location_history
