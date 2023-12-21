

from dataclasses import dataclass
from pathlib import Path
from queue import Queue

from discord import FFmpegPCMAudio

from Model.Getter.Youtube import YoutubeGetter

@dataclass
class PlayListItem():
    title : str = ""
    id : str = ""

    is_download : bool = False
    file_path : Path = None

    def get_discord_FFmpegPCMAudio(self) -> FFmpegPCMAudio:
        return FFmpegPCMAudio(self.file_path)

@dataclass
class PlayList():

    def __init__(self) -> None:
        self.Items : Queue = Queue()

    def AddPlayListItem(self,item:PlayListItem) -> None:
        self.Items.put(item)
    