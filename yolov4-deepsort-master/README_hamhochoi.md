## This file contains my contributions to the original project
### Car counting
- The simple algorithm is set a line for each lane of the street and increase the counting variables by one after a car passing to it.

### Speed Estimation
- The idea is taken from ![here](- https://medium.com/hal24k-techblog/how-to-track-objects-in-the-real-world-with-tensorflow-sort-and-opencv-a64d9564ccb1)

- Idea:
    + Get 4 points in a video frame (The area as large as possible)
    + Get the real world coordinates of those pixel points
    + Transform/Mapping pixels points to real coordinates using an OpenCV function
    + Mapping real coordinate into Cartesian coordination
    + Get the Cartesian coordinations of the target object at two times: current frame and one frame in the past to calculate the distance between them.
    + Compute distance of the two frames and the time interval between two frames.
    + Estimated Speed = Delta_distance / Time interval.


- Apply to this project: ![here](https://github.com/Smorodov/Multitarget-tracker/issues/295)
    - Save one frame from video and open it in image editor (gimp, ms paint etc);
    - Open Google Earth and find place with camera;
    - find 4 key points on frame and on map (points aren't on one straight line!);
    - Save coordinates in pixels and in degrees into vectors framePoints and geoPoints.
