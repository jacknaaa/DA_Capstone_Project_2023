import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re


def scrape_most_popular_movies():
    """
    Scrape data from the most popular movies page on IMDb.

    Returns:
    pandas.DataFrame: DataFrame containing movie titles and ratings.
    """
    # URL of the most popular movies page on IMDb
    url = 'https://www.imdb.com/chart/moviemeter/'

    # Send a GET request to the URL
    # If you not set headers user-agent the web site will know and send 403
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    time.sleep(2)
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        # with open("output1.html", "w", encoding='utf-8') as file:
        #     file.write(str(soup))

        movie_titles = [a.get_text(strip=True)
                        for a in soup.select('a.ipc-title-link-wrapper h3.ipc-title__text')]
        movie_titles = movie_titles[:-7]
        # print(len(movie_titles))

        pattern = re.compile(r'\((.*?)\)')
        rating = []
        movie_ratings = [b.get_text(strip=True)
                         for b in soup.select('span.sc-479faa3c-1 div.jlKVfJ')]
        for movie_rating in movie_ratings:
            rating.append(movie_rating[:3])
        # print(len(rating))

        movie_votecounts = [pattern.search(item).group(1) if pattern.search(
            item) else None for item in movie_ratings]
        # print(len(movie_votecounts))

        # Create a Pandas DataFrame from the scraped data
        movie_data = pd.DataFrame(
            {'Title': movie_titles, 'Rating': rating, 'Vote count': movie_votecounts})

        return movie_data
    else:
        print(
            f"Failed to retrieve the page. Status code: {response.status_code}")
        return None


# Call the function to scrape data for most popular movies
popular_movies_dataframe = scrape_most_popular_movies()

print(popular_movies_dataframe.head())
