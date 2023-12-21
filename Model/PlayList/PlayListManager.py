
from dataclasses import dataclass
from Model.Getter.Youtube import YoutubeGetter
from Model.PlayList.PlayList import PlayList, PlayListItem
from yt_dlp import YoutubeDL

class PlayListManager():
    def __init__(self,tempDir:str) -> None:
        self.playListById : dict[str,PlayList] = dict()
        self.ytGetter = YoutubeGetter(tempDir)
        
        ydl_opts = {
            'format': 'm4a/bestaudio/best',
            'outtmpl' : tempDir + "/%(id)s.%(ext)s"
        }

        self.ydl : YoutubeDL = YoutubeDL(ydl_opts)

    def __del__(self) -> None:
        self.ydl.close()

    def AddYoutubePlayListItem(self,channel_id:str,url:str) -> None:
        # プレイリストが存在しない場合は作成
        if channel_id not in self.playListById:
            self.playListById[channel_id] = PlayList()

        

        info = self.ydl.getVideoInfo(ydl,id)
        item = PlayListItem(title=info.title,
                            id=info.id)
        self.ydl.getFileFromUrl(ydl,id)

        # プレイリストアイテムを作成
        item = PlayListItem()

        item.is_download = True
        item.file_path = tempDir + "/" + info.id + ".m4a"


        item.id = url

        # プレイリストに追加
        self.playListById[channel_id].AddPlayListItem(url)

    
