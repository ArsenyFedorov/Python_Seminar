#Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# если составить уравнение и принять работу Пети за х тогда х + х + 4х = S 
# Работа Кати 4х тк она сделала в 2 раза  больше чем Петя и Серёжа , а их работы это х + х 
paperbirds = int(input("Cколько дети сделали журавликов:"))
x = paperbirds / 6 
print(f"Катя сделала {int(x*4)} журавликов , Петя сделал {int(x)} журавликов , Серёжа сделал {int(x)} журавликов")
# задача ломается если работа детей не делится начело на 6 ) 