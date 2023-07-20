# import plotly.graph_objects as go
# from plotly.offline import iplot


# def heatmap_plot(df):
#     # Prepare the Pokémon data in a 2D array format
#     pokemon_data = df[["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]].values

#     # Create and show the figure
#     fig = go.Figure()

#     fig.add_trace(
#         go.Heatmap(
#             z=pokemon_data,
#             colorbar=dict(
#                 title="Stats",
#                 titleside="top",
#                 tickmode="array",
#                 tickvals=[0, 50, 100, 150, 200],
#                 ticks="outside",
#             ),
#             text=df["Names"]
#         )
#     )
#     return fig

import plotly.graph_objects as go
from plotly.offline import iplot

def heatmap_plot(df):
    # Select the top 10 ranked Pokemon based on the "Rank" column
    top_10 = df.nsmallest(10, "Rank")

    # Prepare the Pokemon data for the heatmap in a 2D array format
    pokemon_data = top_10[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].values

    # Create the figure
    fig = go.Figure()

    # Add the heatmap trace
    fig.add_trace(go.Heatmap(
        z=pokemon_data,
        colorbar=dict(
            title="Stats",
            titleside="top",
            tickmode="array",
            tickvals=[0, 50, 100, 150, 200],
            ticks="outside"
        ),
        hovertemplate="{text}",
        text=df["Names"],
        colorscale="Viridis"
    ))

    # Set the layout and display the figure
    layout = go.Layout(
        title="Heatmap of Top 10 Ranked Pokemon",
        xaxis=dict(title="Attributes"),
        yaxis=dict(title="Rank"),
    )

    fig.update_layout(layout)

    return fig
