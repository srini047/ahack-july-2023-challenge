import plotly.graph_objects as go
from plotly.offline import iplot
def scatter_plot3d(df,name1,name2,name3):
# Select the attributes for the 3D scatter plot
x = df[name1]
y = df[name2]
z = df[name3]

# Create the trace for the 3D scatter plot
trace = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=5,
        color=df["Total"],
        colorscale='Viridis',
        showscale=True,
        colorbar=dict(
            title='Total',
            tickfont=dict(color='#111111'),
        ),
        opacity=0.8
    ),
    text=df["Names"]
)

data = [trace]

layout = go.Layout(
    plot_bgcolor='rgba(0,0,0,1)',
    scene=dict(
        xaxis=dict(title='Attack', titlefont=dict(color='#111111')),
        yaxis=dict(title='Defense', titlefont=dict(color='#111111')),
        zaxis=dict(title='Speed', titlefont=dict(color='#111111'))
    ),
    title='3D Scatter Plot of Attack, Defense, and Speed',
    title_font=dict(color='#111111')
)

fig = go.Figure(data=data, layout=layout)
return iplot(fig, filename='3DScatterPlot')
