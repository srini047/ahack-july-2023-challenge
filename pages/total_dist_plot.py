# Displot of all stats
import plotly.graph_objects as go
from plotly.offline import iplot
import plotly.figure_factory as ff


colors = ['#393E46', '#2BCDC1', '#F66095', '#835AF1', '#7FA6EE', '#B8F7D4']

# HP, Attack, Defense, Sp. Atk, Sp. Def, Speed
def dist_plot(df, c1, c2, c3, c4, c5, c6):
    hist_data = [df[c1], df[c2], df[c3], df[c4], df[c5], df[c6]]
    group_labels = list(df.iloc[:, 5:11].columns)
    fig = ff.create_distplot(hist_data, group_labels, bin_size=5, colors=colors)
    # iplot(fig, filename="Distplot of all pokemon stats")

    return fig


# average derived through img
