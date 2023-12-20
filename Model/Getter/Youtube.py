
from pathlib import Path
from yt_dlp import YoutubeDL

class FileGetterBase():
    def __init__(self) -> None:
        pass

class YoutubeGetter(FileGetterBase):
    '''Youtubeからファイルを取得するクラス'''

    def __init__(self,tempDir:str) -> None:
        self.tempDir = tempDir

    def getFileFromUrl(self, url:str) -> None:
        """指定したURLからファイルをダウンロードし、一時フォルダに保存する。

        Args:
            url (str): ダウンロードするファイルのURL。動画IDでも可。
        """

        # オプション
        ydl_opts = {
            'format': 'm4a/bestaudio/best',
            'outtmpl' : self.tempDir + "/%(id)s.%(ext)s"
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])


    def isExists(self,ydl:YoutubeDL,url:str) -> bool:
        pass

    def isExists(self, url:str) -> bool:
        with YoutubeDL() as ydl:
            return self.isExists(ydl,url)