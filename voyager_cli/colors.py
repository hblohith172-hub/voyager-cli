python
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

    @classmethod
    def green(cls, text): return f"{cls.GREEN}{text}{cls.END}"
    @classmethod
    def red(cls, text): return f"{cls.RED}{text}{cls.END}"
    @classmethod
    def yellow(cls, text): return f"{cls.YELLOW}{text}{cls.END}"
    @classmethod
    def blue(cls, text): return f"{cls.BLUE}{text}{cls.END}"