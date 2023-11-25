import pytest
from movie_scraper import *


def test_scrape_most_popular_movies_IMDB():
    # Add your test cases here
    result = scrape_most_popular_movies_IMDB()
    assert len(result) > 0, "No data scraped from IMDb"


def test_scrape_most_popular_movies_rotten_tomatoes():
    # Add your test cases here
    result = scrape_most_popular_movies_rotten_tomatoes()
    assert len(result) > 0, "No data scraped from Rotten Tomatoes"


def test_join_two_df_by_SQL():
    # Mock data for testing
    df1 = scrape_most_popular_movies_IMDB()
    df2 = scrape_most_popular_movies_rotten_tomatoes()

    # Add your test cases here
    result = join_two_df_by_SQL(df1, df2)

    # Assuming join should not result in an empty DataFrame
    assert len(result) > 0, "Join result is empty"
