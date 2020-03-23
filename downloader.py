import os
from moviepy.editor import *
import pytube  # pip install pytube 3


def download_youtube_video(url):
    # download video from YouTube
    youtube = pytube.YouTube(url)
    videoTitle = youtube.title
    video = youtube.streams.filter().first()
    file_path = video.download()
    return file_path


def convert_video_to_mp3(file_path):
    # convert video to audio
    video = VideoFileClip(file_path)
    video.audio.write_audiofile(os.path.join(os.path.curdir, file_path[:len(file_path)-4] + '.mp3'))
    # remove video
    video.close()
    os.remove(file_path)
