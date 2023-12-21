
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

        self.tempDir = tempDir
        self.ytGetter = YoutubeGetter(tempDir)
        self.ydl : YoutubeDL = YoutubeDL(ydl_opts)

    def __del__(self) -> None:
        self.ydl.close()

    def AddYoutubePlayListItem(self,channel_id:str,url:str) -> None:
        # プレイリストが存在しない場合は作成
        if channel_id not in self.playListById:
            self.playListById[channel_id] = PlayList()

        # URLから情報を取得
        info = self.ytGetter.getVideoInfo(self.ydl,url)
        item = PlayListItem(title=info.title,
                            id=info.id)
        self.ytGetter.getFileFromUrl(self.ydl,url)

        # プレイリストアイテムを作成
        item = PlayListItem()

        item.is_download = True
        item.file_path = self.tempDir + "/" + info.id + ".m4a"
        item.title = info.title
        item.id = url

        # プレイリストに追加
        self.playListById[channel_id].AddPlayListItem(item)

    def PopPlayListItem(self,channel_id:str) -> PlayListItem:
        return self.playListById[channel_id].Items.get()
