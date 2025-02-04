#import matplotlib as plt
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt



def plot_gen(isoCen_mass, isoCen_bfld, nonIsoCen_mass, nonIsoCen_bfld, preInf_mass, preInf_bfld, postInf_mass, postInf_bfld, filename):
    #plot isolated centrals
    plt.scatter(isoCen_mass, isoCen_bfld, color='blue', label='Isolated Central Galaxies', marker='.')

    #plot non-isolated centrals
    plt.scatter(nonIsoCen_mass, nonIsoCen_bfld, color='red', label='Non-Isolated Central Galaxies', marker='.')

    #plot pre-infall satellites
    plt.scatter(preInf_mass, preInf_bfld, color='green', label='Pre-Infall Satellites', marker='*')

    #plot post-infall satellites
    plt.scatter(postInf_mass, postInf_bfld, color='purple', label='Post-Infall Satellites', marker='2')

    plt.xscale('log')
    plt.yscale('log')

    # Add labels and title
    plt.xlabel('Mass')
    plt.ylabel('B-field')
    #plt.title('Scatter Plot of Two Groups')

    # Add a legend
    plt.legend()


    #save plot
    dir = 'images/' + filename
    plt.savefig(dir, bbox_inches='tight')


    # Show the plot
    plt.show()


def plot_wcontour(isoCen_mass, isoCen_bfld, 
                  nonIsoCen_mass, nonIsoCen_bfld, 
                  preInf_mass, preInf_bfld, 
                  postInf_mass, postInf_bfld, 
                  isoCen_mass_er, isoCen_bfld_er, 
                  nonIsoCen_mass_er, nonIsoCen_bfld_er, 
                  preInf_mass_er, preInf_bfld_er, 
                  postInf_mass_er, postInf_bfld_er, 
                  filename):
    xdat = preInf_mass
    ydat = preInf_bfld
    concol = 'green'
    linewidth = 0.75
    alph = 0.5
    
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
    
    
    #contour
    plt.contour(xx,yy,Z,colors=concol,linewidths=linewidth,levels=7,alpha=alph)
    

    #plot non-isolated centrals
    plt.errorbar(nonIsoCen_mass, nonIsoCen_bfld, xerr=nonIsoCen_mass_er, yerr=nonIsoCen_bfld_er, fmt='.', color='red', label='Non-Isolated Central Galaxies', elinewidth = 0.2)
    #plt.scatter(nonIsoCen_mass, nonIsoCen_bfld, color='red', label='Non-Isolated Central Galaxies', marker='.')
    
    #plot isolated centrals include error
    plt.errorbar(isoCen_mass, isoCen_bfld, xerr=isoCen_mass_er, yerr=isoCen_bfld_er, fmt='.', color='blue', label='Isolated Central Galaxies', elinewidth = 0.2)
    #plt.scatter(isoCen_mass, isoCen_bfld, color='blue', label='Isolated Central Galaxies', marker='.')

    #plot pre-infall satellites
    plt.errorbar(preInf_mass, preInf_bfld, xerr=preInf_mass_er, yerr=preInf_bfld_er, fmt='*', color='green', label='Pre-Infall Satellites', elinewidth = 0.2)
    #plt.scatter(preInf_mass, preInf_bfld, color='green', label='Pre-Infall Satellites', marker='*')

    #plot post-infall satellites
    plt.errorbar(postInf_mass, postInf_bfld, xerr=postInf_mass_er, yerr=postInf_bfld_er, fmt='2', color='purple', label='Post-Infall Satellites', elinewidth = 0.2)
    #plt.scatter(postInf_mass, postInf_bfld, color='purple', label='Post-Infall Satellites', marker='2')
    

    plt.xscale('log')
    plt.yscale('log')

    # Add labels and title
    plt.xlabel('Mass $M_* (M_\odot)$')
    plt.ylabel('Magnetic Field Strength (Gauss)')
    #plt.title('Scatter Plot of Two Groups')

    # Add a legend
    #plt.legend()
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)


    #save plot
    dir = 'images/' + filename
    plt.savefig(dir, bbox_inches='tight')


    # Show the plot
    plt.show()