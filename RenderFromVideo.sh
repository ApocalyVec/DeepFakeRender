
video_name=ob2hw

# for getting video from youtube
#source_url=https://www.youtube.com/watch?v=5-s3ANu4eMs
#source_start=00:01:40
#source_end=00:01:50

#youtube-dl $source_url --merge-output-format mp4 -o data/source.mp4  # download source video
#ffmpeg -y -i data/source.mp4 -ss $source_start -to $source_end -r 25 data/source-shortened.mp4  # shorten the video
#rm /content/data/source_tmp.mp4

mkdir data/$video_name
python3 extract_images_from_video.py --pathIn data/${video_name}.mp4 --pathOut data/${video_name}
python3 DECA/demos/demo_reconstruct_img_out.py -i data/${video_name}/ --saveDepth True --saveObj True -s out/${video_name}
python3 make_video_from_images.py --pathIn out/${video_name} --pathOut out/${video_name}.mp4 --sourceVideo data/${video_name}.mp4 --imgPreffix vis  # must use mp4 for compatibility with moviepy's codec
python3 make_video_from_images.py --pathIn out/${video_name} --pathOut out/${video_name}.mp4 --sourceVideo data/${video_name}.mp4 --imgPreffix detailed_images