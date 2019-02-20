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
m.fillcontinents(color='#c1ffc1', lake_color='#002344')

xs = []
ys = []

# 29 north 95 west (Houston, TX)
hlat, hlon = 29.7604, -95.368
xpt, ypt = m(hlon, hlat)
xs.append(xpt)
ys.append(ypt)
# Plot the xpt as longitude and ypt as latitude, with a red marker
m.plot(xpt, ypt, 'r*', markersize=15)

# Hanover, MA
blat, blon = 42.1162, -70.8477
xpt, ypt = m(blon, blat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt, ypt, 'mo')

# Checks to make sure the plotted coordinates are on land
land_check = m.is_land(xpt, ypt)
print(land_check)

# Draw a line from point to point (straight line)
m.plot(xs, ys, linewidth=2, label='Flight 115')

# Draws a slight line/ curve from point to point
m.drawgreatcircle(hlon, hlat, blon, blat, linewidth=2, color='c', label='Great Circle')

plt.legend()
plt.title('Basemap Example with Coordinate Connections')
plt.show()
