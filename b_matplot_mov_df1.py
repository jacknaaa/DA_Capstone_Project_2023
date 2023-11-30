import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)


def matplot_mov_df1():
    df = pd.DataFrame(pd.read_csv("data\mov_df1.csv"))
    most_ranking_count = df["Rating"].value_counts()
    plt.figure(figsize=(10, 10))
    plt.pie(most_ranking_count, labels=most_ranking_count.index,
            autopct='%1.1f%%', startangle=90, colors=sns.color_palette("viridis"))
    plt.title('Most Ranking in 2023 Categories')
    plt.show()


matplot_mov_df1()
