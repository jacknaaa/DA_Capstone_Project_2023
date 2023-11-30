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

## Features:

1. Web Scraping:
   Scrapes data from the most popular movies pages on IMDb and Rotten Tomatoes.
   Extracts information such as movie titles, ratings, vote counts, and start dates
2. Data Cleaning and Processing:
   Cleans the scraped data, removes duplicates, and performs some data operations.
   Joins the data from IMDb and Rotten Tomatoes based on movie titles using both pandas and pandasql.
3. Data Visualization:
   Utilizes Bokeh to create a horizontal bar plot showcasing IMDb's most popular movies on Rotten Tomatoes.
   Generates a pie chart using Matplotlib and Seaborn to visualize the distribution of movie ratings.
4. Output:
   Saves the scraped data and the joined dataset to CSV files.
   Creates HTML files containing the raw HTML content of the scraped pages for future reference.
5. Structure:
   The script is structured into functions, making it modular and easy to understand.
   Each major step (scraping, cleaning, visualization) is encapsulated within its own function.
6. Documentation:
   Includes comments to explain specific sections of the code.
   Prints relevant information, such as the scraped data and the result of the SQL join.
7. Assumptions:
   Assumes the existence of a config module with specified path variables.
   Assumes the availability of HTML and CSV directories.
   # In summary, the script automates the retrieval, cleaning, and visualization of data related to popular movies from IMDb and Rotten Tomatoes, providing insights into ratings and release dates. The final output includes both visualizations and structured datasets for further analysis.

## Sources:

URL of the most popular movies page on IMDb
'https://www.imdb.com/chart/moviemeter/'
Rotten Tomatoes Movies in Theaters (2023)
'https://www.rottentomatoes.com/browse/movies_in_theaters/?page=4'

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
