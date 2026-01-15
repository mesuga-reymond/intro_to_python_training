import marimo

__generated_with = "0.19.2"
app = marimo.App(width="medium")


@app.cell
def _():
    # =============================================================================
    # Required Python Libraries for Geospatial Calculations Exercises
    # =============================================================================

    # Core libraries for data manipulation
    # pandas: for working with DataFrames, filtering, grouping, merging
    # polars: for fast DataFrame operations similar to Pandas

    # Numerical operations
    # numpy: for vectorized calculations, generating synthetic data, and math functions

    # Plotting and visualization
    # matplotlib: for scatter plots of farm locations

    # Install these libraries via pip if not already installed:
    # pip install pandas polars numpy matplotlib pyarrow

    # Note:
    # - Polars is optional but recommended for performance practice
    return


@app.cell
def _():
    import marimo as mo

    mo.md("""
    # Introduction to DataFrames (pandas)

    **Audience:** Philippine Statistics Authority

    This notebook introduces DataFrames using theoretical agricultural survey data.
    The concepts here are foundational for data analysis, geospatial processing,
    and future AI / Machine Learning workflows.
    """)
    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # 4.1 Introduction to DataFrames

    DataFrames are the central structure for working with tabular data in Python.
    They allow us to organize, manipulate, and analyze survey data easily.

    Two popular libraries for DataFrames are:

    1. **pandas** – widely used, easy to learn
    2. **polars** – newer, faster, optimized for large datasets

    In the context of the Philippine Statistics Authority (PSA) agricultural surveys, the data may look something like this:

    - Each **row** represents a farm, household, or agricultural plot
    - Each **column** represents a survey variable (crop type, farm area, production, etc.)
    - Each **cell** contains a recorded value from the survey

    Understanding DataFrames is essential before moving on to data cleaning, analysis, geospatial work, and eventually AI/ML.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import polars as pl
    return pd, pl


@app.cell
def _(mo):
    mo.md("""
    We import **pandas** and **polars** to allow side-by-side comparison.
    Later, you will see that **almost all concepts are identical** between the two libraries.
    """)
    return


@app.cell
def _(pd):
    # Pandas Series
    crop_series_pd = pd.Series(
        ["Rice", "Corn", "Rice", "Banana"],
        name="Crop_Type"
    )
    crop_series_pd
    return


@app.cell
def _(pl):
    # Polars Series
    crop_series_pl = pl.Series("Crop_Type", ["Rice", "Corn", "Rice", "Banana"])
    crop_series_pl
    return


@app.cell
def _(mo):
    mo.md("""
    **Explanation:**

    - Each value represents the crop planted by a farm
    - Index (0,1,2,3) represents individual survey records
    - `Crop_Type` describes the variable

    Polars Series are similar to pandas Series, but optimized for **speed and larger datasets**.
    """)
    return


@app.cell
def _(pd):
    # Pandas DataFrame
    data_pd = {
        "Region": ["IV-A", "IV-A", "III", "III"],
        "Crop": ["Rice", "Corn", "Rice", "Banana"],
        "Farm_Area_ha": [1.2, 0.8, 2.5, 1.0],
        "Production_mt": [4.8, 2.1, 10.2, 7.5],
    }

    df_pd = pd.DataFrame(data_pd)
    df_pd
    return (df_pd,)


@app.cell
def _(pl):
    # Polars DataFrame
    df_pl = pl.DataFrame(
        {
            "Region": ["IV-A", "IV-A", "III", "III"],
            "Crop": ["Rice", "Corn", "Rice", "Banana"],
            "Farm_Area_ha": [1.2, 0.8, 2.5, 1.0],
            "Production_mt": [4.8, 2.1, 10.2, 7.5]
        }
    )
    df_pl
    return (df_pl,)


@app.cell
def _(mo):
    mo.md("""
    **Key Points:**

    - Both pandas and polars DataFrames represent the complete survey table
    - Each column is a Series internally
    - Each row is a single farm / survey record
    - For now, understanding the **DataFrame concept** is more important than the library used
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## 4.2 Basic DataFrame Operations

    Once you have a DataFrame, the next step is to **inspect, select, filter, and manipulate** data.

    In the context of agricultural surveys, these operations allow analysts to:

    - Look at specific variables (columns)
    - Filter farms by region, crop, or production
    - Create new calculated variables (e.g., yield per hectare)

    We will demonstrate **pandas** and **polars** equivalents side by side.
    """)
    return


@app.cell
def _(df_pd):
    # Pandas: selecting a column
    farm_area_pd = df_pd["Farm_Area_ha"]
    farm_area_pd
    return


@app.cell
def _(df_pl):
    # Polars: selecting a column
    farm_area_pl = df_pl["Farm_Area_ha"]
    farm_area_pl
    return


@app.cell
def _(mo):
    mo.md("""
    **Discussion: Selecting Columns**

    - **What we did:** Extracted a single column (`Farm_Area_ha`) from the DataFrame.
    - **Pandas:** Use `df["column_name"]` to select a column.
    - **Polars:** Use `df["column_name"]` as well.
    - **Why it’s useful:** Analysts often need to work with one variable at a time, e.g., calculating statistics like mean farm size.
    - **Note:** Both libraries treat a column as a Series internally.
    """)
    return


@app.cell
def _():
    return


@app.cell
def _(df_pd):
    # Pandas: filter farms in region 'III'
    df_region_pd = df_pd[df_pd["Region"] == "III"]
    df_region_pd.iloc[0]
    return


@app.cell
def _(df_pl, pl):
    # Polars: filter farms in region 'III'
    df_region_pl = df_pl.filter(pl.col("Region") == "III")
    df_region_pl
    return


@app.cell
def _(mo):
    mo.md("""
    **Discussion: Filtering Rows**

    - **What we did:** Selected only farms in Region 'III'.
    - **Pandas:** Boolean indexing `df[df["Region"] == "III"]`.
    - **Polars:** `filter(pl.col("Region") == "III")`.
    - **Why it’s useful:** Filtering lets you analyze subsets of data, like a specific region or crop type.
    - **Tip:** Combine multiple conditions with `&` (and) or `|` (or) for more complex filters.
    """)
    return


@app.cell
def _(df_pd):
    # Pandas: calculate yield (Production / Farm Area)
    df_pd_yield = df_pd.copy()
    df_pd_yield["Yield_mt_per_ha"] = df_pd_yield["Production_mt"] / df_pd_yield["Farm_Area_ha"]
    df_pd_yield
    return


@app.cell
def _(df_pl, pl):
    # Polars: calculate yield (Production / Farm Area)
    df_pl_yield = df_pl.with_columns(
        (pl.col("Production_mt") / pl.col("Farm_Area_ha")).alias("Yield_mt_per_ha")
    )
    df_pl_yield
    return


@app.cell
def _(mo):
    mo.md("""
    **Discussion: Calculating Yield**

    - **What we did:** Created a new column `Yield_mt_per_ha` by dividing Production by Farm Area.
    - **Pandas:** Simply assign a new column with the calculation.
    - **Polars:** Use `with_columns()` and `alias()` to create the new column.
    - **Why it’s useful:** Yield is a key metric in agriculture; derived columns allow analysts to compute new variables from existing data.
    - **Tip:** Always check that units are consistent (e.g., hectares vs. square meters) before calculation.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    **Key points:**

    - Column selection works similarly in pandas and polars
    - Row filtering is essential for analyzing specific regions or crops
    - Derived columns allow calculation of metrics like yield
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## 4.3 Advanced DataFrame Operations

    In real-world survey data, we often need to:

    - Combine datasets (merging/joining)
    - Handle missing or incomplete data

    These operations are **Advanced-level** and prepare analysts for more complex data tasks, like geospatial joins or AI/ML preprocessing.

    We will demonstrate both **pandas** and **polars** approaches.
    """)
    return


@app.cell
def _(pd):
    # Pandas: merge two DataFrames
    df_farm_info_pd = pd.DataFrame(
        {"Farm_ID": [1, 2, 3, 4], "Owner": ["Juan", "Maria", "Pedro", "Ana"]}
    )

    df_crop_pd = pd.DataFrame(
        {
            "Farm_ID": [1, 2, 3, 4],
            "Crop": ["Rice", "Corn", "Rice", "Banana"],
            "Production_mt": [4.8, 2.1, 10.2, 7.5],
        }
    )

    df_merged_pd = pd.merge(df_farm_info_pd, df_crop_pd, on="Farm_ID")
    df_merged_pd
    return


@app.cell
def _(pl):
    # Polars: join two DataFrames
    df_farm_info_pl = pl.DataFrame(
        {"Farm_ID": [1, 2, 3, 4], "Owner": ["Juan", "Maria", "Pedro", "Ana"]}
    )

    df_crop_pl = pl.DataFrame(
        {
            "Farm_ID": [1, 2, 3, 4],
            "Crop": ["Rice", "Corn", "Rice", "Banana"],
            "Production_mt": [4.8, 2.1, 10.2, 7.5],
        }
    )

    df_merged_pl = df_farm_info_pl.join(df_crop_pl, on="Farm_ID")
    df_merged_pl
    return


@app.cell
def _(mo):
    mo.md("""
    **Discussion: Merging DataFrames**

    - **What we did:** Combined two separate tables (farm info and crop production) using a common key (`Farm_ID`).
    - **Pandas:** `pd.merge(df1, df2, on="Farm_ID")` performs an inner join by default.
    - **Polars:** `df1.join(df2, on="Farm_ID")` achieves the same result.
    - **Why it’s useful:** Survey data often comes in separate tables (farm owners, production, yields). Merging allows analysis across datasets.
    - **Tip:** Always check that the key column (`Farm_ID`) is unique or matches correctly in both tables to avoid unexpected duplicates.
    """)
    return


@app.cell
def _(pd):
    # Pandas: missing data
    df_missing_pd = pd.DataFrame(
        {"Farm_ID": [1, 2, 3, 4], "Production_mt": [4.8, None, 10.2, None]}
    )

    # Fill missing with mean
    df_filled_pd = df_missing_pd.fillna(df_missing_pd["Production_mt"].mean())
    df_filled_pd
    return


@app.cell
def _(pl):
    # Polars: missing data
    df_missing_pl = pl.DataFrame(
        {"Farm_ID": [1, 2, 3, 4], "Production_mt": [4.8, None, 10.2, None]}
    )

    df_filled_pl = df_missing_pl.with_columns(
        pl.col("Production_mt").fill_null(df_missing_pl["Production_mt"].mean())
    )
    df_filled_pl
    return


@app.cell
def _(mo):
    mo.md("""
    **Discussion: Handling Missing Values**

    - **What we did:** Detected missing values (`None` / `NaN`) and filled them with the mean of the column.
    - **Pandas:** `fillna()` replaces missing values; `dropna()` could remove rows entirely.
    - **Polars:** `fill_null()` performs a similar function.
    - **Why it’s useful:** Missing values are common in surveys (e.g., respondents skipped questions). Filling them allows calculations like averages or totals without errors.
    - **Tip:** Decide carefully whether to **fill**, **drop**, or **impute** based on the type of analysis and data quality.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## 4.4 Reading and Writing Data

    Survey data often comes from **files** rather than pre-built DataFrames.
    In this section, we will:

    - Read CSV files
    - Save DataFrames to CSV
    - Verify data types

    We will use the **farm_survey_large.csv** dataset for these exercises.
    """)
    return


@app.cell
def _(pd):
    # Pandas: read CSV locally (section-specific variable)
    df_pd_farm = pd.read_csv("farm_survey_large.csv")
    df_pd_farm.head()
    return (df_pd_farm,)


@app.cell
def _(pl):
    # Polars: read CSV locally (section-specific variable)
    df_pl_farm = pl.read_csv("farm_survey_large.csv")
    df_pl_farm.head()
    return (df_pl_farm,)


@app.cell
def _(mo):
    mo.md("""
    **Discussion: Reading CSV**

    - **What we did:** Loaded `farm_survey_large.csv` into section-specific DataFrames (`df_pd_farm`, `df_pl_farm`).
    - **Pandas:** `pd.read_csv()` loads CSV data; `head()` shows first rows.
    - **Polars:** `pl.read_csv()` is optimized for larger datasets.
    - **Why it’s useful:** Survey datasets often come in CSV format. Loading correctly is essential for analysis.
    - **Tip:** Always check the first few rows to ensure data loaded correctly.
    """)
    return


@app.cell
def _(df_pd_farm):
    # Pandas: calculate Yield and save
    df_pd_farm_yield = df_pd_farm.copy()
    df_pd_farm_yield["Yield_mt_per_ha"] = df_pd_farm_yield["Production_mt"] / df_pd_farm_yield["Farm_Area_ha"]
    df_pd_farm_yield.to_csv("farm_survey_output_pd.csv", index=False)
    return (df_pd_farm_yield,)


@app.cell
def _(df_pl_farm, pl):
    # Polars: calculate Yield and save
    df_pl_farm_yield = df_pl_farm.with_columns(
        (pl.col("Production_mt") / pl.col("Farm_Area_ha")).alias("Yield_mt_per_ha")
    )
    df_pl_farm_yield.write_csv("farm_survey_output_pl.csv")
    return (df_pl_farm_yield,)


@app.cell
def _(mo):
    mo.md("""
    **Discussion: Writing CSV with Changes**

    - **What we did:** Added a new column `Yield_mt_per_ha` before saving the CSV.
    - **Why it’s useful:** Makes the output CSV more meaningful for analysis and reports.
    - **Tip:** Any transformation (new columns, filtered rows, renamed columns) before saving will create a CSV that is different from the original input, which is often the real-world scenario.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## 4.5 Calculations and Plots

    Using the farm survey dataset with the new `Yield_mt_per_ha` column, we will:

    - Summarize production and yield by **Crop** or **Region**
    - Calculate basic statistics
    - Visualize the data with bar charts, scatter plots, and histograms

    This helps survey analysts quickly explore agricultural data.
    """)
    return


@app.cell
def _(df_pd_farm_yield):
    # Pandas: check the Yield column
    df_pd_farm_yield.head()
    return


@app.cell
def _(df_pl_farm_yield):
    # Polars: check the Yield column
    df_pl_farm_yield.head()
    return


@app.cell
def _(df_pd_farm_yield):
    # Pandas: total production by Crop
    df_total_crop_pd = df_pd_farm_yield.groupby("Crop")["Production_mt"].sum().reset_index()
    df_total_crop_pd
    return (df_total_crop_pd,)


@app.cell
def _(df_pl_farm_yield, pl):
    # Polars: total production by Crop
    df_total_crop_pl = (
        df_pl_farm_yield.group_by("Crop")      # <-- note: group_by instead of groupby
        .agg(pl.sum("Production_mt").alias("Total_Production_mt"))
    )

    df_total_crop_pl
    return (df_total_crop_pl,)


@app.cell
def _(mo):
    mo.md("""
    **Discussion: Grouping by Crop**

    - **What we did:** Summed `Production_mt` for each crop type.
    - **Pandas:** Use `groupby()` + aggregation functions.
    - **Polars:** Use `group_by().agg()`.
    - **Why it’s useful:** Helps identify which crops contribute most to total production.
    - **Tip:** Can also group by Region or by Crop + Region for more detailed analysis.
    """)
    return


@app.cell
def _(df_total_crop_pd):
    import matplotlib.pyplot as plt

    # Pandas bar chart
    df_total_crop_pd.plot.bar(
        x="Crop", y="Production_mt", legend=False, title="Total Production by Crop"
    )
    plt.ylabel("Production (mt)")
    plt.show()
    return (plt,)


@app.cell
def _(df_total_crop_pl, plt):
    # Polars plotting via conversion to pandas (using pyarrow)
    df_total_crop_pl.to_pandas().plot.bar(
        x="Crop", y="Total_Production_mt", legend=False, title="Total Production by Crop"
    )
    plt.ylabel("Production (mt)")
    plt.show()
    return


@app.cell
def _(mo):
    mo.md("""
    **Discussion: Bar Chart**

    - **What we did:** Visualized total production per crop using a bar chart.
    - **Pandas:** Built-in `plot.bar()` is simple for quick charts.
    - **Polars:** Convert to pandas for plotting.
    - **Why it’s useful:** Visualizations allow analysts to quickly understand which crops dominate production.
    """)
    return


@app.cell
def _(df_pd_farm_yield, plt):
    # Pandas scatter plot
    df_pd_farm_yield.plot.scatter(
        x="Farm_Area_ha", y="Yield_mt_per_ha", title="Yield vs Farm Area"
    )
    plt.show()
    return


@app.cell
def _(df_pl_farm_yield, plt):
    # Polars scatter plot via pandas
    df_pl_farm_yield.to_pandas().plot.scatter(
        x="Farm_Area_ha", y="Yield_mt_per_ha", title="Yield vs Farm Area"
    )
    plt.show()
    return


@app.cell
def _(mo):
    mo.md("""
    ## 4.6 Optional Geospatial Calculations

    In agricultural surveys, geospatial analysis helps identify:

    - How far farms are from each other
    - Farms that are geographically close
    - Patterns or clusters that may affect logistics or farm management
    - Farms that are efficient when combining yield and proximity

    In this section, we calculate distances between farms using their **latitude and longitude** (using **Euclidean distance**). We also practice:

    - Filtering farm pairs by distance
    - Summarizing crop yields
    - Calculating farm efficiency metrics

    Students will use both **Pandas** and **Polars** throughout.

    **Learning objectives:**

    1. Compute distances between farms using **latitude and longitude** (Euclidean approximation).
    2. Filter farm pairs that are **“close”** based on a distance threshold.
    3. Summarize crop production by grouping farms by crop type.
    4. Calculate farm **efficiency** by combining yield and distance metrics.
    5. Practice using **both Pandas and Polars** for geospatial operations and aggregations.

    **Notes:**

    - For simplicity in exercises we use **Euclidean distance**, which is sufficient for small-scale survey datasets.
    - Distance values are **in degrees**, but can be roughly converted to kilometers by multiplying by ~111 km/degree.
    - The **Efficiency** metric combines Yield and Distance to identify top-performing farms in both productivity and proximity.
    - This section is optional, but recommended for survey analysts who want to **combine spatial thinking with data analysis**.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## 4.6 Exercises – Geospatial Calculations

    | Exercise Name | Topics | Python, Geospatial, or AI/ML topics covered | Description | Level |
    |---------------|--------|--------------------------------------------|------------|-------|
    | Visualize Farm Locations | pandas, matplotlib | Python, Geospatial | Plot farm locations on a scatter plot using latitude and longitude. | Beginner |
    | Compute Euclidean Distance Between Farms | pandas, polars, numpy | Python, Geospatial | Calculate Euclidean distances between farm pairs using latitude and longitude. | Intermediate |
    | Filter Nearby Farms | pandas, polars | Python, Geospatial | Identify farm pairs that are within a certain distance threshold (e.g., 0.15 degrees or ~16.5 km). | Beginner |
    | Group Crop Yield | pandas, polars | Python, Geospatial | Summarize crop production by grouping farms by crop type and calculating total and average yield. | Intermediate |
    | Analyze Farm Efficiency | pandas, polars | Python, Geospatial, Data Aggregation | Calculate an efficiency metric combining yield and distance to identify top-performing farms. | Advanced |
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 1: Visualize Farm Locations

    **Objective:**
    Plot the farm locations on a scatter plot using latitude and longitude.

    **Instructions:**
    1. Use `df_pd_farms` (Pandas) or `df_pl_farms` (Polars)
    2. Plot `Longitude` on the x-axis and `Latitude` on the y-axis
    3. Add labels, a title, and markers for clarity
    4. Optional: Try different marker sizes or colors to differentiate farms

    **Level:** Beginner
    **Topics:** Pandas, Polars, Matplotlib, Python, Geospatial
    """)
    return


@app.cell
def _(pd, pl):
    # Exercise 1
    # Sample farm dataset
    farm_data = {
        "Farm_Name": ["Farm A", "Farm B", "Farm C", "Farm D", "Farm E"],
        "Latitude": [12.34, 12.45, 12.50, 12.55, 12.60],
        "Longitude": [121.0, 121.1, 121.2, 121.25, 121.3]
    }

    # Create Pandas DataFrame
    df_pd_farms = pd.DataFrame(farm_data)

    # Optional: Polars DataFrame
    df_pl_farms = pl.DataFrame(farm_data)

    df_pd_farms
    return (df_pd_farms,)


@app.cell
def _(df_pd_farms, plt):
    # Using Pandas DataFrame
    plt.figure(figsize=(6, 5))
    plt.scatter(df_pd_farms["Longitude"], df_pd_farms["Latitude"], s=80, color="green")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Farm Locations")
    for i, name in enumerate(df_pd_farms["Farm_Name"]):
        plt.text(df_pd_farms["Longitude"][i]+0.002, df_pd_farms["Latitude"][i]+0.002, name, fontsize=9)
    plt.grid(True)
    plt.show()
    return


@app.cell
def _(mo):
    mo.md("""
    **Explanation of the Solution:**

    - `plt.scatter()` creates a scatter plot of all farms.
    - `Longitude` is plotted on the x-axis and `Latitude` on the y-axis.
    - `plt.text()` labels each point with the farm name.
    - Adding `grid(True)` helps with visual reference.
    - Students can experiment with marker size, color, or different styles to make the plot clearer.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 2: Calculate Distance Between Farms

    **Objective:**
    Compute the Euclidean distance between each pair of farms using latitude and longitude.

    **Instructions:**
    1. Use `df_pd_pairs` (Pandas) or `df_pl_pairs` (Polars)
    2. Compute distance using Euclidean formula:

    Distance = sqrt((Lat2 - Lat1)^2 + (Lon2 - Lon1)^2)

    3. Add a new column `Distance` with the computed distances
    4. Optional: Convert the distance to approximate kilometers by multiplying by 111
    5. Optional: Filter farm pairs with distance < 0.15 degrees (or < ~16 km)

    **Level:** Intermediate
    **Topics:** Pandas, Polars, Python, Geospatial
    """)
    return


@app.cell
def _(pd, pl):
    # Exercise 2
    # Sample farm pairs dataset
    farm_pairs_data = {
        "Farm1": ["Farm A", "Farm A", "Farm B"],
        "Farm2": ["Farm B", "Farm C", "Farm C"],
        "Lat1": [12.34, 12.34, 12.45],
        "Lon1": [121.0, 121.0, 121.1],
        "Lat2": [12.45, 12.50, 12.50],
        "Lon2": [121.1, 121.2, 121.2]
    }

    # Pandas DataFrame
    df_pd_pairs = pd.DataFrame(farm_pairs_data)

    # Polars DataFrame
    df_pl_pairs = pl.DataFrame(farm_pairs_data)

    df_pd_pairs
    return df_pd_pairs, df_pl_pairs


@app.cell
def _(df_pd_pairs):
    import numpy as np

    # Compute Euclidean distance in degrees
    df_pd_pairs["Distance"] = np.sqrt(
        (df_pd_pairs["Lat2"] - df_pd_pairs["Lat1"])**2 +
        (df_pd_pairs["Lon2"] - df_pd_pairs["Lon1"])**2
    )

    # Optional: convert to approximate kilometers
    df_pd_pairs["Distance_km"] = df_pd_pairs["Distance"] * 111

    df_pd_pairs
    return (np,)


@app.cell
def _(df_pl_pairs, pl):
    # Compute Euclidean distance in Polars and assign to new variable
    df_pl_pairs_dist = df_pl_pairs.with_columns(
        (
            ((pl.col("Lat2") - pl.col("Lat1"))**2 + (pl.col("Lon2") - pl.col("Lon1"))**2).sqrt()
        ).alias("Distance")
    )

    # Optional: convert to approximate kilometers
    df_pl_pairs_dist = df_pl_pairs_dist.with_columns(
        (pl.col("Distance") * 111).alias("Distance_km")
    )

    df_pl_pairs_dist
    return (df_pl_pairs_dist,)


@app.cell
def _(mo):
    mo.md("""
    **Explanation of the Solution:**

    - **Euclidean distance** is a simple way to measure straight-line distance between two points.
    - Pandas allows vectorized calculations using `**2` for squares and `np.sqrt()` for the square root.
    - Polars uses expressions with `with_columns()` to compute the distance efficiently.
    - In this example, the result ~0.14866 is **in degrees**, because latitude and longitude are angular measurements.
    - Optional conversion to kilometers: multiply the degree-based distance by ~111 km per degree.
      - 0.14866 degrees → ~16.5 km.
    - Optional filtering can identify **farm pairs that are very close**, e.g.:

    **Pandas:** `df_pd_pairs[df_pd_pairs['Distance'] < 0.15]`
    **Polars:** `df_pl_pairs_dist.filter(pl.col('Distance') < 0.15)`
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 3: Filter Nearby Farms

    **Objective:**
    Identify farm pairs that are “close” to each other using the distance calculated previously.

    **Instructions:**
    1. Use `df_pd_pairs` (Pandas) or `df_pl_pairs_dist` (Polars)
    2. Filter farm pairs based on:
       - **Distance in degrees < 0.15** OR
       - **Distance in km < 16.5 km**
    3. Display the filtered dataset

    **Hints:**
    - In Pandas, use boolean indexing: `df[df['Distance'] < 0.15]`
    - In Polars, use `.filter(pl.col('Distance') < 0.15)`

    **Level:** Beginner
    **Topics:** Pandas, Polars, Python, Geospatial
    """)
    return


@app.cell
def _(df_pd_pairs):
    # Filter farm pairs within 0.15 degrees
    nearby_farms_pd_deg = df_pd_pairs[df_pd_pairs["Distance"] < 0.15]

    # Filter farm pairs within 16.5 km
    nearby_farms_pd_km = df_pd_pairs[df_pd_pairs["Distance_km"] < 16.5]

    print("Nearby farms (degrees):")
    print(nearby_farms_pd_deg)
    print("\nNearby farms (km):")
    print(nearby_farms_pd_km)
    return


@app.cell
def _(df_pl_pairs_dist, pl):
    # Filter farm pairs within 0.15 degrees
    nearby_farms_pl_deg = df_pl_pairs_dist.filter(pl.col("Distance") < 0.15)

    # Filter farm pairs within 16.5 km
    nearby_farms_pl_km = df_pl_pairs_dist.filter(pl.col("Distance_km") < 16.5)

    print("Nearby farms (degrees):")
    print(nearby_farms_pl_deg)
    print("\nNearby farms (km):")
    print(nearby_farms_pl_km)
    return


@app.cell
def _(mo):
    mo.md("""
    **Explanation of the Solution:**

    - This exercise filters farm pairs based on the **Euclidean distance** calculated previously.
    - In **Pandas**, we use a simple boolean condition.
    - In **Polars**, we use `.filter(pl.col('Distance') < 0.15)`.
    - Distance values are **in degrees** (latitude/longitude), optional conversion to km: 0.15° ≈ 16.65 km.
    - This exercise shows how to:
      - Filter rows based on numeric conditions
      - Use both Pandas and Polars
      - Focus analysis on meaningful subsets of survey data
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 4: Group Crop Yield

    **Objective:**
    Using the `farm_survey_large` dataset, summarize crop production by grouping the data by crop type and calculating total and average yield.

    **Instructions:**
    1. Use `df_pd` (Pandas) or `df_pl` (Polars)
    2. Perform a **group by** on the column `Crop`
    3. Calculate:
       - Total yield per crop
       - Average yield per crop
    4. Display the results sorted by **total yield descending**

    **Level:** Intermediate
    **Topics:** Pandas, Polars, Python, Data Aggregation
    """)
    return


@app.cell
def _(np, pd, pl):
    # The data is loaded below for you
    # A synthetic yield column is added for this exercises
    # Load the dataset into brand-new variables
    df_pd_yield_ex4 = pd.read_csv("farm_survey_large.csv")  # new variable
    df_pl_yield_ex4 = pl.from_pandas(df_pd_yield_ex4)

    # Add synthetic Yield column
    np.random.seed(42)
    df_pd_yield_ex4["Yield"] = np.random.randint(800, 2000, size=len(df_pd_yield_ex4))
    df_pl_yield_ex4 = pl.from_pandas(df_pd_yield_ex4)  # update Polars copy

    df_pd_yield_ex4.head()
    return df_pd_yield_ex4, df_pl_yield_ex4


@app.cell
def _(df_pd_yield_ex4):
    # Pandas solution
    total_yield_pd = df_pd_yield_ex4.groupby("Crop")["Yield"].sum().reset_index().sort_values("Yield", ascending=False)
    avg_yield_pd = df_pd_yield_ex4.groupby("Crop")["Yield"].mean().reset_index().sort_values("Yield", ascending=False)

    print("Pandas - Total Yield per Crop:")
    print(total_yield_pd)
    print("\nPandas - Average Yield per Crop:")
    print(avg_yield_pd)
    return


@app.cell
def _(df_pl_yield_ex4, pl):
    # Polars solution
    yield_summary_pl = df_pl_yield_ex4.group_by("Crop").agg([
        pl.sum("Yield").alias("Total_Yield"),
        pl.mean("Yield").alias("Average_Yield")
    ]).sort("Total_Yield", descending=True)  # <-- use descending instead of reverse

    yield_summary_pl
    return


@app.cell
def _(mo):
    mo.md("""
    **Explanation of the Solution:**

    - We added a **synthetic `Yield` column** to simulate realistic crop production values for each farm.
    - **Grouping by `Crop`** allows us to summarize total and average yield per crop.
    - In **Pandas**, `groupby("Crop")` with `.sum()` and `.mean()` efficiently calculates total and average yield.
    - In **Polars**, `group_by("Crop").agg([...])` achieves the same result in a single, fast operation.
    - **Sorting by total yield** highlights which crops contribute the most to production.
      - In Pandas, `sort_values("Yield", ascending=False)` is used.
      - In Polars, `sort("Total_Yield", descending=True)` is used (note `descending=True` replaces `reverse=True`).
    - These techniques are fundamental for **summarizing agricultural survey data** and identifying important patterns.
    - Optional extension:
      - You can **filter crops with low total yield** to focus analysis on high-performing crops:
        - **Pandas:** `total_yield_pd[total_yield_pd["Yield"] > 5000]`
        - **Polars:** `yield_summary_pl.filter(pl.col("Total_Yield") > 5000)`
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 5: Analyze Farm Efficiency

    **Objective:**
    Identify farms that are most “efficient” by combining yield and proximity information. For example, farms with high yield that are close to other farms.

    **Instructions:**
    1. Use df_farms (Pandas) or df_farms_pl (Polars)
    2. Create a new column Efficiency Score defined as:
       - `Efficiency = Yield / (1 + Distance)`
       - Use `Distance` in degrees or converted to km
    3. Sort farms by **Efficiency Score** descending
    4. Display the top 5 most efficient farms

    **Hints:**

    - In Pandas:
      ```python
      df_farms['Efficiency'] = df_farms['Yield'] / (1 + df_farms['Distance'])
      df_farms.sort_values('Efficiency', ascending=False).head(10)
      ```

    - In Polars:
      ```python
      df_farms_pl.with_columns(
          (pl.col('Yield') / (1 + pl.col('Distance'))).alias('Efficiency')
      ).sort('Efficiency', descending=True).head(10)
      ```

    **Level:** Advanced
    **Topics:** Pandas, Polars, Python, Geospatial, Data Aggregation
    """)
    return


@app.cell
def _(np, pd, pl):
    # Run this code to create a dataset for your exercise
    # Create synthetic farm dataset
    np.random.seed(42)
    df_farms = pd.DataFrame({
        "Farm_ID": range(1, 21),  # 20 farms
        "Crop": np.random.choice(["Rice", "Corn", "Sugarcane", "Vegetables"], size=20),
        "Yield": np.random.randint(800, 2000, size=20),
        "Latitude": np.random.uniform(12.5, 13.0, size=20),
        "Longitude": np.random.uniform(121.0, 121.5, size=20),
    })

    # Add synthetic distance column (in degrees)
    df_farms["Distance"] = np.random.rand(len(df_farms)) * 0.3  # ~0-33 km

    # Convert to Polars
    df_farms_pl = pl.from_pandas(df_farms)

    # Display the dataset
    df_farms.head()
    return df_farms, df_farms_pl


@app.cell
def _(df_farms):
    # --- Pandas Solution ---
    df_eff_pd = df_farms.copy()
    df_eff_pd["Efficiency"] = df_eff_pd["Yield"] / (1 + df_eff_pd["Distance"])
    df_eff_pd_sorted = df_eff_pd.sort_values("Efficiency", ascending=False)
    print("Top 5 Efficient Farms (Pandas):")
    df_eff_pd_sorted.head(5)
    return


@app.cell
def _(df_farms_pl, pl):
    # --- Polars Solution ---
    df_eff_pl = df_farms_pl.with_columns(
        (pl.col("Yield") / (1 + pl.col("Distance"))).alias("Efficiency")
    ).sort("Efficiency", descending=True)
    print("Top 5 Efficient Farms (Polars):")
    df_eff_pl.head(5)
    return


@app.cell
def _(mo):
    mo.md("""
    **Explanation of the Solution:**

    - The **Efficiency** metric combines **Yield** and **Distance** to create a single value that rewards farms with high production but penalizes those that are farther away.
    - The formula `Efficiency = Yield / (1 + Distance)`:
      - Uses **Yield** as the numerator so higher yield increases efficiency.
      - Adds 1 to the **Distance** in the denominator to avoid division by zero.
      - Penalizes farms that are farther away (higher Distance) while still keeping the metric in a reasonable range.
    - In Pandas, vectorized operations (`/` and `+`) allow fast computation for the entire column.
    - In Polars, the same calculation is done with `with_columns()` and expressions for efficiency.
    - Sorting the `Efficiency` column descending identifies the **top-performing farms** quickly.
    - Note: In this synthetic dataset, `Distance` is a random value, so the metric is illustrative. In real surveys, `Distance` could be computed as:
      - Euclidean distance to a reference point (like a market or survey office)
      - Distance to the nearest farm
      - Or using geospatial coordinates converted to kilometers
    - Displaying the **top 5 farms** helps survey analysts identify high-priority farms for logistics or further study.
    """)
    return


if __name__ == "__main__":
    app.run()
