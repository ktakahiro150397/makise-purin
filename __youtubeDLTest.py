import asyncio
from os import getcwd

import yt_dlp

from Model.Getter.Youtube import YoutubeGetter
from Model.PlayList.PlayList import PlayList, PlayListItem
from yt_dlp import YoutubeDL


async def main():
    # 一時フォルダを設定してインスタンス化
    tempDir = getcwd() + "/content"
    ytGetter = YoutubeGetter(tempDir)

    # 指定ファイルをダウンロード(ID指定/URL指定いずれでもOK)
    id = "Yz9ne1zaOKc"
    url = "https://www.youtube.com/watch?v=Yz9ne1zaOKc"
    # ytGetter.getFileFromUrl(id)

    # 存在チェック
    # no_exists_id = "aaabbbccc"
    # try:
    #     ytGetter.getFileFromUrl(no_exists_id)
    # except yt_dlp.utils.DownloadError as e:
    #     # エラー発生時にキャッチして対応する
    #     print(e)

    # # プレイリスト : 内容をすべて普通に落とせる
    playlist_url = "https://www.youtube.com/playlist?list=PLEi4OmzKDGqEEz5Ye-dEEFqkjXLbADdCq"
    # try:
    #    ytGetter.getFileFromUrl(playlist_url)
    # except yt_dlp.utils.DownloadError as e:
    #     # エラー発生時にキャッチして対応する
    #     print(e)

    # # 動画情報を取得
    # info = ytGetter.getVideoInfo(id)
    # print(info.id)
    # print(info.title)

    # # プレイリスト情報を取得
    # playlist_info = ytGetter.getVideoInfo(playlist_url)
    # for item in playlist_info["entries"]:
    #     print(item["id"])
    #     print(item["title"])

    # プレイリスト追加イメージ
    playList = PlayList()
        
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'outtmpl' : tempDir + "/%(id)s.%(ext)s"
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ytGetter.getVideoInfo(ydl,id)
        item = PlayListItem(title=info.title,
                            id=info.id)
        ytGetter.getFileFromUrl(ydl,id)

        item.is_download = True
        item.file_path = tempDir + "/" + info.id + ".m4a"

    playList.AddPlayListItem(item)

    print(playList.Items.queue[0])

if __name__ == "__main__":
    asyncio.run(main())
