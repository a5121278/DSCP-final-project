# import part
from sys import flags
import pip
pip.main(['install', 'pandas'])
pip.main(['install', 'matplotlib'])

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


if __name__ == '__main__':
    dist = "YOUTUBE CHANNELS DATASET.csv"
    def Subscribers_converter(x: str):
        x = x.replace('M', '')
        if x == '':
            return None
        else:
            return float(x)
    df = pd.read_csv( dist, converters={'Subscribers': Subscribers_converter})
    length = len(df.Subscribers)
    # Data Visualization
    plt.plot(df.index, df.Subscribers)
    plt.xlim(length + 1, -1)
    plt.title(" Youtube top 100 channels ")


    ax = plt.gca()
    y_major_locator = MultipleLocator(20)
    ax.yaxis.set_major_locator(y_major_locator)
    plt.ylim(df.Subscribers[ length - 2]-20, df.Subscribers[0])

    plt.xlabel(r" Ranking")
    plt.ylabel(r" Subscribers (in millions)")
    plt.show()
