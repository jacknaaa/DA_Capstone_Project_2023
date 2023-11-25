# DA_Capstone_Project_2023

# Project Setup Guide

\*\*\* Note: This project requires an internet connection.
Follow these steps to set up the project on your local machine:

1. Cloned the repo to your machine, navigate to the project
   folder in GitBash/Terminal.
2. Create a virtual environment in the project folder. `python3 -m venv venv` [^1]
3. Activate the virtual environment. `source venv/Scripts/activate` (Windows OS)
4. Install the required packages. `pip install -r requirements.txt`
5. Run the movie_scraper.py script.
6. bokeh_plot should shows on your defult browser

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

### Virutal Environment Instructions

1. After you have cloned the repo to your machine, navigate to the project
   folder in GitBash/Terminal.
1. Create a virtual environment in the project folder. `python3 -m venv venv` [^1]
1. Activate the virtual environment. `source venv/bin/activate`
1. Install the required packages. `pip install -r requirements.txt`
1. When you are done working on your repo, deactivate the virtual environment.
   `deactivate`

[^1]: GitBash on Windows uses “python” instead of “python3”

# Note

!!!PIP Uninstall All Packages

1. pip freeze > requirements.txt
2. pip uninstall -r requirements.txt This helps to uninstall packages one by one.
3. pip uninstall -r requirements.txt -y This helps to delete all the packages at once.

## Unit Tests

### Writing Unit Tests

We have included three unit tests to ensure the functionality of key functions in this project. You can find these tests in the `tests` folder:

1. **test_scrape_most_popular_movies_IMDB.py**: Tests the `scrape_most_popular_movies_IMDB` function.
2. **test_scrape_most_popular_movies_rotten_tomatoes.py**: Tests the `scrape_most_popular_movies_rotten_tomatoes` function.
3. **test_join_two_df_by_SQL.py**: Tests the `join_two_df_by_SQL` function.

### Running Unit Tests

To run the unit tests, follow these steps:

1. Make sure your virtual environment is activated (if not, refer to the Virtual Environment Instructions in the README).

2. Navigate to the project folder in your terminal.

3. Run the following command to execute the tests:
