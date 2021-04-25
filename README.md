# DeepFakeRender

## Prerequistes
We recommend using Conda to manage the environement for this project because it uses quite a few cross-platform and
non standard distributuions.

Install Pytorch3D following the instructions [here](https://github.com/facebookresearch/pytorch3d/blob/master/INSTALL.md).

Install CUB library, 



# Face Swap

Download the weights from https://drive.google.com/drive/folders/1en0H05FjO6zBppuLNW0ju5zOOrjBmYxv?usp=sharing and store in ./fsgan/weights
Cannot be stored in git as model files are too large

Code for face swap taken from https://github.com/YuvalNirkin/face_detection_dsfd and git clone https://github.com/YuvalNirkin/fsgan.git

Store source video in data/input.mp4 and target video in data/output.mp4 and run face_swap.sh to get 2D faceswapped video.
