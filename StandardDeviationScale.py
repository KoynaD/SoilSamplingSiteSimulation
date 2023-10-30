import matplotlib.pyplot as plt
import random
import math
import numpy as np

std_values = [0 for i in range(100)]

for a in range(100):

    # Define the size of the square
    square_size = 10  # You can adjust the size as needed

    # Generate a random point within the square
    point1_x = random.uniform(0, square_size)
    point1_y = random.uniform(0, square_size)

    # Generate 2nd random point within the square
    if (point1_x <= 5) :
        point2_x = random.uniform(5, square_size)
        point2_y = random.uniform(0, square_size)

    else:
        point2_x = random.uniform(0, 5)
        point2_y = random.uniform(0, square_size)

    # Generate 3rd random point within the square
    if (point1_y <= 5) :
        point3_x = random.uniform(1, square_size)
        point3_y = random.uniform(5, square_size)

    else:
        point3_x = random.uniform(0, square_size)
        point3_y = random.uniform(0, 5)

    # Generate 4th point 
    point4_x = random.choice([0,10])
    point4_y = random.uniform(0, 10)

    # Generate 5th point 
    point5_y = random.choice([0, 10])
    point5_x = random.uniform(0, 10)
    
    point1 = [point1_x, point1_y]
    point2 = [point2_x, point2_y]
    point3 = [point3_x, point3_y]
    point4 = [point4_x, point4_y]
    point5 = [point5_x, point5_y]

    coordinates = [point1,point2,point3,point4,point5]

    distance = [0 for i in range(math.comb(5, 2))] 
    c = 0
    for x in range(5):
        for y in range(x+1,5):
            distance[c] = math.sqrt((coordinates[x][0] - coordinates[y][0] )**2 + (coordinates[x][1] - coordinates[y][1] )**2)
            c = c+1

    # Calculate the standard deviation
    std_deviation = np.std(distance)

    std_values[a] = std_deviation

for x in range(100):
    plt.plot(std_values[x], 1, 'ro')

# Adding labels and title
plt.xlabel('Index')
plt.title('Line Plot of 100 Numbers')

# Display the plot
plt.show()
