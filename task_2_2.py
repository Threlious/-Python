weather_upd = []
weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(weather))
weather_upd.append(weather[0])
weather_upd.append(f'"0{weather[1]}"')
weather_upd.append(weather[2])
weather_upd.append(f'"{weather[3]}"')
weather_upd.append(" ".join(weather[4:8]))
weather_upd.append(f'"+0{int(weather[8])}"')
weather_upd.append(weather[9])
print(" ".join(weather_upd))
print(id(weather_upd))
