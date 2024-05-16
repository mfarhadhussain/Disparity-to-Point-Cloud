
import numpy as np
""" 
    camera_intrinsic_matrix = [
                                [f_x, 0, u_0],
                                [0, f_y, v_0],
                                [0, 0, 1]
                                ]
"""

# def disparity_to_point(disparity, camera_intrinsic_matrix, baseline):
#     f_x = camera_intrinsic_matrix[0, 0]
#     f_y = camera_intrinsic_matrix[1,1]
#     u_0 = camera_intrinsic_matrix[0, 2]
#     v_0 = camera_intrinsic_matrix[1, 2]
    
#     n_rows, n_columns = disparity.shape
#     points = np.zeros((n_rows * n_columns, 3))

#     mean_disparity = np.mean(disparity)
#     std_disparity = np.std(disparity)

#     for v in range(n_rows):
#         for u in range(n_columns):
#             d = disparity[v, u]
#             if d > (mean_disparity - 0.5*std_disparity):
#                 z = (f_x * baseline) / d
#                 x = (u - u_0) * z / f_x
#                 y = (v - v_0) * z / f_y
#                 points[v * n_columns + u]  = np.array([x, y, y])
#             else:
#                 points[v * n_columns + u]  = np.array([np.nan, np.nan, np.nana])
                
#     return points[~np.isnan(points).any(axis=1)]


def disparity_to_point(disparity, camera_intrinsic_matrix, baseline):
    f_x = camera_intrinsic_matrix[0, 0]
    f_y = camera_intrinsic_matrix[1, 1]
    u_0 = camera_intrinsic_matrix[0, 2]
    v_0 = camera_intrinsic_matrix[1, 2]
    
    n_rows, n_columns = disparity.shape
    points = []

    mean_disparity = np.mean(disparity)
    std_disparity = np.std(disparity)

    for v in range(n_rows):
        for u in range(n_columns):
            d = disparity[v, u]
            if d > (mean_disparity - 0.5 * std_disparity):
                z = (f_x * baseline) / d
                x = (u - u_0) * z / f_x
                y = (v - v_0) * z / f_y
                points.append([x, y, z])
                
    return np.array(points)


def transform_points(transformation_matrix, point_cloud): # point_cloud shape: (N, 3), transformation_matrix shape: (3,4)

    point_cloud = np.hstack((point_cloud, np.ones((point_cloud.shape[0], 1)))) # homogeneous
    return (np.dot(transformation_matrix, point_cloud.T)).T

