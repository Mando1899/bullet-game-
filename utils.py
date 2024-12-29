import math

def mag_vector(vector, mag=5):
    hip = math.sqrt(vector[0]**2 + vector[1]**2)
    if vector[0] > 0 and vector[1] > 0: 
        angle = math.sin(vector[0]/hip)
        x = mag * math.sin(angle)
        y = mag**2 - x
    if vector[0] < 0 and vector[1] > 0 :
        angle = math.sin(-vector[0]/hip)
        x = mag * math.sin(angle)
        y = mag**2 - x
        x = -x
    if vector[0] > 0 and vector[1] < 0 :
        angle = math.sin(vector[0]/hip)
        x = mag * math.sin(angle)
        y = mag**2 - x
        y = -y
    if vector[0] < 0 and vector[1] < 0 :
        angle = math.sin(-vector[0]/hip)
        x = mag * math.sin(angle)
        y = mag**2 - x
        y = -y
        x = -x
    return [x, y]

def draw_text(text, font, text_color, x, y, surf):
    img = font.render(text, True, text_color)
    surf.blit(img, [x, y])





