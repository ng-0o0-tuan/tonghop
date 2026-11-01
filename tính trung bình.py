def tinh_trung_binh(a, b, c):
    return (a + b + c)/3
a, b, c = (int (input("nhap ba so a: ")), int(input("nhap ba so b: ")), int(input("nhap ba so c: ")))
x = tinh_trung_binh(a, b, c)
print("ket_qua:", round(x, 2))