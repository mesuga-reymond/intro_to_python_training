import marimo

__generated_with = "0.19.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Labor Productivity Analysis

    This notebook will show examples to:
    - Compute labor productivity
    - Filter and classify farms
    - Loop through averages
    - Use lambda functions
    - Visualize data
    """)
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    return (pd,)


@app.cell
def _(mo):
    mo.md("""
    ## Dataset Description

    The dataset collected from farms includes:

    - Farm_ID – Unique farm identifier
    - Crop – Crop planted
    - Labor_days – Total labor days spent for the crop
    - Production_tons – Total production (tons)

    We will calculate labor productivity as production per labor day.
    """)
    return


@app.cell
def _(pd):
    # Run this cell block to define the dataset
    data = {
        "Farm_ID": ["F101", "F102", "F103", "F104", "F105", "F106",
                    "F107", "F108", "F109", "F110", "F111", "F112"],
        "Crop": ["Tomato", "Eggplant", "Cassava", "Mango", "Tomato", "Cassava",
                 "Mango", "Eggplant", "Tomato", "Mango", "Cassava", "Eggplant"],
        "Labor_days": [15, 18, 22, 10, 12, 20, 8, 25, 17, 9, 23, 19],
        "Production_tons": [4.5, 5.0, 6.0, 3.0, 4.0, 5.5, 3.5, 5.2, 4.8, 3.2, 6.3, 4.9]
    }

    df = pd.DataFrame(data)
    df
    return


@app.cell
def _(mo):
    mo.md("""
    ### Task 1: Data Exploration

    1. Display the first 5 rows of the dataset.
    2. Display the data types of each column.
    3. Display summary statistics for numerical columns.
    """)
    return


@app.cell
def _():
    # Write your solution here
    return


@app.cell
def _(mo):
    mo.md("""
    ### Task 2: Labor Productivity

    1. Compute **Labor Productivity** = Production_tons ÷ Labor_days
    2. Create a new column `Labor_Productivity` rounded to **3 decimal places**
    """)
    return


@app.cell
def _():
    # Write your solution here
    return


@app.cell
def _(mo):
    mo.md("""
    ### Task 3: Identify Low Productivity Farms

    1. Filter farms with Labor_Productivity < 0.25
    2. Display the following columns:
       - Farm_ID
       - Crop
       - Labor_days
       - Production_tons
       - Labor_Productivity
    3. Add a short interpretation:
       > "These farms may need improved labor planning or mechanization."
    """)
    return


@app.cell
def _():
    # Write your solution here
    return


@app.cell
def _(mo):
    mo.md("""
    ### Task 4: Average Labor Productivity per Crop

    1. Compute the **average Labor_Productivity** for each crop using `groupby`.
    2. Sort from **highest to lowest productivity**.
    """)
    return


@app.cell
def _():
    # Write your solution here
    return


@app.cell
def _(mo):
    mo.md("""
    ### Task 5: Advisory Messages Using Loops

    Using the average Labor_Productivity per crop, print advisory messages:

    - **High productivity**: ≥ 0.5 tons/day
    - **Moderate productivity**: 0.3 – 0.49 tons/day
    - **Low productivity**: < 0.3 tons/day
    """)
    return


@app.cell
def _():
    # Write your solution here
    return


@app.cell
def _(mo):
    mo.md("""
    ### Task 6: Productivity Classification Using Lambda

    1. Create a new column `Productivity_Class`
    2. Use a lambda function:
       - "High" if Labor_Productivity ≥ 0.4
       - "Low" otherwise
    """)
    return


@app.cell
def _():
    # Write your solution here
    return


@app.cell
def _(mo):
    mo.md("""
    ### Task 7: Data Visualization

    A. **Bar Chart** – Average Labor_Productivity per crop
    B. **Scatter Plot** – Labor_days vs Production_tons, color by Crop

    Add axes labels and titles.
    """)
    return


@app.cell
def _():
    # Write your solution here
    return


@app.cell
def _(mo):
    mo.md("""
    ### Reflection Questions

    1. Which crop has the highest labor productivity?
    2. Does increasing labor always lead to higher production?
    3. How can this analysis help farmers optimize labor?
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    # Write your answers here!
    """)
    return


if __name__ == "__main__":
    app.run()
