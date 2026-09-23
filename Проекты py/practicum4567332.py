def S(x1,x2):
    L = x1*x2/10
    print(f"необходимо {L} литров краски")
S(10,10)
def vinni(med):
    if med < 7 or med == 7:
        print("Всё обошлось")
    elif med > 7:
        print("Кто-то останется на ночовку")
vinni(7)
vinni(8)
def geometric_progressiya(N):
    i = 1
    for i in range(N):
        i = i * i
    print(f"Людей,которые узнали всю историю танкостроения за {N} дней - {i}")
geometric_progressiya(50)
def geometric_progressiya_x2(a):
    v = a
    b = 1
    b2 = 0
    while a < 1060:
        a = a*2
        b = b+1
        if b > 30:
            b2 = b2+1
    print(f"При начальной скорости {v} кликов/сек,Гена смог побить рекорд за {b2} месяцев и {b} дней")
geometric_progressiya_x2(1)
