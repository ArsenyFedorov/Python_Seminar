# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
longch =int(input("Ввидите длинну шоколадки:"))
widthch =int(input("Ввидите ширину шоколадки:"))
piecesch =int(input("Cколько вам надо кусочков:"))
if(piecesch < longch*widthch and piecesch//longch or piecesch//widthch):
    print("Можно отломи")
else:
    print("Нельзя ")