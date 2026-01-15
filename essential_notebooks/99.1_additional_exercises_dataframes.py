import marimo

__generated_with = "0.19.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Exercise: Farm Typology and Survey Prioritization

    ## Context

    Agricultural survey analysis goes beyond computing simple totals or averages.
    Analysts often derive indicators, classify farms, detect unusual observations, and combine multiple signals to support decision-making.

    In this exercise, you will analyze farm survey data to help a statistical agency prioritize farms for **validation, follow-up, or deeper analysis**.

    This is a **multi-part, progressive exercise**.
    Each part builds on the outputs of the previous tasks.

    You may solve each task using **either Pandas or Polars**.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Dataset

    You are given a farm-level dataset with at least the following columns:

    - `Farm_ID`
    - `Crop`
    - `Yield`
    - `Farm_Area`
    - `Latitude`
    - `Longitude`
    - `Distance` (a derived spatial metric)

    Assume the dataset has already been loaded as:

    - `df_pd` (Pandas), or
    - `df_pl` (Polars)
    """)
    return


@app.cell
def _():
    # =============================================================================
    # Synthetic Dataset for Epic Exercise (Used by ALL sub-problems)
    # Only raw values are provided; students derive all indicators
    # =============================================================================

    import numpy as np
    import pandas as pd
    import polars as pl

    # ----------------------------
    # Reproducibility
    # ----------------------------
    np.random.seed(42)

    # ----------------------------
    # Create synthetic farm survey dataset
    # ----------------------------
    df_pd = pd.DataFrame({
        "Farm_ID": range(1, 31),  # 30 farms
        "Crop": np.random.choice(
            ["Rice", "Corn", "Sugarcane", "Vegetables"], size=30
        ),
        "Farm_Area": np.random.uniform(1.0, 5.0, size=30),  # hectares
        "Production": np.random.randint(800, 5000, size=30),  # total output in kg
        "Latitude": np.random.uniform(12.5, 13.0, size=30),
        "Longitude": np.random.uniform(121.0, 121.5, size=30),
    })

    # ----------------------------
    # Convert to Polars
    # ----------------------------
    df_pl = pl.from_pandas(df_pd)

    # ----------------------------
    # Preview dataset
    # ----------------------------
    df_pd.head()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Mini-Problem 1: Deriving Productivity Indicators

    ### Objective
    Create new variables that better represent farm productivity and can be used for further analysis.

    ### Tasks
    1. Create a productivity indicator that accounts for both output and land size.
       - *(Yield_per_Area = Yield / Farm_Area)*
    2. Compute a reference value that represents the typical yield across all farms.
    3. Using this reference value, flag farms that perform better than the typical farm.
    4. Inspect the newly created columns to ensure they make sense.

    ### Expected Outcome
    The dataset now contains derived indicators that describe **relative productivity**, not just raw production.
    """)
    return


@app.cell
def _():
    # Write your solution here
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Mini-Problem 2: Developing Farm Typologies

    ### Objective
    Classify farms into meaningful types using both productivity and land size information.

    ### Tasks
    1. Identify suitable reference values that describe:
       - Typical yield
       - Typical farm size
    2. Use these references to group farms into distinct categories that reflect:
       - Differences in yield performance
       - Differences in land area
    3. Assign each farm to exactly one category.
    4. Review how farms are distributed across the resulting types.

    ### Expected Outcome
    Farms are transformed from individual records into members of interpretable groups.
    """)
    return


@app.cell
def _():
    # Write your solution here
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Mini-Problem 3: Identifying Unusual Farms

    ### Objective
    Detect farms that differ strongly from common productivity patterns.

    ### Tasks
    1. Use the productivity indicator created earlier to define what “typical” performance looks like.
    2. Create a metric that measures how far each farm deviates from this typical performance.
       - *(Outlier_Score = absolute difference from the reference value)*
    3. Rank farms by this deviation measure.
    4. Examine the farms with the largest deviations.

    ### Expected Outcome
    You identify farms that may represent:
    - Exceptional performance
    - Data quality issues
    - Cases requiring validation
    """)
    return


@app.cell
def _():
    # Write your solution here
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Mini-Problem 4: Evaluating Performance Within Crop Groups

    ### Objective
    Assess farm performance relative to other farms growing the same crop.

    ### Tasks
    1. Group farms by crop type.
    2. Compute a crop-level benchmark for productivity.
    3. Compare each farm’s productivity against its crop benchmark.
       - *(Relative_Performance = farm productivity / crop benchmark)*
    4. Interpret which farms perform above or below expectations for their crop.

    ### Expected Outcome
    Farm performance is interpreted **in context**, accounting for crop-specific differences.
    """)
    return


@app.cell
def _():
    # Write your solution here
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Mini-Problem 5: Constructing a Survey Priority Index (Capstone)

    ### Objective
    Combine multiple indicators into a single metric that can guide survey prioritization.

    ### Tasks
    1. Scale yield values so they are comparable across farms.
       - *(Normalized_Yield = Yield / maximum Yield)*
    2. Combine multiple indicators into a single index:
       - Productivity relative to crop peers
       - Degree of deviation from typical productivity
       - Overall yield level
    3. Create a composite score using a weighted combination.
       - *(Survey_Priority_Index = 0.4 × Relative_Performance
         + 0.4 × Outlier_Score
         + 0.2 × Normalized_Yield)*
    4. Rank farms by this index and identify the top candidates for follow-up.
    """)
    return


@app.cell
def _():
    # Write your solution here
    return


if __name__ == "__main__":
    app.run()
