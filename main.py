# 1 - misol
royxat_1 = ["hello", "say", "welcome", "hi"]


transformatsiya_1 = lambda x: f"{x[0]}-{len(x)}"


natija_1 = list(map(transformatsiya_1, royxat_1))

print(f"Boshlang'ich ro'yxat: {royxat_1}")
print(f"Natija 1: {natija_1}")



# 2 - misol
royxat_2 = ["Ali Valiyev", "Bobur Yo'ldoyev", "Stive Jobs", "Bill Gates"]

def ism_familiyani_qisqartirish(to_liq_ism):
    qismlar = to_liq_ism.split()
    ism = qismlar[0]
    familiya_bosh_harfi = qismlar[1][0]
    return f"{ism} {familiya_bosh_harfi}."


natija_2 = list(map(ism_familiyani_qisqartirish, royxat_2))

print(f"Boshlang'ich ro'yxat: {royxat_2}")
print(f"Natija 2: {natija_2}")



# 3 - misol
royxat_3 = ["Ali", "Bobur", "Stive", "Santyago"]


transformatsiya_3 = lambda x: x + str(len(x))


natija_3 = list(map(transformatsiya_3, royxat_3))

print(f"Boshlang'ich ro'yxat: {royxat_3}")
print(f"Natija 3: {natija_3}")











