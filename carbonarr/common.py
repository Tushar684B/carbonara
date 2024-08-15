"""The common module contains common functions and classes used by the other modules.
"""

def hello_world():
    """Prints "Hello World!" to the console.
    """
    print("Hello World!")

import geopandas as gpd
import matplotlib.pyplot as plt

def shapefile(shapefile_path):
    # Load the shapefile
    gdf = gpd.read_file(shapefile_path)
    
    # Plot the shapefile and zoom to its extent
    ax = gdf.plot(figsize=(10, 10), edgecolor='k')
    
    # Set the x and y limits to the bounds of the shapefile
    xmin, ymin, xmax, ymax = gdf.total_bounds
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    
    # Add title and display plot
    plt.title("Zoomed Shapefile")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()

# Example usage:
# shapefile("path_to_your_shapefile.shp")
