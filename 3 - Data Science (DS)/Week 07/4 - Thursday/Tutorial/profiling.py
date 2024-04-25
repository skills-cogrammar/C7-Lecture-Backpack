from ydata_profiling import ProfileReport
import pandas as pd
import sweetviz
import dtale

# Load the dataset from CSV file
data = pd.read_csv('data/car_details_v4.csv')


# my_report = sweetviz.analyze(data)
# my_report.show_html()

profile = ProfileReport(data, title="Profiling Report")
profile.to_file("profiling_report_new.html")

# Start a D-Tale instance for the data
d = dtale.show(data)
# using Python's `webbrowser` package it will try and open your server's default browser to this process
d.open_browser()