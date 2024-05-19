# Disparity-to-Point-Cloud
3D point cloud of a disparity image in camera frame and base frame.

# 3D Point Calculation

$$
z = \frac{{f_x \cdot B}}{{D(u,v)}}
$$

$$
x = \frac{{(u - c_x) \cdot z}}{{f_x}}
$$

$$
y = \frac{{(v - c_y) \cdot z}}{{f_y}}
$$

Where:
- $D(u,v)$ is the disparity at pixel $(u,v)$,
- $B$ is the baseline distance between the stereo camera pair,
- $(u,v)$ are the pixel coordinates,
- $(c_x, c_y)$ are the principal point coordinates,
- $(f_x, f_y)$ are the focal lengths along the x and y axes.

# Disparity Image and its 3D Points Cloud

<div style="text-align: center;">
  <img src="Assignment/Disparity.png" alt="Disparity Image" style="max-width: 90%; height: auto;">
</div>

<div style="display: flex; justify-content: space-around; align-items: flex-start; margin-top: 20px;">
  <div style="flex: 0 0 45%; padding: 10px;">
    <img src="Assignment/camera_frame.png" alt="Camera Frame" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <p style="text-align: center; font-style: italic; margin-top: 5px;">$P_c$: 3D Points cloud in camera frame</p>
  </div>
  <div style="flex: 0 0 45%; padding: 10px;">
    <img src="Assignment/base_frame.png" alt="Base Frame" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <p style="text-align: center; font-style: italic; margin-top: 5px;">$P_b$: 3D Points cloud in base frame</p>
  </div>
</div>

$$
P_b = R^b_c \cdot P_c 
$$
