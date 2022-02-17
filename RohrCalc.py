import math

"""""
    # Ausrechnen aus den vorher gegebenen Parametern
    gewicht = math.pi * ((r1 * r1) * (r2 * r2)) * dichte
"""""


def RohrVolumen(dicke, radius):
    r1 = float(radius)
    d = float(dicke)/1000
    r2 = r1 - d
    #print(f"Radius2: {r2}")
    vol1 = math.pi * (r1 * r1)
    #print(f"DEBUG Volumen 1 {vol1}")
    vol2 = math.pi * (r2 * r2)
    #print(f"DEBUG Volumen 2 {vol2}")
    volges = vol1 - vol2

    vol = round(volges, 5)

    return vol

def RohrGewicht(volumen, density):
    weight = float(volumen) * float(density)
    return weight
