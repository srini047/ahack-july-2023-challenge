#displot of all stats
def displot(df,c1,c2,c3,c4,c5,c6):
    hist_data = [df[c1],df[c2],df[c3],df[c4],df[c5],df[c6]]
    group_labels = list(df.iloc[:,5:11].columns)
    fig = ff.create_distplot(hist_data, group_labels, bin_size=5)
    return iplot(fig, filename='Distplot of all pokemon stats')
#average derived through img
