import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def cpr_graph(objects, caliber, filename):

    average_cpr = calc_avg(objects)
    
    # Extract self.cpr and self.timestamp as paired variables
    print(average_cpr)
    current_datetime = datetime.now()

    # Format the current date and time as "month day, year"
    formatted_datetime = current_datetime.strftime('%B %d, %Y')

    # Convert datetime strings to datetime objects
    # Plotting the line graph
    plt.plot(formatted_datetime, average_cpr, marker='x')
    plt.xlabel('CPR')
    plt.ylabel('Datetime', rotation=90)
    plt.title(f'{caliber} CPR on {formatted_datetime}')

    # Save the graph as a PNG image
    plt.savefig(filename)

def calc_avg(objects):
    total = 0
    count = 0

    for obj in objects:
            if hasattr(obj, 'cpr'):  # Check if the object has the 'cpr' attribute
                cpr_value = getattr(obj, 'cpr')
                try:
                    total += float(cpr_value)  # Convert the cleaned string to a float and accumulate   
                except ValueError:
                    pass  # Ignore the value if it cannot be converted to a float
            else:
                total += cpr_value  # If it's already a float, accumulate directly

            count += 1

    # if count > 0:
    temp_average = total / count
    average = round(temp_average, 2)
    print(average)
    return average
