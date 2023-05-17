import matplotlib.pyplot as plt

def create_graph(ammunitions):
    # Extract the cpr values from the Ammunition objects
    cpr_values = [ammo.cpr for ammo in ammunitions]

    # Create the x-axis values as indices of the cpr_values list
    x_values = range(len(cpr_values))

    # Plot the line graph
    plt.plot(x_values, cpr_values, marker='o')

    # Customize the graph labels and title
    plt.xlabel('Ammunition Index')
    plt.ylabel('CPR Value')
    plt.title('Line Plot of CPR Values')

    # Save the graph as an image file
    plt.savefig('line_plot.png')

    # Display the graph
    plt.show()
