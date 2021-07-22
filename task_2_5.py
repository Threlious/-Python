prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
print("Часть A")
for idx in range(len(prices)):
    if prices[idx] % 1 == 0:  # если сумма без копеек
        prices[idx] = f'{prices[idx]} руб 00 коп'
    elif prices[idx] % 1 != 0:  # если сумма с копейками
        kop = prices[idx] % 1 * 100  # обозначение копеек
        if kop // 10 > 1:
            prices[idx] = f'{prices[idx] // 1:.0f} руб {kop:.0f} коп'  # если копейки двузначные
        else:
            prices[idx] = f'{prices[idx] // 1:.0f} руб 0{kop:.0f} коп'  # если копейки однозначные
print(", ".join(prices))
print()
print("Часть B")
prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
print(id(prices))
prices.sort()
print(prices)
print(id(prices))
print()
print("Часть C")
prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
print(id(prices))
prices_reverse = sorted(prices, reverse=True)
print(prices_reverse)
print(id(prices_reverse))
print()
print("Часть D")
prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
prices.sort()
top_price = prices[-5:]
for idx in range(len(top_price)):
    top_price[idx] = str(top_price[idx])
print(", ".join(top_price))
