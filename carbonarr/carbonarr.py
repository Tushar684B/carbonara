
import json
import ipyleaflet
import geopandas as gpd
from ipyleaflet import basemaps, GeoJSON, LayersControl


class Map(ipyleaflet.Map):
    """A customized map class for displaying geospatial data using ipyleaflet.
    
    Inherits from the ipyleaflet Map class and adds functionalities to load different layers and basemaps.

    Args:
        center (list, optional): Latitude and longitude for the map's center. Defaults to [27.48, 77.3].
        zoom (int, optional): Initial zoom level for the map. Defaults to 12.
        **kwargs: Additional keyword arguments passed to the ipyleaflet Map class.
    """

    def __init__(self, center=[27.48, 77.3], zoom=12, **kwargs):
        """Initializes the map with a given center and zoom level.
        
        Args:
            center (list, optional): Latitude and longitude for the map's center. Defaults to [27.48, 77.3].
            zoom (int, optional): Initial zoom level for the map. Defaults to 12.
            **kwargs: Additional keyword arguments passed to the ipyleaflet Map class.
        """
        super().__init__(center=center, zoom=zoom, **kwargs)
        
    def add_tile_layer(self, url, name, **kwargs):
        """Adds a tile layer to the map.

        Args:
            url (str): The URL template for the tile layer.
            name (str): The name of the tile layer.
            **kwargs: Additional keyword arguments for the TileLayer.
        """
        layer = ipyleaflet.TileLayer(url=url, name=name, **kwargs)
        self.add(layer)

    def add_basemap(self, name):
        """Adds a basemap to the map.

        Args:
            name (str or ipyleaflet.TileLayer): The name of the basemap or a TileLayer object.
        """
        if isinstance(name, str):
            basemap = eval(f"basemaps.{name}").build_url()
            self.add_tile_layer(basemap, name)
        else:
            self.add(name)
    
    def add_layers_control(self, position='topright'):
        """Adds a layers control to the map, allowing users to toggle different layers on and off.

        Args:
            position (str, optional): Position of the layers control on the map. Defaults to 'topright'.
        """
        self.add_control(LayersControl(position=position))

    def add_geojson_layer(self, filepath, name='geojson', **kwargs):

        """Adds a GeoJSON layer to the map from a file.

        Args:
            filepath (str): Path to the GeoJSON file.
            name (str): The name of the GeoJSON layer.
            **kwargs: Additional keyword arguments for the GeoJSON layer.
        """

        
        with open(filepath, 'r') as f:
            data = json.load(f)
        geo_json = GeoJSON(data=data, name=name, **kwargs)
        self.add(geo_json)
       
    
    def add_shapefile_layer(self, filepath, **kwargs):
        """Adds a shapefile layer to the map by converting it to GeoJSON.

        Args:
            filepath (str): Path to the shapefile.
            **kwargs: Additional keyword arguments for the GeoJSON layer.
        """
        # Read the shapefile using geopandas
        gdf = gpd.read_file(filepath)
        
        # Convert the GeoDataFrame to GeoJSON format
        data = json.loads(gdf.to_json())
        
        # Create a GeoJSON layer and add it to the map
        geo_json = GeoJSON(data=data, **kwargs)
        self.add(geo_json)