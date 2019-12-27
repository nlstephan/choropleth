# Nicole Stephan
# 5222 Final Project 
# Choropleth Map

import sys
sys.path.append('/Users/nicolestephan/Desktop/5222/gisalgs')
from geom.shapex import *
from geom.point import *
import matplotlib.pyplot as plt
import numpy as np

def eq_bins(lower_bound, width, class_num):
    bins = []
    for low in range(int(lower_bound), int(lower_bound) + class_num*width + 1, width):
        bins.append((low, low+width))
    return bins

def qu_bins(data, class_num):
    obs_per_bin = len(data)//class_num
    remainder = len(data)%class_num
    full_bins = []
    for _ in range(class_num):
        if remainder > _:
            full_bins.append(data[_ * (obs_per_bin+1) : (_+1) * (obs_per_bin+1)])
        else:
            diff = _ - remainder
            start = remainder * (obs_per_bin + 1) + diff * obs_per_bin
            end = start + obs_per_bin
            newdata = data[start : end]
            full_bins.append(newdata)
    bins = []
    for b in full_bins:
        bins.append((b[0], b[-1]))
    return bins

def draw_choropleth():
    def add_patch(face_color, class_method, poly):
        for b in class_method:
            if atr in range(b[0], b[1]+1):
                p1 = plt.Polygon(poly, closed=True, fill=True, facecolor=face_color[b], edgecolor='black')
                ax.add_patch(p1)

    fname = input('Enter shapefile path: ')
    shp = shapex(fname)
    prop = input('Enter quantifiable attribute to map: ')
    class_num = int(input('Number of classes (2-9): '))
    class_method = input('Classification method (equal interval or quantile): ')
    colors = [ '#fff7fb', '#ece2f0', '#d0d1e6', '#a6bddb', '#67a9cf', '#3690c0', '#02818a', '#016c59', '#014636' ]
    ax = plt.gca()

    sorted_atr = []
    for f in shp:
        atr = int(f['properties'][prop])
        sorted_atr.append(atr)
    sorted_atr.sort()

    if class_method == 'equal interval':
        classes = class_num - 1
        width = int((sorted_atr[-1]-sorted_atr[0])/classes)
        equalint_bins = eq_bins(sorted_atr[0], width, classes)
        eq_bins_colors = dict(zip(equalint_bins, colors))
    if class_method == 'quantile':
        quantile_bins = qu_bins(sorted_atr, class_num)
        quant_bins_colors = dict(zip(quantile_bins, colors))

    for f in shp:
        atr = int(f['properties'][prop])
        if len(f['geometry']['coordinates']) == 1:
            points = f['geometry']['coordinates'][0]
            poly = [ [p[0], p[1]] for p in points ]
            if class_method == 'equal interval':
                add_patch(eq_bins_colors, equalint_bins, poly)
            if class_method == 'quantile':
                add_patch(quant_bins_colors, quantile_bins, poly)
        if len(f['geometry']['coordinates']) > 1:  # multipolygon
            for c in f['geometry']['coordinates']:
                points = c[0]
                poly = [ [p[0], p[1]] for p in points ]
                if class_method == 'equal interval':
                    add_patch(eq_bins_colors, equalint_bins, poly)
                if class_method == 'quantile':
                    add_patch(quant_bins_colors, quantile_bins, poly)
        
    ax.set_aspect(1)  
    ax.axis('scaled') 
    ax.axis('off')         
    plt.grid()
    plt.show()

draw_choropleth()



