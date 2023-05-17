import matplotlib.pyplot as plt

def cpr_graph(objects, filename):

    # Extract self.cpr and self.timestamp as paired variables
    paired_variables = [(obj.timestamp, obj.cpr) for obj in objects]

    # Unzip the paired variables into separate lists for x and y values
    timestamps, cpr_values = zip(*paired_variables)

    # Plotting the line graph
    plt.plot(timestamps, cpr_values, marker='o')
    plt.xlabel('Time')
    plt.ylabel('self.cpr')
    plt.title('self.cpr over Time')

    # Formatting the x-axis tick labels as dates
    date_fmt = '%Y-%m-%d'  # Format for the tick labels
    plt.gca().xaxis.set_major_formatter(plt.FixedFormatter([timestamp.strftime(date_fmt) for timestamp in timestamps]))

    # Rotating the x-axis tick labels for better readability
    plt.xticks(rotation=45)

    # Save the line graph as an image
    plt.tight_layout()
    plt.savefig(filename, dpi=300, format='png')

