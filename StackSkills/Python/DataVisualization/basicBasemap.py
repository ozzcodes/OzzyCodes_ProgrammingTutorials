from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill',  # Miller chart type
            llcrnrlat=-90,  # lower-left-corner-latitude
            llcrnrlon=-180,  # lower-left-corner-longitude
            urcrnrlat=90,  # upper-right-corner-latitude
            urcrnrlon=180,  # upper-right-corner-longitude
            resolution='l')
'''
Charts resolution:
 'c' is crude
 'l' is low
 'i' is intermediate
 'h' is high definition
 'f' is full resolution
'''

m.drawcoastlines()
m.fillcontinents()
m.drawmapboundary()

plt.title('Basemap Example with Title')
plt.show()
