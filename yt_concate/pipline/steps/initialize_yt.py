from .step import Step
from yt_concate.model.yt import YT


class InitializeYT(Step):
    def process(self, data, inputs, utils):
        return [YT(url) for url in data]  # list comprehension 針對每個data裡的url把它轉換成YT物件
