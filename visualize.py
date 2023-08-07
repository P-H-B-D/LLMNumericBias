#load the data from the csv named 1_10_n1000.csv
import csv
import matplotlib.pyplot as plt
import os 



for item in os.listdir("./datasets"):
    plt.clf()
    data=[]
    pathname="./datasets/"+item

    name=pathname.split("/")[2]
    low=int(name.split("_")[0])
    high=int(name.split("_")[1].split("_")[0])

    with open(pathname, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(int(row[0]))

    weights = [1/len(data) for _ in data]

    # Plot histogram with proportions
    plt.hist(data, bins=range(low, high+2), edgecolor="k", align='left', weights=weights) #works well for ints, but not for floats
    expected_proportion = 1/len(range(low, high+1))
    plt.axhline(y=expected_proportion, color='r', linestyle='--', label="Expected Proportion")

    # Set the title and labels
    plt.title(f'Integers from {low} to {high}, n= '+str(len(data)))
    plt.xlabel('Value')
    plt.ylabel('Proportion')
    plt.xticks(list(range(low, high+1)))

    #save in figures folder
    plt.savefig("./figures/"+name+".png")

