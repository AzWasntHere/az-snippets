#convert rgb to hex or vice-versa

#to_hex((r, g, b))
def to_hex(rgb):
    return '%02x%02x%02x' % rgb

#to_rgb('HEX CODE WITHOUT #')
def to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))
