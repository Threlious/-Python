weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(weather))
for idx in range(len(weather)):
    if weather[idx].isdigit():
        weather[idx] = int(weather[idx])
        weather[idx] = f'"{weather[idx]:02}"'
    elif "+" in weather[idx]:
        weather[idx] = int(weather[idx])
        weather[idx] = f"{weather[idx]:02}"
        weather[idx] = str(weather[idx])
        weather[idx] = f'"+{weather[idx]}"'
    elif "-" in weather[idx]:
        weather[idx] = int(weather[idx])
        weather[idx] = f'"{weather[idx]:03}"'
print(" ".join(weather))
print(id(weather))
