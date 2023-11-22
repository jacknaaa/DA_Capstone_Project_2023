import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import pandasql as psql
from config import DB_CONFIG
import psycopg2
from sqlalchemy import create_engine


def scrape_most_popular_movies():
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

        # Extract movie titles from the HTML using CSS selectors
        movie_titles = [a.get_text(strip=True)
                        for a in soup.select('a.ipc-title-link-wrapper h3.ipc-title__text')]
        # Exclude the last 7 items as they are not movies
        movie_titles = movie_titles[:-7]

        # Extract movie ratings using CSS selectors and regular expressions
        # Regular expression to extract text inside parentheses
        pattern = re.compile(r'\((.*?)\)')
        rating = []
        movie_ratings = [b.get_text(strip=True)
                         for b in soup.select('span.sc-479faa3c-1 div.jlKVfJ')]
        for movie_rating in movie_ratings:
            # Extract the first 3 characters as the rating
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

# data cleaning and a SQL join. We'll create a second dataset with additional movie information and then perform a join using the pandasql library.


def join_two_df_by_SQL(df1, df2):

    print(df1)


def df_to_SQL(df):
    # Extracting database connection details from the configuration
    dbname = DB_CONFIG['dbname']
    user = DB_CONFIG['user']
    password = DB_CONFIG['password']
    host = DB_CONFIG['host']
    port = DB_CONFIG['port']

    # Construct the connection string
    connection_string = f"dbname={dbname} user={user} password={password} host={host} port={port}"
    # Establish a connection to the PostgreSQL database
    try:
        connection = psycopg2.connect(connection_string)
        print("Connected to the database!")

        # Create a SQLAlchemy engine
        engine = create_engine(
            f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}")

        # Insert the DataFrame into the database
        df.to_sql('st_details', engine, if_exists='replace', index=False)

        print("Data inserted into PostgreSQL!")

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Example: Execute a simple SQL query
        cursor.execute("SELECT * FROM st_details")
        rows = cursor.fetchall()

        print(rows)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if connection:
            cursor.close()
            connection.close()
            print("Connection closed.")


# Call the function to scrape data for most popular movies
popular_mov_df = scrape_most_popular_movies()

###########  cleaning data  ###########
# replacing na values in college with No college
popular_mov_df['Vote count'].fillna("", inplace=True)
# replacing na values in college with No college
# popular_mov_df['Vote count'].fillna(method='bfill', inplace=True)

# print(popular_mov_df.info())
# print(popular_mov_df.isnull().sum())
# print(popular_mov_df['Vote count'])
###########  cleaning data  ###########

########## DataFram to SQL ##########
df_to_SQL(popular_mov_df)
########## DataFram to SQL ##########

# Create a second dataset with additional movie information
additional_movie_data = pd.DataFrame({
    'Title': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump'],
    'Genre': ['Drama', 'Crime', 'Action', 'Crime', 'Drama'],
    'Year': [1994, 1972, 2008, 1994, 1994]
})
