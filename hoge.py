from pathlib import Path
import pandas as pd


def print_hoge() -> str:
    return 'hoge'


def tashizan(a: int, b: int) -> int:
    return a - b


if __name__ == '__main__':
    hoge = print_hoge()
    c = tashizan(1, 2)

    p = Path('./')
    df = pd.DataFrame(data=None)
