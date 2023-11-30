# IMDb and RottenTomatoes ranking movies

# Overview

Welcome to the Data Analysis Capstone Project for 2023! This project focuses on web scraping data from IMDb and Rotten Tomatoes, utilizing Bokeh for interactive data visualization on a web-based platform.

## Instructions:

\*\*\* Note: This project requires an internet connection.

1. Cloned the project to your machine.
2. Create and activate a virtual environment and install the packages listed in the requirements.txt file. (instructions for virtual environment below)

   2.1 Create virtual environment on Windows by entering

- Windows (GitBash): `python -m venv venv`
- Linux/Mac (Terminal): `python3 -m venv venv

  2.2 Activate venv by entering:

- Windows (GitBash): `sourve venv/Scripts/activate`
- Linux/Mac (Terminal): `source venv/bin/activate`

  2.3 Run requirements.txt to install needed libraries:

- Windows (GitBash): `pip install -r requirements.txt`
- Linux/Mac (Terminal): `pip install -r requirements.txt`

  2.4 When done in venv, deactivate by entering:

- Windows (GitBash): `deactivate`
- Linux/Mac (Terminal): `deactivate`

3. Run the `movie_scraper.py` script.
4. Open your defult browser to see data visualization.

## Running Unit Tests:

We have included three unit tests to ensure the functionality of key functions in this project.
To run the unit tests, follow these steps:

1. Make sure your virtual environment is activated (if not, refer to the Virtual Environment Instructions in the README).

2. Navigate to the project folder in your terminal.

3. Run the following command to execute the tests: `pytest test.py`

## Data Dictionary

### scrape_most_popular_movies_IMDB Function Output (mov_df1)

- **Title:** Movie title.
- **Rating:** Movie rating on IMDb.
- **Vote count:** Number of votes for the movie on IMDb.

### scrape_most_popular_movies_rotten_tomatoes Function Output (mov_df2)

- **Title:** Movie title.
- **Start Date:** Release start date of the movie on Rotten Tomatoes.

### join_two_df_by_SQL Function Output (merged_data)

- **Title:** Movie title.
- **Rating:** Movie rating on IMDb.
- **Vote count:** Number of votes for the movie on IMDb.
- **Start Date:** Release start date of the movie on Rotten Tomatoes.

### bokeh_plot Function Input (df1)

- **Title:** Movie title.
- **Rating:** Movie rating on IMDb.
