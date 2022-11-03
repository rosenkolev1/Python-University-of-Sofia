class RGB:

    def __init__(self, r, g, b):
        """Initialize the RGB class with the given values for red, green and blue.
        Each value should be an integer between 0 and 255.
        """

        if r < 0 or r > 255:
            raise ValueError('Invalid red value')
        if g < 0 or g > 255:
            raise ValueError('Invalid green value')
        if b < 0 or b > 255:
            raise ValueError('Invalid blue value')

        self._r = r
        self._g = g
        self._b = b

    @property
    def r(self):
        return self._r

    @property
    def g(self):
        return self._g

    @property
    def b(self):
        return self._b

    def to_hex(self):
        return f'#{self.r:02X}{self.g:02X}{self.b:02X}'
    
    @classmethod
    def from_hex(cls, hex):
        r = int(hex[1:3], base=16)
        g = int(hex[3:5], base=16)
        b = int(hex[5:7], base=16)

        return cls(r, g, b)
        
    def __repr__(self):
        return f'RGB({self.r}, {self.g}, {self.b})'

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b

    def __hash__(self):
        return hash((self.r, self.g, self.b))

    def rgb_pallette_to_hex_str(palette):
        return [rgb_el.to_hex() for rgb_el in palette]

    def hex_str_pallete_to_rgb(hex_str):
        return [RGB.from_hex(hex_str_el) for hex_str_el in hex_str]


PALLETTE = {
    RGB(255, 255, 255): 'white',
    RGB(0, 0, 0): 'black',
    RGB(255, 0, 0): 'red',
    RGB(0, 255, 0): 'green',
    RGB(0, 0, 255): 'blue',
    RGB(69, 69, 69): "the 51st shade of grey",
}

def extract_only_named_colors(hex_colors):
    # 1. Convert hex to RGB objects
    # 2. Check if each RGB object is in Pallette
    # 3. Return the names those who are in Pallette

    rgb_objects = RGB.hex_str_pallete_to_rgb(hex_colors)
    filtered_objects = [rgb_object for rgb_object in rgb_objects if rgb_object in PALLETTE]
    names_of_filtered_objects = [PALLETTE[filtered_object] for filtered_object in filtered_objects]

    return names_of_filtered_objects

print(RGB.hex_str_pallete_to_rgb(["#000000", "#0A0B0C"]))
print(RGB.rgb_pallette_to_hex_str([RGB(10, 11, 12), RGB(255, 255, 255)]))
print(extract_only_named_colors(["#696969", "#00FF00", "#AAAAAA"]))
