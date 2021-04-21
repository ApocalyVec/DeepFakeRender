import argparse
import os
from os.path import isfile, join
from ffpyplayer.player import MediaPlayer
import cv2
from moviepy.editor import *
import moviepy.editor as mp

def makeVideo(pathIn, pathOut, sourceVideo, imgPreffix):
    fps = 29.97  # match the original video's framerate
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f)) if imgPreffix in f]  # for sorting the file names properly
    files.sort(key=lambda x: int(''.join([i for i in x if i.isdigit()])))  # sort the files by numbering

    for i in range(len(files)):
        print('Processing from {0} of {0}'.format(i + 1, len(files)), end='\r', flush=True)
        filename = os.path.join(pathIn, files[i])
        # reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        # inserting the frames into an image array
        frame_array.append(img)
    assert size
    out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'XVID'), fps, size)
    for i in range(len(frame_array)):
        print('Writing from {0} of {0}'.format(i + 1, len(frame_array)), end='\r', flush=True)
        # writing to a image array
        out.write(frame_array[i])
    out.release()

    # add back the audio
    audio_temp_path = '.temp_audio.mp3'
    clip = VideoFileClip(pathOut)
    source_clip = mp.VideoFileClip(sourceVideo)
    source_clip.audio.write_audiofile(audio_temp_path)
    source_audioclip = AudioFileClip(audio_temp_path)
    clip = clip.set_audio(source_audioclip)
    clip.write_videofile(pathOut.split('.')[0] + '_' + imgPreffix + '_audio.' + pathOut.split('.')[1])
    os.remove(audio_temp_path)

if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video", default='out/dt2ob')
    a.add_argument("--pathOut", help="path to images", default='out/dt2ob.mp4')
    a.add_argument("--sourceVideo", help="Source video to extract audio", default='data/dt2ob.mp4')
    a.add_argument("--imgPreffix", help="preffix of the images", default='vis')

    args = a.parse_args()
    print(args)
    makeVideo(args.pathIn, args.pathOut, args.sourceVideo, args.imgPreffix)