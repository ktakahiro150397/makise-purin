
from dataclasses import dataclass
from pathlib import Path
from yt_dlp import YoutubeDL


@dataclass    
class YoutubeVideoInfo():
    id : str = ""
    title : str = ""

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

    def getVideoInfo(self,url:str) -> YoutubeVideoInfo:
        with YoutubeDL() as ydl:
            return self.getVideoInfo(ydl,url)

    def getVideoInfo(self, ydl:YoutubeDL,url:str) -> YoutubeVideoInfo:
        info = ydl.extract_info(url,download=False)
        return YoutubeVideoInfo(info["id"],info["title"])
