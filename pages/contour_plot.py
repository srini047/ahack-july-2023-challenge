import plotly.graph_objects as go
from plotly.offline import iplot

#for First 10 data alone
def contour_plot(df):
    # Prepare the Pokémon data in a 2D array or matrix format for the first 100 data points
    # pokemon_data = df[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].head(10).values

    # # Create and show the figure
    # fig = go.Figure()

    # fig.add_trace(go.Contour(
    #     z=pokemon_data,
    #     colorscale='Electric',
    # ))

    # return fig

    fig = go.Figure(data =
    go.Contour(
        z=[[10, 10.625, 12.5, 15.625, 20],
           [5.625, 6.25, 8.125, 11.25, 15.625],
           [2.5, 3.125, 5., 8.125, 12.5],
           [0.625, 1.25, 3.125, 6.25, 10.625],
           [0, 0.625, 2.5, 5.625, 10]],
        contours=dict(
            start=0,
            end=8,
            size=2,
        ),
        text=df["Names"]
    ))

    return fig
