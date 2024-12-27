# import part
from sys import flags
import pip
pip.main(['install', 'pandas'])
pip.main(['install', 'matplotlib'])

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


if __name__ == '__main__':
    dist = "YOUTUBE CHANNELS DATASET.csv"
    Subscribers_converter = lambda x: (x.replace('M', ''))
    df = pd.read_csv( dist, converters={'Subscribers': Subscribers_converter})
    for ele in df.Subscribers:
        if ele == '':
            ele = 0.0
        ele = float(ele)
    length = len(df.Subscribers)
    index = range(length)
    # Data Visualization
    plt.plot(index, df.Subscribers)
    plt.xlim(0, length)
    plt.title(" Youtube top 500 channels ")

    y_major_locator = MultipleLocator(10)
    ax = plt.gca()
    ax.yaxis.set_major_locator(y_major_locator)

    plt.xlabel(r" Ranking")
    plt.ylabel(r" Subscribers ")
    plt.show()
