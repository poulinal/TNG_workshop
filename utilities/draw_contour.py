#Bryanne McDonough

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import matplotlib.lines as mlines

def conplot(xdat,ydat,concol, subplots=False, ax=[],alph=0.5, linewidth=0.75):
    """
    Plots a contour plot based on the provided x and y data.

    Parameters:
    xdat (array-like): The x data points.
    ydat (array-like): The y data points.
    concol (str): The color of the contour lines.
    subplots (bool, optional): Whether to plot on subplots. Default is False.
    ax (matplotlib.axes.Axes, optional): The axes to plot on if subplots is True. Default is an empty list.
    alph (float, optional): The alpha blending (transparency) value for the contour lines. Default is 0.5.
    linewidth (float, optional): The width of the contour lines. Default is 0.75.

    Returns:
    None
    """
    binsize=100
    deltaX=(max(xdat)-min(xdat))/binsize
    deltaY=(max(ydat)-min(ydat))/binsize

    xmin=min(xdat)-deltaX
    xmax=max(xdat)+deltaX
    ymin=min(ydat)-deltaY
    ymax=max(ydat)+deltaY

    xx,yy=np.mgrid[xmin:xmax:100j,ymin:ymax:100j]
    positions=np.vstack([xx.ravel(),yy.ravel()])
    values=np.vstack([xdat,ydat])

    kernel=st.gaussian_kde(values)
    Z=np.reshape(kernel(positions).T,xx.shape)
    #print(Z.shape)

    if concol=='blue': linestyle='dashed'
    elif concol=='green': linestyle='dashdot'

    else: linestyle='solid'
        
    #Z=np.reshape(kernel(positions).T,X.shape)
    #delSFR.reshape((len(s_mass),len(SFR)))
    if not subplots: plt.contour(xx,yy,Z,colors=concol,linewidths=linewidth,levels=7,alpha=alph) #z should not be delSFR
    else: ax.contour(xx,yy,Z,colors=concol,linewidths=linewidth,levels=7,alpha=1,linestyles=linestyle)
    return()

custom_leg=[mlines.Line2D([0],[0],color='magenta', alpha=0.5),
             mlines.Line2D([0],[0],color='green',alpha=0.5), 
             mlines.Line2D([0],[0], color='red',linestyle='None', marker='x'), 
             mlines.Line2D([0],[0], color='orange',linestyle='None', marker='+')]
labels=['all centrals','all satellites','quenched low-mass centrals', 'quenched low-mass satellites']