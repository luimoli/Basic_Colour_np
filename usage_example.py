import numpy as np
import smv_colour

if __name__ == '__main__':
    img = np.random.random((1080, 1920, 3)) # randomly initilize a img in domain[0,1].
    res = smv_colour.RGB2XYZ(img, color_space='bt709') # make a conversion from RGB space to CIE-XYZ space.
    print(res.shape)