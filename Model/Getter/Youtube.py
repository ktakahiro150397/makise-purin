
from pathlib import Path
from yt_dlp import YoutubeDL

class FileGetterBase():
    def __init__(self) -> None:
        pass

class YoutubeGetter(FileGetterBase):
    '''Youtubeからファイルを取得するクラス'''

    def __init__(self,tempDir:str) -> None:
        self.tempDir = tempDir

        # オプション
        self.ydl_opts = {
            'format': 'm4a/bestaudio/best',
            'outtmpl' : self.tempDir + "/%(id)s.%(ext)s"
        }

    def getFileFromUrl(self, url:str) -> None:
        """指定したURLからファイルをダウンロードし、一時フォルダに保存する。

        Args:
            url (str): ダウンロードするファイルのURL。動画IDでも可。
        """
        with YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([url])

    def getFileFromUrl(self, ydl:YoutubeDL, url:str) -> None:
        ydl.download([url])

    def getVideoInfo(self,url:str):
        with YoutubeDL() as ydl:
            return ydl.extract_info(url,download=False)