"""Main module."""
import ipyleaflet
class Map(ipyleaflet.Map):

    def __init__(self,center= [27.48,77.3],zoom = 12, **kwargs):
        super().__init__(center = center, zoom = zoom, **kwargs)
        self.add_control(ipyleaflet.LayersControl())
        # self.add_LayerControl()