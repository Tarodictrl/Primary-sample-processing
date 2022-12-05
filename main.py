from Processing import Processing
import pandas as pd

if __name__ == '__main__':
    p = Processing("samples/I22.csv")
    print("Min value:=", p.min_value)
    print("Max value:=", p.max_value)
    print("Scope:=", p.scope)
    print("Number of intervals:=", p.number_intervals)
    print("Interval:=", p.interval)
    print(pd.DataFrame(p.mid_intervals, columns=['Mid intervals']))
    print("Sample average:=", p.sample_average)
    print("Median:=", p.median)
    print("Sample variance:=", p.sample_variance)
    print("Standard deviation:=", p.standard_deviation)
    print("Sample moments of the 3rd order:=", p.get_sample_moment(3))
    print("Sample moments of the 4rd order:=", p.get_sample_moment(4))
    print("Selective excess:=", p.selective_excess)
    print("Coefficient of asymmetry:=", p.coefficient_asymmetry)
    p.histogram()