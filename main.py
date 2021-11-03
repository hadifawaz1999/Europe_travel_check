import matplotlib.pyplot as plt
import geopandas as gpd
import numpy as np
import random

# list the visited countries (by country code 2 capital letters only) in the list

visited_countries = ['IT','FR']

# the path for each json file
rg_path = './data/NUTS_RG_01M_2021_3035_LEVL_0.json'
bn_path = './data/NUTS_BN_01M_2021_3035_LEVL_0.json'
lb_path = './data/NUTS_LB_2021_3035_LEVL_0.json'

# load the three geo pandas data frames

gdf_rg = gpd.read_file(rg_path)

gdf_bn = gpd.read_file(bn_path)

gdf_lb = gpd.read_file(lb_path)


# extract the country names from the labels geo data frame

country_names = np.asarray(gdf_lb['NAME_LATN'])

# extract the country coordinated x and y from the labels geo data frame (geometry shapely)

country_x_y = np.asarray(gdf_lb['geometry'])

country_x = np.asarray([country_x_y[i].x for i in range(len(country_x_y))])
country_y = np.asarray([country_x_y[i].y for i in range(len(country_x_y))])


# create the figure

fig, ax = plt.subplots(figsize=(30,25))

# plot on the same axis the regions (country areas) in gray and the boundaries in red

gdf_rg.plot(axes=ax,color='gray')
gdf_bn.plot(axes=ax,color='black')

# search the row in gdf_rg (countries regions) for each visited country

for i in range(len(visited_countries)):

    visited_country = gdf_rg[gdf_rg['CNTR_CODE'].str.contains(visited_countries[i])]
    
    # plot the visited country region in red

    visited_country.plot(axes=ax,color='red')

# generation of random colors for each countary

number_of_colors = len(country_names)

color_array = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]

# iterate for each country and scatter the point labeled (with the country name)
# with the corresponding color

for i in range(len(country_names)):

    check_label = ''

    # check if country has been visited

    if str(gdf_lb.iloc[[i]]['CNTR_CODE'].values[0]) in visited_countries:
        print("test")

        # add a check label

        check_label = u'\N{check mark}'


    ax.scatter(country_x[i],country_y[i],lw=10,color=color_array[i],label=country_names[i]+check_label)


# Plot everything

plt.legend(fontsize=20)
plt.savefig('map.png')