# DA_Capstone_Project_2023

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
