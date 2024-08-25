"""Main module."""
import ipyleaflet
from ipyleaflet import basemaps
class Map(ipyleaflet.Map):

    def __init__(self,center= [27.48,77.3],zoom = 12, **kwargs):
        super().__init__(center = center, zoom = zoom, **kwargs)
        
    def add_tile_layer(self, url,name,**kwargs):
        layer = ipyleaflet.TileLayer(url = url, name = name, **kwargs)
        self.add(layer)
    def add_basemap(self, name):
        if isinstance(name, str):
            basemap = eval(f"basemaps.{name}").build_url()
            self.add_tile_layer(basemap,name)

            self.add(basemap)
        else:
            self.add(name)
    def add_layers_control(self, position = 'topright'):
        self.add_control(ipyleaflet.LayersControl(position = position))