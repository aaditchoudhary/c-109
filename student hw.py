import pandas as pd
import plotly.express as px
import math
import csv
import plotly.figure_factory as ff
import statistics
df=pd.read_csv(r"C:\Users\a2z\Downloads\Data-visualization-master\Data-visualization-master\csv files\StudentsPerformance (2).csv")
mathScore_list=df["math score"].tolist()
mathScore_mean=statistics.mean(mathScore_list)
mathScore_median=statistics.median(mathScore_list)
mathScore_mode=statistics.mode(mathScore_list)
print("Mean, Median and Mode of mathScore is {}, {} and {} respectively".format(mathScore_mean, mathScore_median, mathScore_mode))
mathScore_std_deviation = statistics.stdev(mathScore_list)
mathScore_first_std_deviation_start, mathScore_first_std_deviation_end = mathScore_mean-mathScore_std_deviation, mathScore_mean+mathScore_std_deviation
mathScore_second_std_deviation_start,mathScore_second_std_deviation_end =mathScore_mean-(2*mathScore_std_deviation), mathScore_mean+(2*mathScore_std_deviation)
mathScore_third_std_deviation_start, mathScore_third_std_deviation_end = mathScore_mean-(3*mathScore_std_deviation), mathScore_mean+(3*mathScore_std_deviation)
mathScore_list_of_data_within_1_std_deviation = [result for result in mathScore_list if result > mathScore_first_std_deviation_start and result < mathScore_first_std_deviation_end]
mathScore_list_of_data_within_2_std_deviation = [result for result in mathScore_list if result > mathScore_second_std_deviation_start and result < mathScore_second_std_deviation_end]
mathScore_list_of_data_within_3_std_deviation = [result for result in mathScore_list if result > mathScore_third_std_deviation_start and result < mathScore_third_std_deviation_end]
print("{}% of data for mathScore lies within 1 standard deviation".format(len(mathScore_list_of_data_within_1_std_deviation)*100.0/len(mathScore_list)))
print("{}% of data for mathScore lies within 2 standard deviations".format(len(mathScore_list_of_data_within_2_std_deviation)*100.0/len(mathScore_list)))
print("{}% of data for mathScore lies within 3 standard deviations".format(len(mathScore_list_of_data_within_3_std_deviation)*100.0/len(mathScore_list)))