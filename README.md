# geojson
This repo provides geojson files for USA zipcode by states. the project provide the step by step to these geojson files. 
You may need census bureau api key to get additional data from census bureau. Otherwise you can use the census free call api that is provided by [census.gov](https://api.census.gov/)

### create venv environment
* create venv environment
```
python3 -m venv .geojsonvenv
```
* activate venv
```
source .geojsonvenv/bin/activate
```

* install requirements

```
pip install -r requirements.txt
```
* include  the census api key in the .zshrc file

```
export CENSUS_API_KEY="your census api key"
```

* run the jupyternote book


