import scipy.stats as stats
import numpy as np


def get_data(filename):
    return np.loadtxt(filename)


def get_coordinates(data, each_dist):
    # Part A
    """
    :param: np.ndarray, str
    :return: np.ndarray, np.ndarray
    """
    # Your code starts here...
    x, y = stats.probplot(data, dist=each_dist) 
    return(x)


def calculate_distance(x, y):
    # Part B

    """
    :param: float, float
    :return: float
    """
    # Your code starts here...
    part_one = x #First part of eq
    part_two = (x + y) / 2  #2nd part of eq
    part_three = y #3rd part of eq
    calc_dist = np.sqrt(((part_one - part_two)*(part_one - part_two)) + ((part_three - part_two)*(part_three - part_two))) #entire equation 
    return(calc_dist)

def find_dist(sum_err, dists):
    # Part C
    """
    :param: list[float], list[str]
    :return: float, str
    """
    # Your code starts here...
    min_val = min(sum_err) #minimum sum error
    index1 = sum_err.index(min_val) #index of that value
    name = dists[index1] #name of the value
    return(min_val, name)


def main(data_file):
    """
    Input a csv file and return distribution type, the error corresponding to the distribution type (e.g. return 0.32, 'norm')
    :param: *.csv file name (str)
    :return: float, str
    """
    # Part B
    data = get_data(data_file) #Get the data
    dists = ("norm", "expon", "uniform", "wald") #Create a tuple of the names
    sum_err = [0] * 4 #Set list size
    for ind, each_dist in enumerate(dists):
        X, Y = get_coordinates(data, each_dist) #et the coordinates
        for x, y in zip(X, Y):
            sum_err[ind] += calculate_distance(x, y) #Find the distances
    return find_dist(sum_err, dists)


if __name__ == "__main__":
    #test case for calculate_distance function
    print("Test case for calculate_distance:")
    print("Student answer was (rounded to 4 places):", round(calculate_distance(10, 20),4), "    calculate_distance answer correct?",
          round(calculate_distance(10, 20),4) == 7.0711)
    print(" ")
    print("Error and the distribution selected for the given .csv files ")
    
    for each_dataset in [
        "sample_norm.csv",
        "sample_expon.csv",
        "sample_uniform.csv",
        "sample_wald.csv",
        "distA.csv",
        "distB.csv",
        "distC.csv",
    ]:
        print(main(each_dataset))
