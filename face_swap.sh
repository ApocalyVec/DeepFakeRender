# conda install pytorch torchvision cudatoolkit=10.1 -c pytorch -y
# pip3 install opencv-python ffmpeg-python youtube-dl yacs tqdm

# Store source video in ./data/source.mp4 and target in ./data/target.mp4
python ./run_fsgan.py
# result stored in ./output.mp4