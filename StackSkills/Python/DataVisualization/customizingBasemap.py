from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill',  # Miller chart type
            llcrnrlat=20,  # lower-left-corner-latitude
            llcrnrlon=-130,  # lower-left-corner-longitude
            urcrnrlat=50,  # upper-right-corner-latitude
            urcrnrlon=-60,  # upper-right-corner-longitude
            resolution='i')

m.drawcoastlines()
m.drawcountries(linewidth=2)
m.drawstates(color='red')
# m.drawcounties(color='green')
# m.etopo()  # Draws topography

# m.fillcontinents(color='g', lake_color='b')
# m.bluemarble()

# 29 north 95 west (Houston, TX)
lat, lon = 29.7604, -95.368
xpt, ypt = m(lon, lat)
# Plot the xpt as longitude and ypt as latitude, with a red marker
m.plot(xpt, ypt, 'r*', markersize=15)

# Boulder, CO
lat, lon = 40.125, -104.237
xpt, ypt = m(lon, lat)
m.plot(xpt, ypt, 'bo')

# Hanover, MA
lat, lon = 42.1162, -70.8477
xpt, ypt = m(lon, lat)
m.plot(xpt, ypt, 'g*')

land_check = m.is_land(xpt, ypt)
print(land_check)

plt.title('Basemap Example with Title')
plt.show()
