import numpy as np
import matplotlib.pyplot as plt



def norm_histogram(hist):
    """
    takes a list of counts and converts to a list of probabilities, which is an output
    with a sum of the counts, i.e. the number of samples(int)
    :param hist: a numpy ndarray object
    :return: a tuple that contains a list and a int, i.e. ([...], int)
    """
    # please delete the "pass" below and your code starts here...

    #hist is the number of bins
    tuple_length = len(hist) #gives the length of the tuple
    summation = sum(hist) #adds up all values in histogram 
    i = 0
    c = 0
    counter = 0
    while i <= (tuple_length - 1): #iterates through given tuple
        counter = hist[i] + counter #totals up all entires from given tuple
        i = i + 1
    list_prob = [0] * tuple_length     #create a new list

    while c < (tuple_length):  #be able to iterate through new tuple
        list_prob[c] = hist[c] / counter #get the probabilites and place into each tuple
        c = c + 1
    tuple_prob = tuple(list_prob) #creates a probability in a tuple
    return tuple_prob, summation
    
    


    


def compute_j(histo, width):
    """
    takes list of counts, uses norm_histogram function to output the list of probabilities and the number of samples, 
    then calculates compute_j for one bin width (reference: histogram.pdf page19)
    :param histo: list
    :param width: float
    :return: float
    """
    # please delete the "pass" below and your code starts here...
    
    tup_problist, value = norm_histogram(histo) #Get the probabilites of the tuples
    tup_len = len(tup_problist) #Get length of list
    #samp_num = tup_problist[tup_len - 1]

    #First part of the j equation
    j1 = 2 / ((width  *(value- 1))) #First part of equation in class

    #2nd part of the j equation
    j2 = (value + 1) / ((value -1) * width) #2nd part of equation in class

    #third part of the j eqation
    i = 0
    j3 = 0
    j4 = 0
    
    while i < (tup_len):
       
        j3 = (tup_problist[i])
        j4 = (j3**2) + j4 #3rd part of eqution in class
        i = i + 1
    j_val = j1 - (j2 * j4) #Entire minimum value equation 

    return j_val  #Not sure if this is what i am suppose to do here??????????????????????????????????????????????????


def sweep_n(data, minimum, maximum, min_bins, max_bins):
    """
    find the optimal bin
    calculate compute_j for a full sweep [min_bins to max_bins]
    please make sure max_bins is included in your sweep
    
    The variable "data" is the raw data that still needs to be "processed"
    with matplotlib.pyplot.hist to output the histogram

    You need to utilize the variables (data, minimum, maximum, min_bins, max_bins) 
    in sweep_n functions to give values to (x, bins, range) in the function matplotlib.pyplot.hist
    Other input variables of matplotlib.pyplot.hist can be set as default value.
    
    :param data: list
    :param minimum: int
    :param maximum: int
    :param min_bins: int
    :param max_bins: int
    :return: list
    """
    # please delete the "pass" below and your code starts here...
    list_jVAL = []
    #range_val = maximum - minimum
    for values in range(min_bins, max_bins + 1):
        histogram_stats = plt.hist(data, values, (minimum, maximum))[0] #Get all histogram stats
        jVAL = compute_j(histogram_stats, ((maximum-minimum) / values)) #Compute list of jvalues
        list_jVAL.append(jVAL) #Add values
    return list_jVAL


def find_min(l):
    """
    takes a list of numbers and returns a tuple that contains the value and index of the two smallest numbers in that list and their mean.
    i.e. 
    ([index_of_smallest_number, index_of_second_smallest_number],[value_of_smallest_number, value_of_second_smallest_number], mean)}
    
    For example:
        If the input list (l) is [14,27,15,49,23,41,147]
        Then it should return ([0,2], [14,15], 14.5)

    :param l: list
    :return: tuple
    """
    # please delete the "pass" below and your code starts here...
    
    min1 = min(l) #Minium val 1
    min_pos1 = l.index(min(l)) #Pos of min value 1
    l.remove(min1) #Can i remove this ??????????????????????????????????????????????????

    min2 = min(l) #min value 2
    min_pos2 = l.index(min(l)) #pos of min val 2
    l.remove(min2) #Can i remove this ??????????????????????????????????????????????????

    mean = (min1 + min2) / 2

    num1_list = [min_pos1, min_pos2] #list of index
    num2_list = [min1, min2] #Actual min vals

    tup_two = (num1_list, num2_list, mean)

    return(tup_two)


if __name__ == "__main__":
    data = np.loadtxt("input.txt")  # reads data from input.txt
    lo = min(data)
    hi = max(data)
    bin_l = 1
    bin_h = 100
    js = sweep_n(data, lo, hi, bin_l, bin_h)
    """
    the values bin_l and bin_h represent the lower and higher bound of the range of bins.
    They will change when we test your code and you should be mindful of that.
    """
    print(find_min(js))
