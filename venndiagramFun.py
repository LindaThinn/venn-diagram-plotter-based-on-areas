# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 14:16:15 2021

@author: ThiLin
"""

import math as m 
import matplotlib.pyplot as plt
import numpy as np


def calculateRadius(area):
    """
    return
    """
    
    radius = m.sqrt(area/m.pi)
    
    return radius 


def plotVennDiagram(leftCircleArea, rightCircleArea, overlayArea, title = 'Venn diagram'):
    """
    plots venn diagram 
    returns four coordinates with origo in left top corner 
    """
    # Capital letter variables corresponds to capital A area and vice versa 

    A = leftCircleArea 
    a = rightCircleArea 
    overlay_Aa = overlayArea 
    
    
    R = calculateRadius(A)
    r = calculateRadius(a) 

    overlay = (overlay_Aa/a)*r  #ratio based 

    y_max = max(R,r)

    # coordinates based on centre of cirle 
    x_R = R
    y_R = y_max

    x_r = 2*R + r - 2*overlay    # displacement  
    y_r = y_max


    y_limit = (y_max * 2)*1.2  # set grid limits 
    x_limit = 2*R + 2*r 

    plt.figure()    
    plt.axis([-1, x_limit, -1, y_limit])     
    plt.grid(False)                         # set the grid

    ax=plt.gca()                            # get the axis
    ax.set_ylim(ax.get_ylim()[::-1])        # invert the axis
    ax.xaxis.tick_top()                     # move the X-Axis      
    ax.yaxis.tick_left()                    # remove right y-Ticks



    circle_R = plt.Circle(( x_R , y_R ), R , alpha=0.5, color = 'red') 
    circle_r =plt.Circle(( x_r , y_r ), r , alpha=0.5, color = 'green') 


    # coordinates with origo in left top corner 
    left_corner_x_R = x_R - R 
    left_corner_y_R = y_R - R 

    left_corner_x_r = x_r- r 
    left_corner_y_r = y_r - r

    plt.scatter(left_corner_x_R, left_corner_y_R, color= 'black', marker= 'x')
    plt.scatter(left_corner_x_r, left_corner_y_r, color= 'black', marker= 'x')
    

    # calculate coordinates for area values based on geometry 
    x_overlay = 0.5*left_corner_x_r + 0.5*left_corner_x_R + R
    x_r_ticket = 0.5*left_corner_x_R + 0.5*left_corner_x_r + r + R
    x_R_ticket = 0.5*(left_corner_x_R + left_corner_x_r)

    plt.text( x_R_ticket , y_R , s= str(A))  # plot area values 
    plt.text( x_r_ticket , y_r , s= str(a))
    plt.text(x_overlay , y_r, str(overlay_Aa))


    ax.set_aspect( 1 ) 
    ax.add_artist( circle_R ) 
    ax.add_artist( circle_r ) 


    plt.title( title) 
    plt.show()
    
    return (left_corner_x_R, left_corner_y_R, left_corner_x_r, left_corner_y_r)
    

if __name__ == '__main__':



    leftCircleArea = 100  # left circle amount 
    rightCircleArea = 200  # right circle amount 
    overlayArea = 70  #overlay amount 
    title = 'test test '

    plotVennDiagram(leftCircleArea, rightCircleArea, overlayArea, title)
