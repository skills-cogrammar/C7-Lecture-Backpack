from ydata_profiling import ProfileReport
import pandas as pd
import sweetviz
import dtale

data = pd.read_csv('data/car_details_v4.csv')  # Load the dataset from CSV file

# # Generate and save the profiling report using ydata_profiling
# profile = ProfileReport(data, title="Profiling Report")
# profile.to_file("profiling_report_new.html")

# # Generate an interactive data report using sweetviz
# sweetviz_report = sweetviz.analyze(data)
# sweetviz_report.show_html('sweetviz_report.html')

# Start a D-Tale instance for the data and open it in the default browser
d = dtale.show(data)
d.open_browser()


print("Press Enter to exit...")
input()  # Wait for user input before exiting