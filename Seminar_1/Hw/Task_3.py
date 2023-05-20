#  Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
#  Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
#  Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
ticket = (input("Ввидите номер билета:"))
if( 5 < len(ticket) < 7):
    ticket = int(ticket)
    firsthalf = ticket//1000
    secondhalf = ticket%1000
    firstsum = 0
    secondsum = 0 
    while(firsthalf > 0):
        firstsum+=firsthalf%10
        firsthalf//=10
    while(secondhalf > 0):
        secondsum+=secondhalf%10
        secondhalf//=10    
    if(firstsum==secondsum):
        print("Да ты визунчик")
    else:
        print("Cегодня не твой день (")
else:
    print("Ты точно купил билет ?")
# Сразу извиняюсь за это решение 
