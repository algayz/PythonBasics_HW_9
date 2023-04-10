min_population = df['population'].min()

filtered_df2 = df[df['population'] == min_population]

max_households = filtered_df2['households'].max()

print("Максимальное значение households в зоне с минимальным значением population: ", max_households)