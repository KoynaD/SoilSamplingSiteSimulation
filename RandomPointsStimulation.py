import matplotlib.pyplot as plt
import random

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

# Create a plot
plt.figure(figsize=(6, 6))  # Adjust the figure size as needed
plt.xlim(0, square_size)
plt.ylim(0, square_size)

# Plot the square
square = plt.Rectangle((0, 0), square_size, square_size, fill=False, color='blue', linewidth=2)
#plt.gca().add_patch(square)

# Plot the random point
plt.plot(point1_x, point1_y, 'ro')
plt.plot(point2_x, point2_y, 'bo')
plt.plot(point3_x, point3_y, 'go')
plt.plot(point4_x, point4_y, 'ro')
plt.plot(point5_x, point5_y, 'ro')
plt.plot()


# Set labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
#plt.legend()

# Show the plot
plt.title('Random Point in a Square')
plt.grid()
plt.show()




