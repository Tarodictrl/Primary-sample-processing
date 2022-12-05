import csv
import math
import numpy as np
import matplotlib.pyplot as plt


class Processing:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.data = np.array(sorted(self.get_data()))
        self.min_value = min(self.data)
        self.max_value = max(self.data)
        self.scope = self.max_value - self.min_value
        self.number_intervals = int(1 + 3.322 * math.log10(len(self.data)))
        self.interval = self.scope / self.number_intervals
        self.mid_intervals = np.array(
            [self.min_value + (self.interval/2) * (i*self.interval)
             for i in range(int(self.number_intervals))]
        )
        self.sample_average = np.average(self.data)
        self.median = np.median(self.data)
        self.sample_variance = np.var(self.data)
        self.standard_deviation = np.std(self.data)
        self.selective_excess = self.get_sample_moment(3) / self.standard_deviation**3
        self.coefficient_asymmetry = self.get_sample_moment(3) / self.standard_deviation**3
        
        
    def get_data(self):
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            data = np.array([float(row[1]) for row in reader])
        return data

    def histogram(self):
        plt.hist(self.data, bins=int(self.number_intervals))
        plt.draw()
        plt.savefig(f'images/{self.filename.split("/")[1].split(".")[0]}.png')
        plt.show()
        
    def get_sample_moment(self, k: int) -> float:
        return np.average(self.data**k)