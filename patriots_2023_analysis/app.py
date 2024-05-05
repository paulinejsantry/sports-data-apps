import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st


# cache dataset first
@st.cache_data(persist=True)
def get_data():
    """Function to retrieve data"""
    year = 2023
    data_source = f"https://github.com/nflverse/nflverse-data/releases/download/pbp/play_by_play_{year}.csv.gz"

    df = pd.read_csv(
        data_source,
        compression="gzip",
        low_memory=False,
    )

    df = df[df.season_type == "REG"]

    return df


def plot_yards_per_play(df: pd.DataFrame):
    """Function to plot average yards per game of the League vs Patriots"""
    # create a df for league averages
    df_average_league = (
        df.query('play_type in ("run", "pass")')
        .groupby(["play_type"])
        .agg({"yards_gained": "mean"})
        .reset_index()  # same as as_index=false, but more efficient in this case
        .rename(columns={"yards_gained": "average_yards_gained"})
    )

    # create a new column and set the value as "league" for all rows. will use this after combining patriots vs league average tables
    df_average_league["group"] = "league"

    # create a df for patriots averages
    df_average_patriots = (
        df.query('posteam == "NE" and play_type in ["run", "pass"]', engine="python")
        .groupby(["play_type"])
        .agg({"yards_gained": "mean"})
        .reset_index(level=0)  # same as as_index=false, but more efficient in this case
        .rename(columns={"yards_gained": "average_yards_gained"})
    )
    # create a new column and set the value as "NE" for all rows. will use this after combining patriots vs league average tables
    df_average_patriots["group"] = "NE"

    # concat the average & NE tables
    df_NE_vs_League = pd.concat([df_average_league, df_average_patriots])

    fig = px.bar(
        df_NE_vs_League,
        x="play_type",
        y="average_yards_gained",
        color="group",
        barmode="group",
        title="Average Yards per Play",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


def plot_third_down_conversion_rates(df: pd.DataFrame):
    """Function to plot 3rd down conversion rate for all teams, compared to the league average."""

    # filter to only look at 3rd down plays, because all other plays will have a value of 0
    df_third_down_plays = df[df["down"] == 3]

    df_third_down_conversions_per_team = (
        df_third_down_plays.groupby(["posteam"], as_index=False)
        .agg({"third_down_converted": "mean"})
        .reset_index(level=0)  # same as as_index=false, but more efficient in this case
        .rename(
            columns={
                "third_down_converted": "third_down_conversion_rate",
                "posteam": "Team",
            }
        )
        .sort_values("third_down_conversion_rate", ascending=False)
    )

    # store league average in a variable
    league_third_down_conversion_rate = df_third_down_plays[
        "third_down_converted"
    ].mean()

    fig = px.bar(
        df_third_down_conversions_per_team,
        x="Team",
        y="third_down_conversion_rate",
        title="Third Down Conversion Rate by Team",
    )
    fig.add_hline(
        y=league_third_down_conversion_rate,
        line_dash="dot",
        annotation_text="League Average",
        line_color="white",
    )
    st.plotly_chart(
        fig,
        use_container_width=True,
    )


def main():
    """"""
    st.markdown(
        """
    # NFL 2023 Season Insights
        """
    )

    df = get_data()
    plot_third_down_conversion_rates(df)

    st.markdown(
        """
    ## Patriots Insights
    The Patriots were *below* the League average for both passing and running yards per play   
      """
    )

    df = get_data()
    plot_yards_per_play(df)


if __name__ == "__main__":
    main()
