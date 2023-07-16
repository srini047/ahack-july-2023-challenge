def heatmap(HP, Attack, Defense, Sp. Atk, Sp. Def, Speed):
# Assuming you have a DataFrame named 'df' containing Pokémon data

# Prepare the Pokémon data in a 2D array format
pokemon_data = df[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].values

# Create and show the figure
fig = go.Figure()

fig.add_trace(go.Heatmap(
    z=pokemon_data,
    colorbar=dict(
        title="Stats",
        titleside="top",
        tickmode="array",
        tickvals=[0, 50, 100, 150, 200],
        ticks="outside"
    )
))

return fig.show()
