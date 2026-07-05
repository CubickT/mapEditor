class Region:
    def __init__(self, id, name, hex_color, params=None):
        self.id = id
        self.name = name
        self.hex_color = hex_color  # hex-строка
        self.params = params if params is not None else {}

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "color": self.hex_color,
            "params": self.params
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["name"], data["color"], data.get("params", {}))
