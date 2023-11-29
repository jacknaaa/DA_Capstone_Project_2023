import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import pandasql as psql
from config import DB_CONFIG, TEST_MODE
from sqlalchemy import create_engine
from bokeh.plotting import figure, show
from bokeh.models import HoverTool, ColumnDataSource


# Function to scrape data from the most popular movies page on IMDb
def scrape_most_popular_movies_IMDB():
    """
    Scrape data from the most popular movies page on IMDb.

    Returns:
    pandas.DataFrame: DataFrame containing movie titles and ratings.
    """
    # URL of the most popular movies page on IMDb
    url = 'https://www.imdb.com/chart/moviemeter/'

    # Send a GET request to the URL with a user-agent header to mimic a web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    time.sleep(2)  # Sleep for 2 seconds to avoid overloading the server
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # write soup file to .html
        # file1 = open("output_imdb.html", "wb")
        # file1.write(soup.encode('utf-8'))
        # file1.close()

        # Extract movie titles from the HTML using CSS selectors
        movie_titles = [a.get_text(strip=True)
                        for a in soup.select('a.ipc-title-link-wrapper h3.ipc-title__text')]
        # Exclude the last 7 items as they are not movies
        movie_titles = movie_titles[:-7]

        pattern = re.compile(r'\((.*?)\)')
        rating = []
        movie_ratings = [b.get_text(strip=True)
                         for b in soup.select('span.sc-479faa3c-1 div.jlKVfJ')]
        for movie_rating in movie_ratings:
            rating.append(movie_rating[:3])

        # Extract vote counts from the movie ratings using regular expressions
        movie_votecounts = [pattern.search(item).group(1) if pattern.search(
            item) else None for item in movie_ratings]

        # Create a Pandas DataFrame from the scraped data
        movie_data = pd.DataFrame(
            {'Title': movie_titles, 'Rating': rating, 'Vote count': movie_votecounts})

        return movie_data
    else:
        print(
            f"Failed to retrieve the page. Status code: {response.status_code}")
        return None


# Function to scrape data from the most popular movies page on Rotten Tomatoes
def scrape_most_popular_movies_rotten_tomatoes():
    """
    Scrape data from the most popular movies page on rottentomatoes.

    Returns:
    pandas.DataFrame: DataFrame containing movie titles and start_date.
    """
    url = 'https://www.rottentomatoes.com/browse/movies_in_theaters/'

    # Send a GET request to the URL with a user-agent header to mimic a web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    time.sleep(2)  # Sleep for 2 seconds to avoid overloading the server
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # write soup file to .html
        # file1 = open("output_rtt.html", "wb")
        # file1.write(soup.encode('utf-8'))
        # file1.close()

        # Extract movie titles from the HTML using CSS selectors
        movie_titles = [a.get_text(strip=True)
                        for a in soup.select('span[data-qa="discovery-media-list-item-title"]')]

        # print(len(movie_titles))
        mv_start_date = []
        movie_start_dates = [b.get_text(strip=True)
                             for b in soup.select('span[data-qa="discovery-media-list-item-start-date"]')]

        for movie_start_date in movie_start_dates:
            # Extract the first 3 characters as the rating
            mv_start_date.append(movie_start_date[7:])

        # print(mv_start_date)

        # Create a Pandas DataFrame from the scraped data
        movie_data = pd.DataFrame(
            {'Title': movie_titles, 'Start Date': mv_start_date})

        return movie_data
    else:
        print(
            f"Failed to retrieve the page. Status code: {response.status_code}")
        return None


# Function to join two DataFrames based on the 'Title' column using SQL
def join_two_df_by_SQL(df1, df2):

    # Merge the two datasets based on the 'Title' column [using pandas Python to perform join data]
    merged_data = pd.merge(df1, df2, on='Title', how='inner')

    # Display the merged DataFrame
    print("Merged Data:")
    print(merged_data)

    # Perform a SQL join using pandasql
    query = """
        SELECT A.*, B.[Start Date]
        FROM df1 A
        JOIN df2 B
        ON A.Title = B.Title
    """
    result = psql.sqldf(query, locals())
    # Display the result of the SQL join using pandasql
    print("\nResult of SQL Join:")
    # print(result)

    return merged_data


# def df_to_SQL(df):  # Function to insert DataFrame into PostgreSQL database
#     # Extracting database connection details from the configuration
#     dbname = DB_CONFIG['dbname']
#     user = DB_CONFIG['user']
#     password = DB_CONFIG['password']
#     host = DB_CONFIG['host']
#     port = DB_CONFIG['port']

#     # Construct the connection string
#     connection_string = f"dbname={dbname} user={user} password={password} host={host} port={port}"
#     # Establish a connection to the PostgreSQL database
#     try:
#         connection = psycopg2.connect(connection_string)
#         print("Connected to the database!")

#         # Create a SQLAlchemy engine
#         engine = create_engine(
#             f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}")

#         # Insert the DataFrame into the database
#         df.to_sql('st_details', engine, if_exists='replace', index=False)

#         print("Data inserted into PostgreSQL!")

#         # Create a cursor object to execute SQL queries
#         cursor = connection.cursor()

#         # Example: Execute a simple SQL query
#         cursor.execute("SELECT * FROM st_details")
#         rows = cursor.fetchall()

#         print(rows)

#     except Exception as e:
#         print(f"Error: {e}")

#     finally:
#         # Close the cursor and connection
#         if connection:
#             cursor.close()
#             connection.close()
#             print("Connection closed.")


def bokeh_plot(df1):
    # Convert 'Rating' to numeric, handle errors
    df1['Rating'] = pd.to_numeric(df1['Rating'], errors='coerce')
    # Drop rows with missing or invalid ratings
    df1 = df1.dropna(subset=['Rating'])

    # Create a Bokeh scatter plot
    source = ColumnDataSource(df1)

    # Define the plot
    p = figure(title='IMDb Top 100 Movies', y_axis_label='Rating',
               x_axis_label='Title', y_range=df1['Title'][::-1])

    # Add a horizontal bar plot
    p.hbar(y='Title', right='Rating', height=0.9,
           source=source, line_color="white", color="blue")

    # Add hover tool for additional information
    hover = HoverTool()
    hover.tooltips = [('Title', '@Title'), ('Rating', '@Rating')]
    p.add_tools(hover)

    # Show the plot
    show(p)

    return None


##### *******   1.	Loading data.  *******#####
# Call the function to scrape data for most popular movies IMDb
mov_df1 = scrape_most_popular_movies_IMDB()
print("Scrape data for most popular movies IMDb")
print(mov_df1)

# Call the function to scrape data for most popular movies
mov_df2 = scrape_most_popular_movies_rotten_tomatoes()
print("Scrape data for most popular movies Rotten Tomatoes")
print(mov_df2)

##### *******   1.	Loading data.  *******#####

##### *******   2.	Clean and operate on the data while combining them.   *******#####

###########  cleaning data  ###########
# replacing na values in college with No college
# popular_mov_df1['Vote count'].fillna("", inplace=True)
# replacing na values in college with No college
# popular_mov_df['Vote count'].fillna(method='bfill', inplace=True)

# print(popular_mov_df.info())
# print(popular_mov_df.isnull().sum())
# print(popular_mov_df['Vote count'])


merged_data = join_two_df_by_SQL(mov_df1, mov_df2)
print("\nSQL join df1 and df2:")
print(merged_data)

###########  cleaning data  ###########
##### *******   2.	Clean and operate on the data while combining them.   *******#####

##### *******   3.	Visualize / Present your data   *******#####
bokeh_plot(merged_data)
##### *******   3.	Visualize / Present your data   *******#####
