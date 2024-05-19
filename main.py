import numpy as np
from matplotlib import pyplot as plt
import utils
# from mpl_toolkits.mplot3d import Axes3D



# Disparity image
DISPARITY_IMAGE_PATH = "Assignment/Disparity.png"
DISPARITY_IMAGE = plt.imread(DISPARITY_IMAGE_PATH)

####   CAMERA FRAME #####

# camera intrinsic matrix
CAMERA_INTRINSIC_MATRIX = np.array([
                    [398.7956237792969,0.0,315.4751892089844],
                    [0.0,398.7956237792969,205.1688232421875],
                    [0,0,1]
                    ])

# distance between the sterio camera centers
BASELINE = 0.075 #m

# Since each channel of disparity (400,640,3) is same. So using first channel 
THRESOLD = (np.mean(DISPARITY_IMAGE[:,:,0]) - 0.5*np.std(DISPARITY_IMAGE[:,:,0]))
points_cloud_camera = utils.disparity_to_point(DISPARITY_IMAGE[:,:,0], CAMERA_INTRINSIC_MATRIX, BASELINE, thresold=THRESOLD)

points_cloud_camera_scaled = (points_cloud_camera-np.min(points_cloud_camera))/(np.max(points_cloud_camera)-np.min(points_cloud_camera))


fig = plt.figure(figsize=(640/50, 400/50))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(points_cloud_camera_scaled[:, 0], points_cloud_camera_scaled[:, 1], points_cloud_camera_scaled[:, 2], c=points_cloud_camera_scaled[:, 2], cmap='plasma', s=1, alpha=1.0)

cbar = plt.colorbar(sc, ax=ax, pad=0.1)
cbar.set_label("Depth")
ax.set_title("Point Cloud in Camera Frame")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.view_init(elev=-90, azim=90)
# plt.savefig("Assignment/camera_frame.png")

plt.show()




##### BASE FRAME #####

#Transformation matrix for camera to base frame is a 3x4 matrix of the form[R|t], R=Rotation, t=Translation.
T_BF_CAM= [
           [ 0.0,  0.0, 1.0,  0.28],
           [-1.0,  0.0, 0.0,  0.0375],
           [ 0.0, -1.0, 0.0,  0.28]
           ]

point_cloud_base = utils.transform_points(transformation_matrix=T_BF_CAM, point_cloud=points_cloud_camera)
points_cloud_base_scaled = (point_cloud_base-np.min(point_cloud_base))/(np.max(point_cloud_base)-np.min(point_cloud_base))

fig = plt.figure(figsize=(640/50, 400/50))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(points_cloud_base_scaled[:, 0], points_cloud_base_scaled[:, 1], points_cloud_base_scaled[:, 2], c=points_cloud_base_scaled[:, 0], cmap='plasma', s=1, alpha=1.0)
cbar = plt.colorbar(sc, ax=ax, pad=0.1)
cbar.set_label("Depth")
ax.set_title("Point Cloud in Base Frame")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.view_init(elev=0, azim=180)
# plt.savefig("Assignment/base_frame.png")
plt.show()
