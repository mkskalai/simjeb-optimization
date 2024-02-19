import numpy as np
import pyvista as pv


def random_downsample_pv_pointcloud(pointcloud, target_num_points):
    """
    Randomly downsample a PyVista point cloud to a specified number of points.

    Parameters:
    - pointcloud (pyvista.PolyData): Input point cloud.
    - target_num_points (int): Target number of points in the downsampled point cloud.

    Returns:
    - pyvista.PolyData: Downsampled point cloud.
    """

    return pv.PolyData(
        random_downsample_points(pointcloud.points, target_num_points)
    )


def random_downsample_points(points, target_num_points):
    """
    Randomly downsample a PyVista point cloud to a specified number of points.

    Parameters:
    - points (3xN np.array): Input point cloud.
    - target_num_points (int): Target number of points in the downsampled point cloud.

    Returns:
    - 3xN np.array: Downsampled point cloud.
    """
    # Get the number of points in the original point cloud
    total_points = len(points)

    # Check if the target number of points is greater than the total number of points
    if target_num_points >= total_points:
        return points  # No downsampling needed

    # Generate random indices for the downsampled point cloud
    random_indices = np.random.choice(total_points, size=target_num_points, replace=False)

    # Extract the selected points from the original point cloud
    downsampled_points = points[random_indices]

    return downsampled_points
