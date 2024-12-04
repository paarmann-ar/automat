import time
from toolboxs.decorators import singleton

@singleton
class Delay():
    def __init__(self, delay_) -> None:
        print(f'I am waiting for {delay_} mili_sec...')
        delay_ /= 1000
        time.sleep(delay_)