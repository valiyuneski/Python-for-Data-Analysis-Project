import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (replace with your file path)
df = pd.read_csv("data.csv")

# -------------------------
# 1. DATA CLEANING
# -------------------------

# 1.1.1 Identify missing values
print("\nMissing values:\n", df.isnull().sum())

# 1.1.2 Decide how to handle missing data for each column (e.g., fill with appropriate values, drop rows, etc.).
df = df.dropna(subset=["Engine HP", "Engine Cylinders", "Number of Doors", "MSRP"])
df["Market Category"] = df["Market Category"].fillna("unknown")
df["Engine Fuel Type"] = df["Engine Fuel Type"].fillna("unknown")

# 1.2 Data type conversion (insure Year is integer)
df["Year"] = df["Year"].astype(int)

# 1.3 Filter cars from 1995 onwards
df = df[df["Year"] >= 1995]

# 1.4 String operations (Standardize text entries by converting these columns' entries to lowercase)
df["Vehicle Style"] = df["Vehicle Style"].str.lower()
df["Market Category"] = df["Market Category"].str.lower()

# -------------------------
# 2. FEATURE ENGINEERING
# -------------------------

# 2.1 Create a column called Total MPG that is the average of city mpg and highway MPG
df["Total MPG"] = (df["city mpg"] + df["highway MPG"]) / 2

# 2.2 Create a column called Price per HP calculated as: MSRP / Engine HP.
df["Price per HP"] = df["MSRP"] / df["Engine HP"]

# -------------------------
# 3. EXPLORATORY DATA ANALYSIS
# -------------------------

# 3.1 Descriptive statistics
# Calculate summary statistics (mean, median, standard deviation) for the following columns:
# Engine HP, MSRP, Popularity, highway MPG, and city mpg
stats = df[["Engine HP", "MSRP", "Popularity", "highway MPG", "city mpg"]].describe()
print("\nDescriptive Statistics:\n", stats)

# 3.2 Group analysis
# Group the data by the following columns and calculate the average MSRP and Popularity for each group:
# Driven_Wheels, Vehicle Size, Engine Cylinders
group_dw = df.groupby("Driven_Wheels")[["MSRP", "Popularity"]].mean()
group_vs = df.groupby("Vehicle Size")[["MSRP", "Popularity"]].mean()
group_cyl = df.groupby("Engine Cylinders")[["MSRP", "Popularity"]].mean()

print("\nDriven Wheels:\n", group_dw)
print("\nVehicle Size:\n", group_vs)
print("\nEngine Cylinders:\n", group_cyl)

# -------------------------
# VISUALIZATIONS
# -------------------------

# 3.3.1 Histogram: city mpg
plt.figure()
df["city mpg"].hist(bins=30)
plt.title("City MPG Distribution")
plt.xlabel("City MPG")
plt.ylabel("Frequency")
plt.savefig('city_mpg_histogram.png')
plt.close()

# 3.3.2 Bar chart: average MSRP by Vehicle Size
plt.figure()
group_vs["MSRP"].plot(kind="bar")
plt.title("Average MSRP by Vehicle Size")
plt.ylabel("MSRP")
plt.savefig('msrp_by_vehicle_size.png')
plt.close()

# 3.3.3 Scatter plot: Engine HP vs MSRP
plt.figure()
plt.scatter(df["Engine HP"], df["MSRP"])
plt.title("Engine HP vs MSRP")
plt.xlabel("Engine HP")
plt.ylabel("MSRP")
plt.savefig('engine_hp_vs_msrp.png')
plt.close()

# 3.3.4 Boxplot: MSRP by Driven_Wheels
plt.figure()
sns.boxplot(x="Driven_Wheels", y="MSRP", data=df)
plt.title("MSRP Distribution by Driven Wheels")
plt.savefig('msrp_by_driven_wheels.png')
plt.close()

# -------------------------
# CORRELATION ANALYSIS
# -------------------------

# 3.4 Correlation analysis
# Calculate the correlation matrix for the following columns:
# Engine HP, MSRP, Popularity, city mpg, and highway MPG
corr = df[["Engine HP", "MSRP", "Popularity", "city mpg", "highway MPG"]].corr()
print("\nCorrelation Matrix:\n", corr)

# Optional: heatmap
plt.figure()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig('correlation_heatmap.png')
plt.close()