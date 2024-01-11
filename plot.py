import pandas as pd
import matplotlib.pyplot as plt

# Load the Locust results CSV file
df = pd.read_csv("C:\Users\imen\Desktop\final\part1.csv")

# Plot a graph (example: Requests per second)
plt.plot(df['Time'], df['RPS'])
plt.xlabel('Time (s)')
plt.ylabel('Requests per second')
plt.title('Locust Performance')
plt.show()
