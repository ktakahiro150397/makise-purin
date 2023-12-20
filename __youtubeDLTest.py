import asyncio
from os import getcwd

import yt_dlp

from Model.Getter.Youtube import YoutubeGetter


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
    # playlist_url = "https://www.youtube.com/playlist?list=PLEi4OmzKDGqEEz5Ye-dEEFqkjXLbADdCq"
    # try:
    #    ytGetter.getFileFromUrl(playlist_url)
    # except yt_dlp.utils.DownloadError as e:
    #     # エラー発生時にキャッチして対応する
    #     print(e)

if __name__ == "__main__":
    asyncio.run(main())
