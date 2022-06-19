from pytube import YouTube


def download(link: str, download_path:str):
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    video.download(download_path)
