class CrawlingError(Exception):
    def __init__(self):
        super().__init__("Load page error")