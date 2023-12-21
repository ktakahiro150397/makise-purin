

from dataclasses import dataclass
from pathlib import Path
from queue import Queue

from Model.Getter.Youtube import YoutubeGetter

@dataclass
class PlayListItem():
    title : str = ""
    id : str = ""

    is_download : bool = False
    file_path : Path = None

@dataclass
class PlayList():

    def __init__(self) -> None:
        self.Items : Queue = Queue()

    def AddPlayListItem(self,item:PlayListItem) -> None:
        self.Items.put(item)

    # async def __download_playlist_item(self) -> None:
    #     # ダウンロードしていないプレイリストアイテムを取得
    #     not_downloaded_items = [item for item in self.Items if item.is_download == False]

    #     # それぞれに対してダウンロードを実行
    #     pass
    



    