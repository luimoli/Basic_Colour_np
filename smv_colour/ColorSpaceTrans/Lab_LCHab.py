import numpy as np
import numpy as np
import colour

from .utils.func import split, stack

def lab2lch(Lab):
    """[Converts from *CIE Lab* colourspace to *CIE LCH* colourspace.]
    Args:
        Lab ([type]): [description]
    Returns:
        [type]: [description]
    """
    L, a, b = split(Lab)

    H = 180 * np.atan2(b, a) / (np.acos(np.zeros(1)).item() * 2)
    H[H < 0] += 360
    C = np.sqrt(a ** 2 + b ** 2)

    LCH = stack((L, C, H))

    return LCH

def lch2lab(LCH):
    """[Converts from *CIE LCH* colourspace to *CIE Lab* colourspace.]
    Args:
        LCHab ([type]): [description]
    Returns:
        [type]: [description]
    """
    L, C, H = split(LCH)

    a_lab = C * np.cos(np.deg2rad(H))
    b_lab = C * np.sin(np.deg2rad(H))

    Lab = stack((L, a_lab, b_lab))

    return Lab

if __name__ == '__main__':
    randxyz = np.rand((1080,1920,3), dtype=np.float32)
    randlab = colour.XYZ_to_Lab(randxyz)
    randlab = np.from_numpy(randlab)

    # # verify Lab_to_LCH----
    # cs = colour.Lab_to_LCHab(randlab)
    # cs = np.from_numpy(cs)
    # our = Lab_to_LCH(randlab)
    # diff = cs - our
    # print(diff.max(), diff.mean())

    # # # verify LCH_to_Lab----
    # randlch = colour.Lab_to_LCHab(randlab)
    # randlch = np.from_numpy(randlch)
    # cs = colour.LCHab_to_Lab(randlch)
    # cs = np.from_numpy(cs)
    # our = lch2lab(randlch)
    # diff = abs(cs - our)
    # print(diff.max(), diff.mean())

