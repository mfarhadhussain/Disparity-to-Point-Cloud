# Disparity-to-Point-Cloud
3D point cloud of a disparity image in camera frame and robot base frame.

# 3D point calcualtion
\[ Z(u,v) = \frac{{f_x \cdot B}}{{D(u,v)}} \]
\[ X = \frac{{(u - c_x) \cdot Z}}{{f_x}} \]
\[ Y = \frac{{(v - c_y) \cdot Z}}{{f_y}} \]

Where:
- \( D(u,v) \) is the disparity at pixel \((u,v)\)
- \( B \) is the baseline distance between the stereo camera pair,
- \( (u,v) \) are the pixel coordinates,
- \( (c_x, c_y) \) are the principal point coordinates,
- \( (f_x, f_y) \) are the focal lengths along the x and y axes

# Disparity image and it's 3D points cloud

<div style="text-align: center;">
  <img src="Assignment/Disparity.png" alt="Disparity Image" style="max-width: 90%; height: auto;">
</div>

<div style="display: flex; justify-content: space-around; align-items: flex-start; margin-top: 20px;">
  <div style="flex: 0 0 45%; padding: 10px;">
    <img src="Assignment/camera_frame.png" alt="Camera Frame" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <p style="text-align: center; font-style: italic; margin-top: 5px;">Camera Frame</p>
  </div>
  <div style="flex: 0 0 45%; padding: 10px;">
    <img src="Assignment/base_frame.png" alt="Base Frame" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <p style="text-align: center; font-style: italic; margin-top: 5px;">Base Frame</p>
  </div>
</div>



