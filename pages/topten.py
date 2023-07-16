# Sort the dataframe by "Total" column in descending order and select the top 10 records
def topten(tot,nam):
top_10 = df.sort_values(by='Total', ascending=False).head(10)
trace = go.Bar(
    x=top_10['Total'],
    y=top_10['Names'],
    orientation='h',  # Set orientation to horizontal
    marker=dict(
        color=top_10['Total'],  # Set color based on the "Total" values
        colorscale='Inferno',  # Choose a colorscale
        showscale=True,
        colorbar=dict(
            title='Total',  # Add a colorbar title
            tickfont=dict(color='#ffffff')  # Customize colorbar tick font
        )
    ),
)

data = [trace]

layout = go.Layout(
    plot_bgcolor='rgba(256,256,256,256)',
    xaxis=dict(
        title='Total',  # Add x-axis label
        title_font=dict(color='#111111'),  # Customize x-axis label color
        tickfont=dict(color='#111111')  # Customize x-axis tick font
    ),
    yaxis=dict(
        title='Names',  # Add y-axis label
        title_font=dict(color='#111111'),  # Customize y-axis label color
        tickfont=dict(color='#111111')  # Customize y-axis tick font
    ),
    title='Top 10 Characters based on Total',
    title_font=dict(color='#111111'),  # Customize title color
    margin=dict(l=150),  # Add margin to the left
)

fig = go.Figure(data=data, layout=layout)
return iplot(fig, filename='Top10Plot')
