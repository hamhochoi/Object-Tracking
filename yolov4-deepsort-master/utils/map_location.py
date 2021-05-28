import numpy as np
from utils.pixel_mapper import PixelMapper

quad_coords = {
    "lonlat": np.array([
        [45.526646, 5.974535], # Third lampost top right
        [45.527566, 5.973849], # Corner of white rumble strip top left
        [45.527904, 5.974135], # Corner of rectangular road marking bottom left
        [45.526867, 5.974826] # Corner of dashed line bottom right
    ]),
    "pixel": np.array([
        [420, 348], # Third lampost top right
        [509, 283], # Corner of white rumble strip top left
        [731, 281], # Corner of rectangular road marking bottom left
        [840, 343] # Corner of dashed line bottom right
    ])
}


pm = PixelMapper(quad_coords["pixel"], quad_coords["lonlat"])


def map(x, y):
    # x, y are pixels of center of bbox.
    uv = (x, y) 
    long, lat = pm.pixel_to_lonlat(uv)[0]
    
    return long, lat


if __name__ == "__main__":
    uv_0 = (602, 287) # Top left give way sign in frame
    long, lat = pm.pixel_to_lonlat(uv_0)[0]
    print (long, lat)
