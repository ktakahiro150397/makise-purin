

from dataclasses import dataclass
from pathlib import Path

from Model.Getter.Youtube import YoutubeGetter

@dataclass
class PlayListItem():
    def __init__(self,title:str,id:str) -> None:
        self.title : str = title
        self.id : str = id

        self.is_download : bool = False
        self.file_path : Path = None

@dataclass
class PlayList():

    def __init__(self) -> None:
        self.Items : list[PlayListItem] = []

    def AddPlayListItem(self,item:PlayListItem) -> None:
        self.Items.append(item)

    # async def __download_playlist_item(self) -> None:
    #     # ダウンロードしていないプレイリストアイテムを取得
    #     not_downloaded_items = [item for item in self.Items if item.is_download == False]

    #     # それぞれに対してダウンロードを実行
    #     pass
    



    