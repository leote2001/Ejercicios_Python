fibo = [0, 1]
i = 1
while i < 17:
    suma = fibo[i-1]+fibo[i]
    fibo.append(suma)
    print(f"{fibo[i-1]} ")
    i += 1
