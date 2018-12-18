from glob import glob

import matplotlib.pyplot as plt
import pandas as pd


def plot_graph(category):

    dateparse = lambda dates: pd.datetime.strptime(dates, '%d-%m-%y %H:%M')

    df = pd.read_csv('meme_metadata.csv', parse_dates=['date'], date_parser=dateparse,
                     skipinitialspace=True, usecols=['type', 'date', 'upvotes'])

    df_type = lambda row_type: df[~(df[['type']] != row_type).any(axis=1)]

    df = df_type(category)
    # df = df_drop('Blacman Feels')
    # df = df_drop('World')
    # df = df_drop('Web is Crazy')
    # df = df_drop('Versus')
    # df = df_drop('Twitter FB Forums')
    # df = df_drop('Stock')
    # df = df_drop('Texts')
    # df = df_drop('Texts')
    # df = df_drop('Texts')
    # df = df_drop('Texts')

    print(df.count())
    print(df)

    x = df['date']
    y = df['upvotes']

    plt.plot(x, y, marker='o', color='cyan')

    plt.tick_params(axis='x', which='major', labelsize=6)

    plt.xlabel(f'Date\n\n{categories}')
    plt.ylabel('Upvotes')
    plt.grid(b=True, which='major', color='b', linestyle='-')
    plt.grid(b=True, which='minor',  color='r', linestyle='--')
    plt.legend()

    # fig = plt.figure()
    # fig.suptitle(category)

    # axes = plt.axis()
    # plt.plot([x[-2], x[-2]+1000*(x[-1]-x[-2])], [y[-2], y[-2]+1000*(y[-1]-y[-2])])
    # plt.xlim([axes[0], axes[1]])
    # plt.ylim([axes[2], axes[3]])

    plt.show()

    # plt.figure()
    # l_h = []
    # for identifier in df[0].unique():
    #     h, = plt.plot(df[df[0] == identifier]['date'], df[df[0] == identifier][3], label=identifier)
    #     l_h.append(h)
    # plt.legend(handles=l_h)
    # plt.show()


memes_types = glob("../memes/[!*ini, !*jpg]*")

meme_categories = [fp.split('\\')[1] for fp in memes_types]
print(meme_categories)

for categories in meme_categories:
    plot_graph(categories)
