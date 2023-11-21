import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


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

        # Find relevant elements containing movie data

        movie_titles = [a.get_text(strip=True)
                        for a in soup.select('.ipc-title__text')]
        movie_ratings = [span.get_text(strip=True)
                         for span in soup.select('.ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating')]
        # movie_ratings = [float(span.get_text(strip=True))
        #                  for span in soup.select('.ipc-rating-star--imdb-rating')]

        # for movie_title in movie_titles:
        #     print(movie_title)

        # for movie_rating in movie_ratings:
        #
        print(movie_ratings)

        # movie_elements = soup.find_all('h3', class_='ipc-title__text')
        # for movie_element in movie_elements:
        #     movie_title = movie_element.get_text()
        #     print(movie_title)

        # Create a Pandas DataFrame from the scraped data
        # movie_data = pd.DataFrame(
        #     {'Title': movie_titles, 'Rating': movie_ratings})
        movie_data = ""
        return movie_data
    else:
        print(
            f"Failed to retrieve the page. Status code: {response.status_code}")
        return None


# Call the function to scrape data for most popular movies
popular_movies_dataframe = scrape_most_popular_movies()
