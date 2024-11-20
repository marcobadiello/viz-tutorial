import polars as pl
import altair as alt
import streamlit as st

data_url = "https://www.dei.unipd.it/~ceccarello/data/gapminder.csv"

gapminder = pl.read_csv(data_url).filter(pl.col("year")==2007)

#st.write(gapminder)

chart = (
    alt.Chart(gapminder)
    .mark_circle()
    .encode(
        alt.X("gdpPercap").scale(type="log"),
        alt.Y("lifeExp"),
        alt.Color("continent"),
        #alt.Size("pop")
        alt.Tooltip(["country","pop"])
    )
)

st.altair_chart(chart,
         use_container_width=True)

barchart = (
    alt.Chart(gapminder)
    .mark_bar()
    .encode(
        alt.X("pop",aggregate="sum",title="Popolazione totale"),
        alt.Y("continent",sort="-x",title="Continente")
        
    )
)
st.altair_chart(barchart,
         use_container_width=True)