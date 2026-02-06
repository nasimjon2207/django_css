#------------------------------------------------------------------------------------
#(1.1)13-masala
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# d=int(input("d="))
# try:
#     print ( ((1-(a+2.9*b))*2/(a*b-d-1.45))  -  ((c-a)/d) / (a*(b+c**2)) + a/(1+2/c) )
# except ZeroDivisionError:
#     print("Nolga bo’lish mumkin bo’lmagani sababli berilgan qiymatlar bilan ifodaning qiymatini hisoblab bo’lmaydi")

#------------------------------------------------------------------------------------

#(1.2)13-masala
# import math
# x=int(input("x="))
# y=int(input("y="))
# z=int(input("z="))

# try:
#     print((((1-math.pow(((x+2.9*y)**2),1/3)*math.e**(x-y))) / abs(x*y-z-1.45)+1.2*10**5) - (math.log(abs(x-z)))/(z+((math.sin(math.pi-y))**2/2)))
# except ZeroDivisionError:
#     print("mahraj nolga teng bo'lganda qiymatni hisoblab bo'lmaydi!5")

#------------------------------------------------------------------------------------

#(1.3)13-masala
# import math

# s=int(input("silindr yon sirti yuzasini kiriting! s= "))
# q=int(input("asosining yuzini kiriting! q= "))
# h=s/2*math.pi*q
# v=(s*q**1/2)/2*math.pi**1/2

# try:
#     print("h=",h," ","v=",v)
    
# except ZeroDivisionError:
#     print("q=0 ga teng bo'lishi mumkin emas!")

#------------------------------------------------------------------------------------

#(1.4.1)13-masala
# def rectangle(r1, r2):
#     x1, y1, x2, y2 = r1
#     x3, y3, x4, y4 = r2
#     left_x = max(x1, x3)
#     bottom_y = max(y1, y3)
#     right_x = min(x2, x4)
#     top_y = min(y2, y4)
#     if left_x < right_x and bottom_y < top_y:
#         return (left_x, bottom_y), (right_x, top_y)
#     else:
#         return None

# rect1 = (1, 1, 5, 5)
# rect2 = (3, 2, 6, 4)

# result = rectangle(rect1, rect2)

# if result:
#     print("Umumiy qism mavjud.")
#     print("Chap quyi burchak:", result[0])
#     print("O‘ng yuqori burchak:", result[1])
# else:
#     print("Umumiy qism mavjud emas.")

#------------------------------------------------------------------------------------

#(1.4.2)13-masala
# def burj_aniqlash(d, n):
#     if (n == 3 and d >= 22) or (n == 4 and d <= 21):
#         return "Hamal"
#     elif (n == 4 and d >= 22) or (n == 5 and d <= 21):
#         return "Savr"
#     elif (n == 5 and d >= 22) or (n == 6 and d <= 21):
#         return "Egizaklar"
#     elif (n == 6 and d >= 22) or (n == 7 and d <= 21):
#         return "Qisqichbaqa"
#     elif (n == 7 and d >= 22) or (n == 8 and d <= 21):
#         return "Sher"
#     elif (n == 8 and d >= 22) or (n == 9 and d <= 21):
#         return "Parizod"
#     elif (n == 9 and d >= 22) or (n == 10 and d <= 21):
#         return "Tarozi"
#     elif (n == 10 and d >= 22) or (n == 11 and d <= 21):
#         return "Chayon"
#     elif (n == 11 and d >= 22) or (n == 12 and d <= 21):
#         return "O‘qotar"
#     elif (n == 12 and d >= 22) or (n == 1 and d <= 21):
#         return "Tog‘ echkisi"
#     elif (n == 1 and d >= 22) or (n == 2 and d <= 21):
#         return "Qovg‘a"
#     elif (n == 2 and d >= 22) or (n == 3 and d <= 21):
#         return "Baliq"
#     else:
#         return "Noto‘g‘ri sana kiritildi"
# d = int(input("Kunni kiriting: "))
# n = int(input("Oyni kiriting: "))

# print("Sizning burjingiz:", burj_aniqlash(d, n))

#------------------------------------------------------------------------------------

#(1.5.1)13-masala
# def yigindi_hisobla(n):
#     a = 1
#     b = 1
#     S = a * b 

#     for k in range(2, n + 1):
#         a_new = a + b
#         b_new = 2 * a * a + b
#         a = a_new
#         b = b_new
#         S += a * b
#     return S
# n = int(input("n ni kiriting: "))
# natija = yigindi_hisobla(n)
# print("Yig‘indi =", natija)

#------------------------------------------------------------------------------------

#(1.5.2)13-masala
# import math
# s=0
# n=int(input("n="))
# k=int(input("k="))
# x=int(input("x="))
# for i in range(1,n+1):
#     for j in range(1,k+1):
#         s=s+(-1)**i*(x**j+j**(1/i))/(math.exp(j)+math.log(i+j))
# print(s)

#------------------------------------------------------------------------------------

#(1.5.3)13-masala
# k = 1  
# max_juft = None

# while True:
#     a_k = int(input(f"a{k} = "))
#     if a_k == 0:
#         break
#     if a_k % 2 == 0:       # juft bo'lsa
#         if max_juft is None or a_k > max_juft:
#             max_juft = a_k
#     k += 1
# if max_juft is None:
#     print("Juft son yo'q")
# else:
#     print("Juftlar ichida eng kattasi =", max_juft)


#------------------------------------------------------------------------------------

#(1.5)13-masala
# import math

# s=int(input("silindr yon sirti yuzasini kiriting! s= "))
# q=int(input("asosining yuzini kiriting! q= "))
# h=s/2*math.pi*q
# v=(s*q**1/2)/2*math.pi**1/2

# try:
#     print(h,v)
    
# except ZeroDivisionError:
#     print("q=0 ga teng bo'lishi mumkin emas!")

#------------------------------------------------------------------------------------

#(1.6)13-masala
# def massiv_ozgartir(A):
#     if A[0] < 0:
#         m = min(A)
#         A = [x * m for x in A]
#     elif A[0] > 0:
#         M = max(A)
#         A = [x * M for x in A]
#     # A[0] == 0 bo‘lsa, o‘zgarmaydi
#     return A
# n = int(input("n ni kiriting: "))
# A = list(map(float, input("Massiv elementlarini kiriting: ").split()))

# A = massiv_ozgartir(A)

# print("Natijaviy massiv:")
# print(A)

#------------------------------------------------------------------------------------

#(1.7)13-masala
# n, m = map(int, input("n va m = ").split())
# A = []
# print("Matritsa elementlarini kiriting (har bir satr alohida qatorda):")
# for i in range(n):
#     row = list(map(float, input().split()))
#     A.append(row)
# max_val = A[0][0]
# min_val = A[0][0]
# imax = 0  
# imin = 0  
# for i in range(n):
#     for j in range(m):
#         if A[i][j] > max_val:
#             max_val = A[i][j]
#             imax = i
#         if A[i][j] < min_val:
#             min_val = A[i][j]
#             imin = i
# if imax != imin:
#     A[imax], A[imin] = A[imin], A[imax]
# print("Natijaviy matritsa:")
# for i in range(n):
#     for j in range(m):
#         print(int(A[i][j]), end=" ")
#     print()

#------------------------------------------------------------------------------------

#(1.8)13-masala
# def latin_to_kiril(S):
#     lugat = {
#         'a': 'а', 'b': 'б', 'd': 'д', 'e': 'е', 'f': 'ф',
#         'g': 'г', 'h': 'ҳ', 'i': 'и', 'j': 'ж', 'k': 'к',
#         'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п',
#         'q': 'қ', 'r': 'р', 's': 'с', 't': 'т',
#         'u': 'у', 'v': 'в', 'x': 'х', 'y': 'й', 'z': 'з',

#         'A': 'А', 'B': 'Б', 'D': 'Д', 'E': 'Е', 'F': 'Ф',
#         'G': 'Г', 'H': 'Ҳ', 'I': 'И', 'J': 'Ж', 'K': 'К',
#         'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О', 'P': 'П',
#         'Q': 'Қ', 'R': 'Р', 'S': 'С', 'T': 'Т',
#         'U': 'У', 'V': 'В', 'X': 'Х', 'Y': 'Й', 'Z': 'З'
#     }

#     natija = ""
#     for belgi in S:
#         if belgi in lugat:
#             natija += lugat[belgi]
#         else:
#             natija += belgi

#     return natija
# S = input("Matn kiriting: ")
# print("Natija:")
# print(latin_to_kiril(S))

#------------------------------------------------------------------------------------

#(1.10)13-masala
# birlik = {
#     1: "bir",
#     2: "ikki",
#     3: "uch",
#     4: "to'rt",
#     5: "besh",
#     6: "olti",
#     7: "yetti",
#     8: "sakkiz",
#     9: "to'qqiz"
# }
# onlik = {
#     1: "o'n",
#     2: "yigirma",
#     3: "o'ttiz",
#     4: "qirq",
#     5: "ellik",
#     6: "oltmish",
#     7: "yetmish",
#     8: "sakson",
#     9: "to'qson"
# }
# def f(n):
#     d1 = n // 10 
#     d2 = n % 10  

#     if d2 == 0:
#         s = onlik[d1]   
#     else:
#         s = onlik[d1] + " " + birlik[d2]  
#     return len(s), s
# for i in range(10, 100):
#     cnt, word = f(i)
#     print(f"{i} → \"{word}\" → {cnt}")

#------------------------------------------------------------------------------------

#(1.18)13-masala
# avtomobillar = [
#     {
#         "marka": "Chevrolet Cobalt",
#         "rang": "Oq",
#         "seriya": "AA123456",
#         "qayd": "01A123AA",
#         "yil": 2015,
#         "baho": 12000
#     },
#     {
#         "marka": "Malibu",
#         "rang": "Qora",
#         "seriya": "BB654321",
#         "qayd": "10B456BB",
#         "yil": 2020,
#         "baho": 22000
#     },
#     {
#         "marka": "Lacetti",
#         "rang": "Kumush",
#         "seriya": "CC789123",
#         "qayd": "50C789CC",
#         "yil": 2012,
#         "baho": 9000
#     }
# ]
# from datetime import datetime
# n = int(input("Necha yildan ortiq bo‘lgan avtomobillarni topish kerak? "))

# joriy_yil = datetime.now().year
# print("\nMos keluvchi avtomobillar:\n")

# for avto in avtomobillar:
#     yosh = joriy_yil - avto["yil"]
#     if yosh > n:
#         print(f"Markasi: {avto['marka']}")
#         print(f"Rangi: {avto['rang']}")
#         print(f"Seriya nomeri: {avto['seriya']}")
#         print(f"Qayd raqami: {avto['qayd']}")
#         print(f"Ishlab chiqarilgan yili: {avto['yil']}")
#         print(f"Bahosi: {avto['baho']} $")
#         print("-" * 30)
#     else:
#         print("Bunday yildagi avtomobil topilmadi!")


#------------------------------------------------------------------------------------

#(1.19.1)13-masala
# from datetime import datetime
# sana_str = input("Sanani kiriting (YYYY-MM-DD): ")
# sana = datetime.strptime(sana_str, "%Y-%m-%d")
# hafta = ["Dush", "Sesh", "Chor", "Pay", "Jum", "Shan", "Yak"]
# kun = sana.day
# oy = sana.month
# yil = sana.year
# hafta_kuni = hafta[sana.weekday()]
# print(f"Kun: {kun:02d}")
# print(f"Hafta kuni: {hafta_kuni}")
# print(f"Oy: {oy:02d}")
# print(f"Yil: {yil:04d}")

#------------------------------------------------------------------------------------

#Olimpiada masalasi 119.
# def ekub(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
# N = int(input("N = "))
# A = list(map(int, input("Sonlarni kiriting: ").split()))
# g = A[0]
# for i in range(1, N):
#     g = ekub(g, A[i])
# print("Natija (EKUB) =", g)

#------------------------------------------------------------------------------------

# grafiklar bilan ishlash 13
# import turtle

# win = turtle.Screen()
# win.title("1.9.1.d - Budilnik soat")

# t = turtle.Turtle()
# t.speed(3)

# # === KATTA DOIRA ===
# t.penup()
# t.goto(0, -100)
# t.pendown()
# t.circle(100)

# # === TEPADAGI QOPQOQ === (yarim doira)
# t.penup()
# t.goto(-40, 100)
# t.setheading(0)
# t.pendown()
# t.circle(40, 180)

# # === QOPQOQ ASOSI (tekis chiziq) ===
# t.penup()
# t.goto(-40, 100)
# t.setheading(0)
# t.pendown()
# t.forward(80)

# # === MIL: O'NGGA ===
# t.penup()
# t.goto(0, 0)
# t.setheading(0)
# t.pendown()
# t.forward(60)

# # O'q uchi
# t.right(150)
# t.forward(10)
# t.back(10)
# t.left(300)
# t.forward(10)
# t.back(10)

# # === MIL: YUQORIGA ===
# t.penup()
# t.goto(0, 0)
# t.setheading(90)
# t.pendown()
# t.forward(60)

# # O'q uchi
# t.right(150)
# t.forward(10)
# t.back(10)
# t.left(300)
# t.forward(10)
# t.back(10)

# # === OYOQLAR ===
# t.penup()
# t.goto(-40, -100)
# t.setheading(-60)
# t.pendown()
# t.forward(40)

# t.penup()
# t.goto(40, -100)
# t.setheading(-120)
# t.pendown()
# t.forward(40)

# t.hideturtle()
# turtle.done()
#------------------------------------------------------------------------------------
#interfeys bilan ishlash amallari
# import tkinter as tk
# import math

# def ildiz_soni():
#     try:
#         a = float(entry_a.get())
#         b = float(entry_b.get())
#         c = float(entry_c.get())
#         D = b*b - 4*a*c
        
#         if D < 0:
#             label_natija.config(text="Ildiz yo'q (D<0)", fg="red")
#         elif D == 0:
#             label_natija.config(text="1 ta ildiz (D=0)", fg="black")
#         else:
#             label_natija.config(text="2 ta ildiz (D>0)", fg="black")
#     except:
#         label_natija.config(text="Xato! a, b, c ni kiriting", fg="red")

# def ildiz_topish():
#     try:
#         a = float(entry_a.get())
#         b = float(entry_b.get())
#         c = float(entry_c.get())
#         D = b*b - 4*a*c
        
#         if D < 0:
#             label_natija.config(text="Ildiz yo'q (D<0)", fg="red")
#         else:
#             x1 = (-b + math.sqrt(D)) / (2*a)
#             x2 = (-b - math.sqrt(D)) / (2*a)
#             label_natija.config(text=f"x1={x1:.2f}, x2={x2:.2f}", fg="black")
#     except:
#         label_natija.config(text="Xato! a, b, c ni kiriting", fg="red")

# def uchburchak_yuzi():
#     try:
#         a = float(entry_a.get())
#         b = float(entry_b.get())
#         c = float(entry_c.get())
        
#         p = (a + b + c) / 2
#         S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        
#         label_natija.config(text=f"Uchburchak yuzi: {S:.2f}", fg="black")
#     except:
#         label_natija.config(text="Xato! a, b, c ni kiriting", fg="red")

# oyna = tk.Tk()
# oyna.title("Kvadrat tenglama + Uchburchak")

# tk.Label(oyna, text="a:").pack()
# entry_a = tk.Entry(oyna)
# entry_a.pack()

# tk.Label(oyna, text="b:").pack()
# entry_b = tk.Entry(oyna)
# entry_b.pack()

# tk.Label(oyna, text="c: (uchala funksiya uchun)").pack()
# entry_c = tk.Entry(oyna)
# entry_c.pack()

# tk.Button(oyna, text="Ildizlar soni", command=ildiz_soni).pack(pady=4)
# tk.Button(oyna, text="Ildizlarni topish", command=ildiz_topish).pack(pady=4)
# tk.Button(oyna, text="Uchburchak yuzi", command=uchburchak_yuzi).pack(pady=4)

# label_natija = tk.Label(oyna, text="", font=("Arial", 12))
# label_natija.pack(pady=10)

# oyna.mainloop()

#------------------------------------------------------------------------------------

# import tkinter as tk
# import math

# def ildiz_soni():
#     try:
#         a = float(q_a.get())
#         b = float(q_b.get())
#         c = float(q_c.get())
#         D = b*b - 4*a*c
        
#         if D < 0:
#             label_natija.config(text="Kvadrat tenglama: ildiz yo'q")
#         elif D == 0:
#             label_natija.config(text="Kvadrat tenglama: 1 ta ildiz")
#         else:
#             label_natija.config(text="Kvadrat tenglama: 2 ta ildiz")
#     except:
#         label_natija.config(text="Kvadrat uchun xato!")

# def ildiz_topish():
#     try:
#         a = float(q_a.get())
#         b = float(q_b.get())
#         c = float(q_c.get())
#         D = b*b - 4*a*c
        
#         if D < 0:
#             label_natija.config(text="Ildiz yo'q")
#         else:
#             x1 = (-b + math.sqrt(D)) / (2*a)
#             x2 = (-b - math.sqrt(D)) / (2*a)
#             label_natija.config(text=f"x1={x1:.2f}, x2={x2:.2f}")
#     except:
#         label_natija.config(text="Kvadrat uchun xato!")

# def uchburchak_yuzi():
#     try:
#         a = float(u_a.get())
#         b = float(u_b.get())
#         c = float(u_c.get())
#         p = (a+b+c)/2
#         S = math.sqrt(p*(p-a)*(p-b)*(p-c))
#         label_natija.config(text=f"Uchburchak yuzi: {S:.2f}")
#     except:
#         label_natija.config(text="Uchburchak uchun xato!")

# def tort_perimetr():
#     try:
#         a = float(t_a.get())
#         b = float(t_b.get())
#         P = 2*(a+b)
#         label_natija.config(text=f"To'g'ri to'rtburchak perimetri: {P:.2f}")
#     except:
#         label_natija.config(text="To'rtburchak uchun xato!")

# oyna = tk.Tk()
# oyna.title("Geometriya + Kvadrat tenglama")

# # === KVADRAT BLOK ===
# tk.Label(oyna, text="Kvadrat tenglama (a,b,c)").pack()

# q_a = tk.Entry(oyna); q_a.pack()
# q_b = tk.Entry(oyna); q_b.pack()
# q_c = tk.Entry(oyna); q_c.pack()

# tk.Button(oyna, text="Ildizlar soni", command=ildiz_soni).pack(pady=3)
# tk.Button(oyna, text="Ildizlarni topish", command=ildiz_topish).pack(pady=3)

# # === UCHBURCHAK BLOK ===
# tk.Label(oyna, text="Uchburchak (a,b,c)").pack(pady=5)

# u_a = tk.Entry(oyna); u_a.pack()
# u_b = tk.Entry(oyna); u_b.pack()
# u_c = tk.Entry(oyna); u_c.pack()

# tk.Button(oyna, text="Uchburchak yuzi", command=uchburchak_yuzi).pack(pady=3)

# # === TO'RTBURCHAK BLOK ===
# tk.Label(oyna, text="To'g'ri to'rtburchak (a,b)").pack(pady=5)

# t_a = tk.Entry(oyna); t_a.pack()
# t_b = tk.Entry(oyna); t_b.pack()

# tk.Button(oyna, text="Perimetri", command=tort_perimetr).pack(pady=3)

# label_natija = tk.Label(oyna, text="", font=("Arial", 12))
# label_natija.pack(pady=10)

# oyna.mainloop()

# import tkinter as tk
# import math

# oyna = tk.Tk()
# oyna.title("Geometriya + Kvadrat Tenglama")

# oyna.geometry("850x600")
# oyna.minsize(700, 500)

# fon = "#d7e8ff"
# blok_fon = "#ffffff"
# btn = "#4a8df7"
# btn_hover = "#2f6be0"
# natija_fon = "#ffe993"

# oyna.config(bg=fon)

# container = tk.Frame(oyna, bg=fon)
# container.pack(fill="both", expand=True, padx=20, pady=20)


# def hover_in(e): e.widget.config(bg=btn_hover)
# def hover_out(e): e.widget.config(bg=btn)


# # === Kvadrat block ===
# frame_kv = tk.Frame(container, bg=blok_fon, padx=12, pady=12,
#                     highlightbackground="#5d7fa5", highlightthickness=2)
# frame_kv.pack(fill="x", pady=8)

# tk.Label(frame_kv, text="Kvadrat tenglama (a, b, c)", bg=blok_fon,
#          font=("Arial", 16, "bold")).pack(pady=4)

# q_a = tk.Entry(frame_kv, width=23, font=("Arial", 13)); q_a.pack(pady=3)
# q_b = tk.Entry(frame_kv, width=23, font=("Arial", 13)); q_b.pack(pady=3)
# q_c = tk.Entry(frame_kv, width=23, font=("Arial", 13)); q_c.pack(pady=3)


# def ildiz_soni():
#     try:
#         a=float(q_a.get()); b=float(q_b.get()); c=float(q_c.get())
#         if a==0:
#             label_natija.config(text="Kvadrat emas!")
#             return
#         D=b*b-4*a*c
#         if D<0: nat="Ildiz yo'q"
#         elif D==0: nat="1 ta ildiz"
#         else: nat="2 ta ildiz"
#         label_natija.config(text=nat)
#     except:
#         label_natija.config(text="Kvadrat uchun xato!")


# def ildiz_topish():
#     try:
#         a=float(q_a.get()); b=float(q_b.get()); c=float(q_c.get())
#         if a==0:
#             label_natija.config(text="Kvadrat emas!")
#             return
#         D=b*b-4*a*c
#         if D<0:
#             label_natija.config(text="Ildiz yo'q")
#         elif D==0:
#             x=-b/(2*a)
#             label_natija.config(text=f"x={x:.2f}")
#         else:
#             x1=(-b+math.sqrt(D))/(2*a)
#             x2=(-b-math.sqrt(D))/(2*a)
#             label_natija.config(text=f"x1={x1:.2f}, x2={x2:.2f}")
#     except:
#         label_natija.config(text="Kvadrat uchun xato!")


# btn1 = tk.Button(frame_kv, text="Ildizlar soni", width=18, font=("Arial", 13),
#                  bg=btn, fg="white", command=ildiz_soni)
# btn2 = tk.Button(frame_kv, text="Ildizlarni topish", width=18, font=("Arial", 13),
#                  bg=btn, fg="white", command=ildiz_topish)

# btn1.pack(pady=3)
# btn2.pack(pady=3)

# for b in (btn1, btn2):
#     b.bind("<Enter>", hover_in)
#     b.bind("<Leave>", hover_out)


# # === Uchburchak block ===
# frame_uch = tk.Frame(container, bg=blok_fon, padx=12, pady=12,
#                      highlightbackground="#5d7fa5", highlightthickness=2)
# frame_uch.pack(fill="x", pady=8)

# tk.Label(frame_uch, text="Uchburchak (a, b, c)", bg=blok_fon,
#          font=("Arial", 16, "bold")).pack(pady=4)

# u_a = tk.Entry(frame_uch, width=23, font=("Arial", 13)); u_a.pack(pady=3)
# u_b = tk.Entry(frame_uch, width=23, font=("Arial", 13)); u_b.pack(pady=3)
# u_c = tk.Entry(frame_uch, width=23, font=("Arial", 13)); u_c.pack(pady=3)


# def uch_yuz():
#     try:
#         a=float(u_a.get()); b=float(u_b.get()); c=float(u_c.get())
#         if a+b<=c or a+c<=b or b+c<=a:
#             label_natija.config(text="Uchburchak bo'lmaydi!")
#             return
#         p=(a+b+c)/2
#         S=math.sqrt(p*(p-a)*(p-b)*(p-c))
#         label_natija.config(text=f"Yuzi: {S:.2f}")
#     except:
#         label_natija.config(text="Uchburchak uchun xato!")


# btn3 = tk.Button(frame_uch, text="Yuzini hisoblash", width=18,
#                  font=("Arial", 13), bg=btn, fg="white", command=uch_yuz)
# btn3.pack(pady=3)
# btn3.bind("<Enter>", hover_in)
# btn3.bind("<Leave>", hover_out)


# # === To'rtburchak block ===
# frame_tort = tk.Frame(container, bg=blok_fon, padx=12, pady=12,
#                       highlightbackground="#5d7fa5", highlightthickness=2)
# frame_tort.pack(fill="x", pady=8)

# tk.Label(frame_tort, text="To'g'ri to'rtburchak (a, b)", bg=blok_fon,
#          font=("Arial", 16, "bold")).pack(pady=4)

# t_a = tk.Entry(frame_tort, width=23, font=("Arial", 13)); t_a.pack(pady=3)
# t_b = tk.Entry(frame_tort, width=23, font=("Arial", 13)); t_b.pack(pady=3)


# def per():
#     try:
#         a=float(t_a.get()); b=float(t_b.get())
#         label_natija.config(text=f"P={2*(a+b):.2f}")
#     except:
#         label_natija.config(text="Xato!")


# btn4 = tk.Button(frame_tort, text="Perimetri", width=18,
#                  font=("Arial", 13), bg=btn, fg="white", command=per)
# btn4.pack(pady=3)
# btn4.bind("<Enter>", hover_in)
# btn4.bind("<Leave>", hover_out)


# # === Natija panel ===
# label_natija = tk.Label(container, text="", bg=natija_fon,
#                         font=("Arial", 18, "bold"), pady=15)
# label_natija.pack(pady=18, fill="x")

# oyna.mainloop()

# import tkinter as tk
# from tkinter import simpledialog
# import math

# oyna = tk.Tk()
# oyna.title("Geometriya + Kvadrat Tenglama")

# oyna.geometry("850x600")
# oyna.minsize(700, 500)

# fon = "#d7e8ff"
# blok_fon = "#ffffff"
# btn = "#4a8df7"
# btn_hover = "#2f6be0"
# natija_fon = "#ffe993"

# oyna.config(bg=fon)

# container = tk.Frame(oyna, bg=fon)
# container.pack(fill="both", expand=True, padx=20, pady=20)

# def hover_in(e): e.widget.config(bg=btn_hover)
# def hover_out(e): e.widget.config(bg=btn)


# # ===== KVADRAT =====
# frame_kv = tk.Frame(container, bg=blok_fon, padx=12, pady=12,
#                     highlightbackground="#5d7fa5", highlightthickness=2)
# frame_kv.pack(fill="x", pady=8)

# tk.Label(frame_kv, text="Kvadrat tenglama (a, b, c)", bg=blok_fon,
#          font=("Arial", 16, "bold")).pack(pady=4)

# def ildiz_soni():
#     a = simpledialog.askfloat("Kvadrat tenglama", "a = ")
#     b = simpledialog.askfloat("Kvadrat tenglama", "b = ")
#     c = simpledialog.askfloat("Kvadrat tenglama", "c = ")

#     if a is None or b is None or c is None:
#         return

#     if a == 0:
#         label_natija.config(text="Kvadrat emas!")
#         return

#     D=b*b-4*a*c
#     if D<0: nat="Ildiz yo'q"
#     elif D==0: nat="1 ta ildiz"
#     else: nat="2 ta ildiz"

#     label_natija.config(text=nat)


# def ildiz_topish():
#     a = simpledialog.askfloat("Kvadrat tenglama", "a = ")
#     b = simpledialog.askfloat("Kvadrat tenglama", "b = ")
#     c = simpledialog.askfloat("Kvadrat tenglama", "c = ")

#     if a is None or b is None or c is None:
#         return

#     if a==0:
#         label_natija.config(text="Kvadrat emas!")
#         return

#     D=b*b-4*a*c
#     if D<0:
#         label_natija.config(text="Ildiz yo'q")
#     elif D==0:
#         x=-b/(2*a)
#         label_natija.config(text=f"x={x:.2f}")
#     else:
#         x1=(-b+math.sqrt(D))/(2*a)
#         x2=(-b-math.sqrt(D))/(2*a)
#         label_natija.config(text=f"x1={x1:.2f}, x2={x2:.2f}")


# btn1 = tk.Button(frame_kv, text="Ildizlar soni", width=18, font=("Arial", 13),
#                  bg=btn, fg="white", command=ildiz_soni)
# btn2 = tk.Button(frame_kv, text="Ildizlarni topish", width=18, font=("Arial", 13),
#                  bg=btn, fg="white", command=ildiz_topish)

# btn1.pack(pady=3)
# btn2.pack(pady=3)

# for b in (btn1, btn2):
#     b.bind("<Enter>", hover_in)
#     b.bind("<Leave>", hover_out)


# # ===== UCHBURCHAK =====
# frame_uch = tk.Frame(container, bg=blok_fon, padx=12, pady=12,
#                      highlightbackground="#5d7fa5", highlightthickness=2)
# frame_uch.pack(fill="x", pady=8)

# tk.Label(frame_uch, text="Uchburchak (a, b, c)", bg=blok_fon,
#          font=("Arial", 16, "bold")).pack(pady=4)

# def uch_yuz():
#     a = simpledialog.askfloat("Uchburchak", "a = ")
#     b = simpledialog.askfloat("Uchburchak", "b = ")
#     c = simpledialog.askfloat("Uchburchak", "c = ")

#     if a is None or b is None or c is None:
#         return

#     if a+b<=c or a+c<=b or b+c<=a:
#         label_natija.config(text="Uchburchak bo'lmaydi!")
#         return

#     p=(a+b+c)/2
#     S=math.sqrt(p*(p-a)*(p-b)*(p-c))
#     label_natija.config(text=f"Uchburchak yuzi = {S:.2f}")

# btn3 = tk.Button(frame_uch, text="Yuzini hisoblash", width=18,
#                  font=("Arial", 13), bg=btn, fg="white", command=uch_yuz)
# btn3.pack(pady=3)
# btn3.bind("<Enter>", hover_in)
# btn3.bind("<Leave>", hover_out)


# # ===== TO'RTBURCHAK =====
# frame_tort = tk.Frame(container, bg=blok_fon, padx=12, pady=12,
#                       highlightbackground="#5d7fa5", highlightthickness=2)
# frame_tort.pack(fill="x", pady=8)

# tk.Label(frame_tort, text="To'g'ri to'rtburchak (a, b)", bg=blok_fon,
#          font=("Arial", 16, "bold")).pack(pady=4)

# def per():
#     a = simpledialog.askfloat("To'g'ri to'rtburchak", "a = ")
#     b = simpledialog.askfloat("To'g'ri to'rtburchak", "b = ")

#     if a is None or b is None:
#         return

#     P = 2*(a+b)
#     label_natija.config(text=f"Perimetri = {P:.2f}")

# btn4 = tk.Button(frame_tort, text="Perimetri", width=18,
#                  font=("Arial", 13), bg=btn, fg="white", command=per)
# btn4.pack(pady=3)
# btn4.bind("<Enter>", hover_in)
# btn4.bind("<Leave>", hover_out)


# # ===== NATIJA PANEL =====
# label_natija = tk.Label(container, text="", bg=natija_fon,
#                         font=("Arial", 18, "bold"), pady=15)
# label_natija.pack(pady=18, fill="x")


# oyna.mainloop()

# import tkinter as tk
# from tkinter import simpledialog
# import math

# oyna = tk.Tk()
# oyna.title("Geometriya + Kvadrat Tenglama")

# oyna.geometry("650x400")
# oyna.minsize(600, 350)

# fon = "#d7e8ff"
# btn = "#4a8df7"
# btn_hover = "#2f6be0"
# natija_fon = "#ffe993"

# oyna.config(bg=fon)


# def hover_in(e): e.widget.config(bg=btn_hover)
# def hover_out(e): e.widget.config(bg=btn)


# # ===== FUNKSIYALAR =====

# def ildiz_topish():
#     a = simpledialog.askfloat("Kvadrat tenglama", "a = ")
#     b = simpledialog.askfloat("Kvadrat tenglama", "b = ")
#     c = simpledialog.askfloat("Kvadrat tenglama", "c = ")

#     if a is None or b is None or c is None:
#         return
#     if a == 0:
#         label_natija.config(text="Kvadrat emas!")
#         return

#     D = b*b - 4*a*c
#     if D < 0:
#         label_natija.config(text="Ildiz yo'q")
#     elif D == 0:
#         x = -b/(2*a)
#         label_natija.config(text=f"x = {x:.2f}")
#     else:
#         x1 = (-b + math.sqrt(D)) / (2*a)
#         x2 = (-b - math.sqrt(D)) / (2*a)
#         label_natija.config(text=f"x1 = {x1:.2f},  x2 = {x2:.2f}")


# def uch_yuz():
#     a = simpledialog.askfloat("Uchburchak", "a = ")
#     b = simpledialog.askfloat("Uchburchak", "b = ")
#     c = simpledialog.askfloat("Uchburchak", "c = ")

#     if a is None or b is None or c is None:
#         return

#     if a + b <= c or a + c <= b or b + c <= a:
#         label_natija.config(text="Uchburchak bo'lmaydi!")
#         return

#     p = (a+b+c)/2
#     s = math.sqrt(p*(p-a)*(p-b)*(p-c))
#     label_natija.config(text=f"Uchburchak yuzi = {s:.2f}")


# def per():
#     a = simpledialog.askfloat("To'g'ri to'rtburchak", "a = ")
#     b = simpledialog.askfloat("To'g'ri to'rtburchak", "b = ")

#     if a is None or b is None:
#         return

#     p = 2*(a+b)
#     label_natija.config(text=f"Perimetri = {p:.2f}")


# # ===== TUGMALAR =====

# btn1 = tk.Button(oyna, text="Kvadrat tenglama ildizlari (a,b,c)",
#                  width=35, font=("Arial", 14), bg=btn, fg="white",
#                  command=ildiz_topish)
# btn1.pack(pady=12)

# btn2 = tk.Button(oyna, text="Uchburchak yuzi (a,b,c)",
#                  width=35, font=("Arial", 14), bg=btn, fg="white",
#                  command=uch_yuz)
# btn2.pack(pady=12)

# btn3 = tk.Button(oyna, text="To'g'ri to'rtburchak perimetri (a,b)",
#                  width=35, font=("Arial", 14), bg=btn, fg="white",
#                  command=per)
# btn3.pack(pady=12)

# for b in (btn1, btn2, btn3):
#     b.bind("<Enter>", hover_in)
#     b.bind("<Leave>", hover_out)


# # ===== NATIJA PANEL =====

# label_natija = tk.Label(oyna, text="", bg=natija_fon,
#                         font=("Arial", 18, "bold"), pady=15)
# label_natija.pack(fill="x", pady=20)


# oyna.mainloop()
import tkinter as tk
import math

oyna = tk.Tk()
oyna.title("Geometriya + Kvadrat Tenglama")
oyna.geometry("650x400")
oyna.config(bg="#d7e8ff")

btn = "#4a8df7"
btn_hover = "#2f6be0"
natija_fon = "#ffe993"

def hover_in(e): e.widget.config(bg=btn_hover)
def hover_out(e): e.widget.config(bg=btn)


# ========== MINI OYNA FUNKSIYALARI ==========

def kvadrat_window():
    win = tk.Toplevel(oyna)
    win.title("Kvadrat tenglama")
    win.geometry("250x260")
    win.config(bg="white")

    tk.Label(win, text="a:", font=("Arial", 12), bg="white").pack(pady=3)
    e_a = tk.Entry(win, font=("Arial", 12)); e_a.pack()

    tk.Label(win, text="b:", font=("Arial", 12), bg="white").pack(pady=3)
    e_b = tk.Entry(win, font=("Arial", 12)); e_b.pack()

    tk.Label(win, text="c:", font=("Arial", 12), bg="white").pack(pady=3)
    e_c = tk.Entry(win, font=("Arial", 12)); e_c.pack()

    def hisobla():
        try:
            a=float(e_a.get()); b=float(e_b.get()); c=float(e_c.get())
            if a==0:
                label_natija.config(text="Kvadrat emas!")
                win.destroy(); return

            D=b*b-4*a*c
            if D<0:
                label_natija.config(text="Ildiz yo'q")
            elif D==0:
                x=-b/(2*a)
                label_natija.config(text=f"x={x:.2f}")
            else:
                x1=(-b+math.sqrt(D))/(2*a)
                x2=(-b-math.sqrt(D))/(2*a)
                label_natija.config(text=f"x1={x1:.2f},  x2={x2:.2f}")
        except:
            label_natija.config(text="Xato!")
        win.destroy()

    tk.Button(win, text="Hisoblash", bg=btn, fg="white",
              font=("Arial", 12), command=hisobla).pack(pady=10)


def uch_window():
    win = tk.Toplevel(oyna)
    win.title("Uchburchak yuzi")
    win.geometry("250x260")
    win.config(bg="white")

    tk.Label(win, text="a:", font=("Arial", 12), bg="white").pack(pady=3)
    e_a = tk.Entry(win, font=("Arial", 12)); e_a.pack()

    tk.Label(win, text="b:", font=("Arial", 12), bg="white").pack(pady=3)
    e_b = tk.Entry(win, font=("Arial", 12)); e_b.pack()

    tk.Label(win, text="c:", font=("Arial", 12), bg="white").pack(pady=3)
    e_c = tk.Entry(win, font=("Arial", 12)); e_c.pack()

    def hisobla():
        try:
            a=float(e_a.get()); b=float(e_b.get()); c=float(e_c.get())
            if a+b<=c or a+c<=b or b+c<=a:
                label_natija.config(text="Uchburchak bo'lmaydi!")
            else:
                p=(a+b+c)/2
                s=math.sqrt(p*(p-a)*(p-b)*(p-c))
                label_natija.config(text=f"Uchburchak yuzi = {s:.2f}")
        except:
            label_natija.config(text="Xato!")
        win.destroy()

    tk.Button(win, text="Hisoblash", bg=btn, fg="white",
              font=("Arial", 12), command=hisobla).pack(pady=10)


def tort_window():
    win = tk.Toplevel(oyna)
    win.title("To'g'ri to'rtburchak")
    win.geometry("250x200")
    win.config(bg="white")

    tk.Label(win, text="a:", font=("Arial", 12), bg="white").pack(pady=3)
    e_a = tk.Entry(win, font=("Arial", 12)); e_a.pack()

    tk.Label(win, text="b:", font=("Arial", 12), bg="white").pack(pady=3)
    e_b = tk.Entry(win, font=("Arial", 12)); e_b.pack()

    def hisobla():
        try:
            a=float(e_a.get()); b=float(e_b.get())
            p=2*(a+b)
            label_natija.config(text=f"Perimetri = {p:.2f}")
        except:
            label_natija.config(text="Xato!")
        win.destroy()

    tk.Button(win, text="Hisoblash", bg=btn, fg="white",
              font=("Arial", 12), command=hisobla).pack(pady=10)


# ========== TUGMALAR ==========

btn1 = tk.Button(oyna, text="Kvadrat tenglama ildizlari (a,b,c)",
                 width=35, font=("Arial", 14), bg=btn, fg="white",
                 command=kvadrat_window)
btn2 = tk.Button(oyna, text="Uchburchak yuzi (a,b,c)",
                 width=35, font=("Arial", 14), bg=btn, fg="white",
                 command=uch_window)
btn3 = tk.Button(oyna, text="To'g'ri to'rtburchak perimetri (a,b)",
                 width=35, font=("Arial", 14), bg=btn, fg="white",
                 command=tort_window)

btn1.pack(pady=10)
btn2.pack(pady=10)
btn3.pack(pady=10)

for b in (btn1, btn2, btn3):
    b.bind("<Enter>", hover_in)
    b.bind("<Leave>", hover_out)


# ========== NATIJA PANELI ==========

label_natija = tk.Label(oyna, text="",
                        bg=natija_fon, font=("Arial", 18,"bold"), pady=15)
label_natija.pack(fill="x", pady=20)

oyna.mainloop()
