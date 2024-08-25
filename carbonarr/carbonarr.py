import json
import ipyleaflet
import geopandas as gpd
from ipyleaflet import basemaps, GeoJSON

class Map(ipyleaflet.Map):

    def __init__(self, center=[27.48, 77.3], zoom=12, **kwargs):
        super().__init__(center=center, zoom=zoom, **kwargs)
        
    def add_tile_layer(self, url, name, **kwargs):
        layer = ipyleaflet.TileLayer(url=url, name=name, **kwargs)
        self.add(layer)

    def add_basemap(self, name):
        if isinstance(name, str):
            basemap = eval(f"basemaps.{name}").build_url()
            self.add_tile_layer(basemap, name)
        else:
            self.add(name)
    
    def add_layers_control(self, position='topright'):
        self.add_control(ipyleaflet.LayersControl(position=position))

    def add_geojson_layer(self, filepath,name,**kwargs):
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        geo_json = GeoJSON(data=data, name= name,**kwargs)
        self.add(geo_json)
    def add_shapefile_layer(self, filepath, **kwargs):
        # Read the shapefile using geopandas
        gdf = gpd.read_file(filepath)
        
        # Convert the GeoDataFrame to GeoJSON format
        data = json.loads(gdf.to_json())
        
        # Create a GeoJSON layer and add it to the map
        geo_json = GeoJSON(data=data, **kwargs)
        self.add(geo_json)