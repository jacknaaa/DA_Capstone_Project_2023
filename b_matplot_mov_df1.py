import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from config import CSV_PATH


def matplot_mov_df1():
    csv_file = os.path.normpath(CSV_PATH+"mov_df1.csv")
    df = pd.DataFrame(pd.read_csv(csv_file))
    most_ranking_count = df["Rating"].value_counts()
    plt.figure(figsize=(10, 10))
    plt.pie(most_ranking_count, labels=most_ranking_count.index,
            autopct='%1.1f%%', startangle=90, colors=sns.color_palette("viridis"))
    plt.title('Most Ranking in 2023 Categories')
    plt.show(block=False)


def matplot_mov_df2():
    csv_file2 = os.path.normpath(CSV_PATH+"mov_df2.csv")
    df = pd.DataFrame(pd.read_csv(csv_file2))
    df['Start_Date'] = pd.to_datetime(df['Start_Date'], format='%b %d, %Y')
    date_counts = df['Start_Date'].value_counts().sort_index()
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=date_counts.index, y=date_counts.values, palette="viridis")
    plt.title("Event Counts by Start Date")
    plt.xlabel("Start Date")
    plt.ylabel("Event Count")
    plt.xticks(rotation=45)
    plt.show()


# Display both plots simultaneously
matplot_mov_df1()
matplot_mov_df2()
