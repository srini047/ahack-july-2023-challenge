# Radarplot of single pokemon
import plotly.graph_objects as go
from plotly.offline import iplot


def radar_plot(df, name):
    x = df[df["Names"] == name]
    data = [
        go.Scatterpolar(
            r=[
                x["HP"].values[0],
                x["Attack"].values[0],
                x["Defense"].values[0],
                x["Sp. Atk"].values[0],
                x["Sp. Def"].values[0],
                x["Speed"].values[0],
                x["HP"].values[0],
            ],
            theta=["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "HP"],
            fill="toself",
            text=df["Names"]
        )
    ]

    layout = go.Layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 250])),
        showlegend=False,
        title="Stats of {}".format(x.Names.values[0]),
    )
    fig = go.Figure(data=data, layout=layout)
    return fig
