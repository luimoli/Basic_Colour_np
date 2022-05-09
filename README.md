# SMV-ColourBase
The purpose of this CodeBase is to unify the conversion of different colour spaces. 

Different colour space conversion methods (including RGB, YUV, Ycbcr, XYZ, xyY, L\*a\*b\*, etc.) are included.

Several OOTF/OETF/EOTF en-decoding functions are also included.

## 1. ColorSpaceTrans  
The colourspaces incorporated in this codebase are listed as below:
```
RGB:
HSV:
YUV:
XYZ:
xyY:
L*a*b*:
L*u*v*:
LCHab:
LCHuv:
```
| Conversion | interface pre-func | interface post-func |
| --------| :-------: | :-------: |
| RGB<->HSV  | RGB2HSV        | HSV2RGB        |
| RGB<->Ycbcr | RGB2Ycbcr | Ycbcr2RGB |
| RGB<->YUV | RGB2YUV | YUV2RGB |
| XYZ<->xyY | XYZ2xyY | xyY2XYZ |
| XYZ<->Lab | XYZ2Lab | Lab2XYZ |
| XYZ<->Luv | XYZ2Luv | Luv2XYZ |
| Lab<->LCHab | Lab2LCHab | LCHab2Lab |
| Luv<->LCHuv | Luv2LCHuv | LCHuv2Luv |
| xy<->xyY | xy2xyY | —— |
| uv<->xy| uv2xy | xy2uv |
| xy<->CCT | xy2CCT | —— |
| OOTF | ——  | —— |
| OETF | ——  | —— |
| EOTF | ——  | —— |

Our functions has been compared and verified with ```OpenCV``` or ```colour-sicence```.  



## 2. Examples
When using this package, all the image inputs should be normalized to [0, 1].

Most of the objects are available from the smv_colour namespace:
```
>>> import smv_colour
```

```
# Conversion from CIE XYZ space to CIE xyY colourspace.
>>> img_xyz
>>> img_xyy = smv_colour.XYZ2xyY(img_xyz)
```

## 3.Illuminants
```
const.ILLUMINANTS = {'D50': [ 0.3457,  0.3585], 
                    'D55': [ 0.33243, 0.34744], 
                    'D60': [0.32162624, 0.337737], 
                    'D65': [ 0.3127,  0.329]}
```

## Future Work
1. Establishing automatic colour conversion graph could make easier colour conversions.(e.g.,RGB->L\*a\*b\*: RGB->XYZ->L\*a\*b\*)
