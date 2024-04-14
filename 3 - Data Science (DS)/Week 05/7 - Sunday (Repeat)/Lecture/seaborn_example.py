# Import seaborn, matplotlib, numpy
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#Check available datasets
print(sns.get_dataset_names())

# Load an example dataset
peng_df = sns.load_dataset("penguins")

#If you are unable to load the data due to SSL certificate error
#you can either fix it following this:
#https://stackoverflow.com/questions/57483667/ssl-certificate-verify-failed-error-when-loading-data-into-seaborn
#or you can download the data as a csv file from here
#https://github.com/mwaskom/seaborn-data

#Check the dataset
peng_df.info()

#Scatterplot
sns.scatterplot(x="flipper_length_mm", y="body_mass_g", 
                data=peng_df, hue="species")
plt.show()

# #Lineplot
sns.lineplot(x="flipper_length_mm", y="body_mass_g", 
             data=peng_df, hue="species")
plt.show()

#Barplot
sns.barplot(x="species", y="body_mass_g", 
            hue="sex", data=peng_df)
plt.show()

#Histogram
sns.histplot(x="bill_length_mm", data=peng_df, 
             bins=20, kde=True, color="green")
plt.show()

#Kernel density plot
sns.kdeplot(data=peng_df, x="bill_length_mm")
plt.show()
sns.kdeplot(data=peng_df, x="bill_length_mm", 
            hue="species", fill=True, alpha=0.6, linewidth=1.5)
plt.show()

#Boxplot
sns.boxplot(x="island", y="body_mass_g", hue="sex", 
            data=peng_df, palette="Set1", linewidth=1.5)
plt.show()

#Violinplot
sns.violinplot(x="species", y="body_mass_g", 
               hue="sex", data=peng_df)
plt.show()

#Categorical plot
sns.catplot(data=peng_df, kind="swarm", 
            x="species", y="body_mass_g", hue="sex")
plt.show()

#Heatmap
#Create correlation between variables (floats only)
print(peng_df.dtypes)
peng_float = peng_df.select_dtypes(include=[np.float64])
corr = peng_float.corr()

#Plot
plt.figure(figsize=(10,7))
sns.heatmap(corr, annot=True)
plt.show()

#Parallel coordinates
# Calculate the average values for each continent
average_data = peng_df.groupby('species')[['body_mass_g', 'flipper_length_mm', 
                                           'bill_length_mm','bill_depth_mm']].mean()

# Normalize the data for better visualization
normalized_data = (average_data - average_data.mean()) / average_data.std()

# Create parallel plot
plt.figure(figsize=(8, 6))
parallel_plot = sns.lineplot(data=normalized_data.transpose(),
                             dashes=False,
                             markers=True,
                             markersize=8)
plt.show()

#Pairplot
sns.pairplot(peng_df, hue="species")
plt.show()

#Jointplot
sns.jointplot(data=peng_df, x="flipper_length_mm", 
              y="bill_length_mm", hue="species")
plt.show()

#Combination plots
g = sns.PairGrid(peng_df, hue="species", corner=True)
g.map_lower(sns.kdeplot, hue=None, levels=5, color=".2")
g.map_lower(sns.scatterplot, marker="+")
g.map_diag(sns.histplot, element="step", linewidth=0, kde=True)
g.add_legend(frameon=True)
g.legend.set_bbox_to_anchor((.61, .6))
plt.show()