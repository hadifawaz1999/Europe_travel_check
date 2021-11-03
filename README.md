# Europe_travel_check

This code will output a map of Europe and differentiate between countries the user traveled to and the ones the user didn't. 

The user should adjust the ``` visited_countries ``` list in ``` main.py ``` , the list should be only of country codes of 2 capital letters found [here](https://countrycode.org/).

## Requirements

* [Matplotlib](https://matplotlib.org/)
* [Numpy](https://numpy.org/)
* [GeoPandas](https://geopandas.org/)

## Data

We will be using the [Eurostat dataset](https://ec.europa.eu/eurostat/web/gisco/geodata/reference-data/administrative-units-statistical-units/nuts#nuts21)

## Results

For example if a user only visited France and Italy he should have the list as follows : ``` visited_countries = ['FR','IT'] ``` and we will have this map as results:

![map.png](https://github.com/hadifawaz1999/Europe_travel_check/blob/main/map.png)
