#for first 10 data alone
def contour_plot(HP, Attack, Defense, Sp.Atk, Sp.Def, Speed):
# Assuming you have a DataFrame named 'df' containing Pokémon data

# Prepare the Pokémon data in a 2D array or matrix format for the first 100 data points
pokemon_data = df[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].head(10).values

# Create and show the figure
fig = go.Figure()

fig.add_trace(go.Contour(
    z=pokemon_data,
    colorscale="Cividis",
))

return fig.show()
