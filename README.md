# Draw Choropleth

Python program that draws a choropleth map based on user inputs. These inputs include a shapefile path, the quantifiable attribute of the shapefile to map, the number of data classes (2-9), and the desired data classification method (equal interval or quantile).
Currently, this program can only support either equal interval or quantile classification. 

This program was created for a class project and utilizes source code from my professor and matplotlib to display the map.

# To Execute

install matplotlib

run draw_choropleth()

Respond to these inputs in termainal:

>>> Shapefile path: 'path/to/.shp file'
>>> Quantifiable attribute to map: name of attribute
>>> Number of classes (2-9): number in range 2-9
>>> Classification method (equal interval or quantile): quantile or equal interval, depending on desired visualization

The map will pop up in separate matplotlib window.

