#Написати програму яка буде виводити на екран розклад занять згідно введеного номеру тижня та дня тижня.

week = input("Введіть номер тижня (1 або 2): ")
day = input("Введіть день тижня: ")

if week == "1":
    if day == "Понеділок":
        print("Операційні системи")
        print("Комп'ютерні мережі")
        print("Комп'ютерні мережі")
        print("Спец.прикладне програмування")
    elif day == "Вівторок":
        print("Розр.клієнт-серверних застосунків")
        print("Операційні системи")
        print("Web-технології та Web-дизайн")
    elif day == "Середа":
        print("Розр.клієнт-серверних застосунків")
        print("Web-технології та Web-дизайн")
        print("Web-технології та Web-дизайн")
    elif day == "Четвер":
        print("Спец.прикладне програмування")
        print("Технологія створення програмних продуктів")
        print("Розр.клієнт-серверних застосунків")
    elif day == "П'ятниця":
        print("Розр.клієнт-серверних застосунків")
        print("Технологія створення програмних продуктів")
    elif day == "Субота" or day == "Неділя":
        print("Вихідні!")

elif week == "2":
    if day == "Понеділок":
        print("Операційні системи")
        print("Комп'ютерні мережі")
        print("Комп'ютерні мережі")
        print("Спец.прикладне програмування")
    elif day == "Вівторок":
        print("Розр.клієнт-серверних застосунків")
        print("Web-технології та Web-дизайн")
        print("Web-технології та Web-дизайн")
    elif day == "Середа":
        print("Розр.клієнт-серверних застосунків")
        print("Web-технології та Web-дизайн")
        print("Web-технології та Web-дизайн")
    elif day == "Четвер":
        print("Спец.прикладне програмування")
        print("Технологія створення програмних продуктів")
        print("Розр.клієнт-серверних застосунків")
    elif day == "П'ятниця":
       print("Розр.клієнт-серверних застосунків")
       print("Технологія створення програмних продуктів")
    elif day == "Субота" or day == "Неділя":
        print("Вихідні!")
else:
    print("Не правильно введений тиждень або день. Будь ласка, введіть 1 або 2 для тижня, та правильний день.")
