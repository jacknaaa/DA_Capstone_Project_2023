from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap, linear_cmap
from bokeh.palettes import Viridis
from bokeh.io import output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColorBar
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)


def matplot_mov_df2():
    df = pd.DataFrame(pd.read_csv("data\mov_df2.csv"))
    # Convert 'Start_Date' column to datetime
    df['Start_Date'] = pd.to_datetime(df['Start_Date'], format='%b %d, %Y')
    # Count the occurrences of each start date
    date_counts = df['Start_Date'].value_counts().sort_index()
    # Plotting with seaborn
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=date_counts.index, y=date_counts.values, palette="viridis")
    plt.title("Event Counts by Start Date")
    plt.xlabel("Start Date")
    plt.ylabel("Event Count")
    plt.xticks(rotation=45)
    plt.show()


def bokehplot_mov_df2():
    df = pd.DataFrame(pd.read_csv("data\mov_df2.csv"))
    # Convert 'Start_Date' column to datetime
    df['Start_Date'] = pd.to_datetime(df['Start_Date'], format='%b %d, %Y')

    # Count the occurrences of each start date
    date_counts = df['Start_Date'].value_counts().sort_index()

    # Create a Bokeh ColumnDataSource
    source = ColumnDataSource(
        data=dict(start_date=date_counts.index, event_count=date_counts.values))

    # Set up the figure with linear_cmap
    output_notebook()
    color_mapper = linear_cmap(field_name='start_date', palette=Viridis[6], low=min(
        date_counts.index), high=max(date_counts.index))
    p = figure(x_axis_type="datetime", sizing_mode="stretch_width",
               title="Event Counts by Start Date")

    p.vbar(x='start_date', top='event_count', width=0.9,
           source=source, line_color="white", color=color_mapper)

    # Customize plot aesthetics
    p.xaxis.axis_label = "Start Date"
    p.yaxis.axis_label = "Event Count"
    p.xaxis.major_label_orientation = 45

    # Add color bar
    color_bar = ColorBar(
        color_mapper=color_mapper['transform'], width=8, location=(0, 0))
    p.add_layout(color_bar, 'right')

    # Show the plot
    show(p)


matplot_mov_df2()
# bokehplot_mov_df2()
