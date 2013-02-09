Point Adjustment

(c) Copyright 2013 Allar Haav
licensed under the terms of GNU GPL v3

This is a tool for making spatial adjustment, namely similarity transformation, to a point vector layer. It does, however, not alter the scale and therefore performs only the translation and rotation operations maintaining the original dimensions. Useful for total station point data in arbitrary coordinate system when there are a few points with known "real-life" coordinates.

The plugin functions as follows:
* A vector point layer is selected with edit mode enabled
* Point A is chosen and its feature ID entered. The coordinates entered in the X and Y fields will specify the new location of the point. It is important to keep in mind that point A will be used as the pivot point for rotation.
* The corresponding fields are filled for point B. This point will be used to obtain the correct angle for rotation. The deviation from the expected location for point B will be indicated in a dialog box, but will only affect the rotation for the layer, not its shape nor location.


If you have any comments or suggestions, feel free to mail me: allar.haav@gmail.com