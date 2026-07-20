from models.region import Region

class Palette:
    def __init__(self, regions=None):
        self.regions = regions if regions is not None else []

    def find_by_color(self, hex_color):
        for r in self.regions:
            if r.hex_color.upper() == hex_color.upper():
                return r
        return None
    
    def find_by_id(self, region_id):
        for r in self.regions:
            if r.id.upper() == region_id.upper():
                return r
        return None

    def add_region(self, region):
        self.regions.append(region)

    def to_jsonable(self):
        return [r.to_dict() for r in self.regions]

    @classmethod
    def from_jsonable(cls, data_list):
        return cls([Region.from_dict(item) for item in data_list])
