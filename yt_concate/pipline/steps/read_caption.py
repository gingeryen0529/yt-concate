
from .step import Step


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            if not utils.caption_file_exists(yt):
                continue

            captions = {}
            with open(yt.caption_filepath, 'r') as f:
                time_line = False
                time = None  # 預設time = None
                caption = None  # 預設字幕 = None
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True  # 做記號說找到時間那一行
                        time = line  # 把時間那一行存下來
                        continue  # 跳到下一行
                    if time_line:  # if time_line == True, 表示我們現在在字幕那一行
                        caption = line  # 把字幕存下來
                        captions[caption] = time  # 把key: caption, value: time,加入字典captions
                        time_line = False  # 這樣拿完這筆資料的time才會回到預設值得false,不然他就會維持True而無法拿下一筆
            yt.captions = captions

        return data
