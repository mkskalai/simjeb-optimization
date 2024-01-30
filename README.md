# simjeb-optimization
## Notes
### 30.01.2023
- 8x512 DeepSDF makes around 10 epochs / h on CPU. consider switching to cloud
  - especially since probably many experiments will be required
### EDA
- tSNE and PCA didn't work on SDF clusters
- ToDo: research about pyvista's SDF
- working solution: pointcloud density, define t-test?
### SDF
- pyvista SDF gives nonsense
  - SDF is OK and fast! was bug in my code
- ToDO: check out trimesh, IGL
  - unnecessary
 ### DeepSDF
 - preprocessing is bad (libraries conflicts, slow, non-robust), substitute with PyVista's
 - change architecture a bit due to my knowledge and memory limits
 - skimage can't be instaled, but mesh generation can be easily handled by PyVista
 - CUDA is a pain, need to compile PyTorch with CUDA
 ### ToDo
 - filter outliers: Done
 - train DeepSDF
 - try out voxelization
