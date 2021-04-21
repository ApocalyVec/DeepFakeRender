import sys
import argparse
import os
import cv2
print(cv2.__version__)

def extractImages(pathIn, pathOut):
    vidcap = cv2.VideoCapture(pathIn)
    fps = vidcap.get(cv2.CAP_PROP_FPS) # get video fps
    def getFrame(sec):
        vidcap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
        hasFrames, image = vidcap.read()
        if hasFrames:
            image_path_out = os.path.join(pathOut, "image" + str(count) + ".jpg")
            cv2.imwrite(image_path_out, image)  # save frame as JPG file
            print('Saved to {0}'.format(image_path_out), end='\r', flush=True)
        return hasFrames

    sec = 0
    frameRate = 1/fps
    count = 1
    success = getFrame(sec)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)

if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video", default='data/dt2ob.mp4')
    a.add_argument("--pathOut", help="path to images", default='out/dt2ob')
    args = a.parse_args()
    print(args)
    extractImages(args.pathIn, args.pathOut)