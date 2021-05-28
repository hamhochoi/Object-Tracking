from utils.convert_longlat_to_cartesian import convert 
from utils.map_location import map
import math

def get_cartesian_pos(box_x_center, box_y_center):
    long, lat = map(box_x_center, box_y_center)
    cartesian_x, cartesian_y = convert(long, lat)
    return cartesian_x, cartesian_y
    

def speed_estimate(pre_box, curr_box, delta_t=10/30):
    pre_box_x_center, pre_box_y_center = pre_box
    curr_box_x_center, curr_box_y_center = curr_box
    
    pre_cartesian_x, pre_cartesian_y = get_cartesian_pos(pre_box_x_center, pre_box_y_center)
    curr_cartesian_x, curr_cartesian_y = get_cartesian_pos(curr_box_x_center, curr_box_y_center)
    
    delta_s = math.sqrt((curr_cartesian_x-pre_cartesian_x)**2 + (curr_cartesian_y-pre_cartesian_y)**2)
    
    return delta_s/delta_t * 3.6        # convert m/s to km/h


if __name__ == "__main__":
    curr_box = (874, 455)
    pre_box = (897,476)
    estimated_speed  = speed_estimate(pre_box, curr_box)
    print (estimated_speed)