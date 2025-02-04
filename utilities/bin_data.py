import numpy as np

#given some array, find the average of the array
def avg(array):
    return np.sum(np.nan_to_num(array, nan=0))/len(array)

#print(all(pre_infall_mass[i] <= pre_infall_mass[i + 1] for i in range(len(pre_infall_mass) - 1)))
##prints true if already sorted

def bin_data(data, bin_size):
    binned_data = []
    st_error = []
    for i in range(0, len(data), bin_size):
        binned_data.append(avg(data[i:i+bin_size]))
        st_error.append(np.std(data[i:i+bin_size]))
    return binned_data, st_error

#given mass array and bfld array, sort by mass but change bfld based on sorting mass
def sort_mass(mass, bfld):
    #sort the mass array
    sorted_mass = np.sort(mass)
    #create a new array to store the sorted bfld
    sorted_bfld = np.zeros(len(bfld))
    #iterate over the sorted mass array
    for i in range(0,len(sorted_mass)):
        #find the index of the mass in the unsorted mass array
        index = np.where(mass == sorted_mass[i])
        #store the bfld in the sorted bfld array
        sorted_bfld[i] = bfld[index[0][0]]
    return sorted_mass, sorted_bfld