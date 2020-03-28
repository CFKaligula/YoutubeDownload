import downloader


with open('urls.txt') as urls_file:
    lines = urls_file.readlines()
    for url in lines:
        file_path = downloader.download_youtube_video(url)
        downloader.convert_video_to_mp3(file_path)
