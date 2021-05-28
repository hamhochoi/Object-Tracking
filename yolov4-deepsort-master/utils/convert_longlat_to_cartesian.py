from pyproj import Transformer

transformer = Transformer.from_crs(4326, 3857, always_xy=True) # Enforce lon,lat order

def convert(long, lat):
    x, y = transformer.transform(*(long, lat))
    return x, y
    
    
if __name__ == "__main__":
    lonlat_1 = (5.9740689, 45.52755007) # Center of the roundabout on googlemaps
    xy_1 = transformer.transform(*lonlat_1)
    print (xy_1)