import os

key = os.environ.get('CENSUS_API_KEY')


if key:
    CENSUS_API_KEY = key
else:
    print("Key not found in .zshrc")