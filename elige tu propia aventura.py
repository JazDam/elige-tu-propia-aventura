print('ELIGE TU PROPIA AVENTURA')
print('Un solo camino')
dead = False

start_game = input('¿Queres jugar?(Responde con un "si" o un "no"): ')
while start_game != 'si' and start_game != 'no':
    print('Respuesta incorrecta. Intentalo de nuevo.')
    start_game = input('¿Queres jugar?(Responde con un "si" o un "no"): ')
if start_game == 'no':
    print('Ok. Adiós!')
    exit()
if start_game == 'si':
    print('Ok. Empecemos!')
print('Te encontras en un descampado; de inmediato empezas a mirar a tu alrededor y te preguntas en donde estas. ¿Que haces?')
options = { 
'a' : 'Explorar el lugar buscando como volver a tu hogar', 
'b' : 'Empezar a gritar pidiendo auxilio',
'c' : 'Quedarte en el mismo lugar sin hacer absolutamente nada ',
}
for key, value in options.items():
    print(key, '=', value)
question1 = input('Mi opción es: ')
if question1 == 'b':
    print('Atraiste a una tribu de canibales y te capturaron. Has muerto devorado por ellos.')
    dead = True
if question1 == 'c':
    print('Han pasado los días y finalmente has muerto a causa de hambre y dehidratación.')
    dead = True
if question1 == 'a':
    print('Tras dezplazarte varios kilometros encontras una cabaña en el medio de un bosque. ¿Que haces?')
    options = {
    'a' : 'Decidis entrar a la cabaña',
    'b' : 'Seguis de largo tu camino',
    'c' : 'Decidis volver a donde habias comenzado',
    }
    for key, value in options.items():
        print(key, '=', value)
    question2 = input('Mi opción es: ')
    if question2 == 'a' :
        print('Resultó ser la cabaña de un ogro, el cual al volver y encontrarte en su hogar decidió hacerse un asado con tus restos. Moriste.')
        dead = True
    if question2 == 'c': 
        print('Te perdiste en el bosque, te encontró un hambriento oso y moriste devorado por él.')
        dead = True
    if question2 == 'b' :
        print('A 5 kilometro de la cabaña encontras un pequeño pueblo. ¿Que haces?')
        options = {
        'a' : 'Decidis explorar el pueblo',
        'b' : 'Pedis desesperadamente ayuda a los pueblerinos',
        'c' : 'Seguis de largo tu camino',
        }
        for key, value in options.items():
            print(key, '=', value)
        question3 = input('Mi opción es: ')
        if question3 == 'a':
            print('Fuiste mordido por un perro callejero. Moriste luego de contraer rabia.')
            dead = True
        if question3 == 'b': 
            print('Asustaste a los pueblerinos. Moriste de un tiro.')
            dead = True
        if question3 == 'c':
            print('Encontras un grupo de exploradores, les comentas tu situación y te ofrecen unirte a ellos.')
        question4 = input('¿Te unis a ellos?. (Responde con un "si" o un "no"): ')
        if question4 == 'si':
            print('Los exploradores estan en busca de un tesoro y se dirigen hacia una isla. Luego de un largo viaje llegan a la isla en la cual se encontraría el tesoro, estan explorando la isla cuando de pronto... son atacados por orangutanes que comienzan a arrojarles bananas entre los árboles. ¿Que haces?')
            options = {
            'a' : 'Decidis comer las bananas que te arrojan los orangutanes',
            'b' : 'Corres para no morir atacado con bananas',
            'c' : 'Fingir tu muerte para que los orangutanes dejen de atacarte',
            }
            for key, value in options.items():
               print(key, '=', value)
            question5 = input('Mi opción es: ')
            if question5 == 'a':
                print('Moriste atragantado por comer tantas bananas.')
                dead = True
            if question5 == 'c':
                print('Al encontrar tu cuerpo tirado los orangutanes se te acercan pero de inmediato descubren que seguis respirando y te matan.')
                dead = True
            if question5 == 'b':
                print('Lograste escapar de los orangutanes pero perdiste a tus compañeros exploradores por lo que de nuevo te encontras solo. Que haces ahora?')
                options = {
                    'a': 'Buscas el tesoro solo',
                    'b': 'Buscas salir cuanto antes de ésa isla',
                    'c': 'Buscas a tus compañeros exploradores',
                }
                for key, value in options.items():
                    print(key, '=', value)
                question6 = input('Mi opción es: ')
                if question6 != 'a':
                    print('Te volvieron a encontrar los orangutanes. Moriste atacado por ellos.')
                    dead = True
                if question6 == 'a':
                    print('Te adentras en lo mas recóndito de la isla cuando llegas a encontrar una enorme edificación similar a un templo que al parecer está abandonado. ¿Decdis entrar? (REsponde con un "si" o un "no".')
                    question7 = input('Mi opción es: ')
                    if question7 == 'si':
                        print('Estas dentro del templo, de repente se te aparece un mapache gigante quien resulta ser el guardian del tesoro. ¡Lo encontraste!. Pero antes tenes que pasar por el guardian. ¿Que haces?')
                        options = {
                            'a': 'Peleas con el guardian para matarlo y quedarte con el tesoro',
                            'b': 'Buscas una salida',
                            'c': 'Le explicas al guardian que venis en busca del tesoro',
                        }
                        for key, value in options.items():
                            print(key, '=', value)
                        question8 = input('Mi opción es: ')
                        if question8 == 'a':
                            print('El guardian te derrotó. Moriste')
                            dead = True
                        if question8 == 'b':
                            print('Una vez que entras al templo no podes salir mas si no es con el tesoro. Moriste lentamente encerrado en ese lugar.')
                            dead = True
                        if question8 == 'c':
                            print('El guardian te da a elegir entre dos opciones')
                            options = {
                                'a' : 'Llevarte el tesoro',
                                'b' : 'Volver a tu hogar al que quisiste llegar desde un principio',
                            }
                            for key, value in options.items():
                                print(key, '=', value)
                            question9 = input('Mi opción es:')
                            if question9 == 'a':
                                print('El guardian te entrega el tesoro! Pasas tus días viviendo en la isla.')
                            if question9 == 'b':
                                print('Despertas y te encontras de nuevo en tu hogar. Todo ha vuelto a la normalidad!')
        if question4 == 'no':
            print('Seguis caminando por varios kilometros hasta que te encontras a un guarda bosques. ¿Le pedis ayuda?(Responde con un "si" o un "no")')
            question10 = input('Mi opción es: ')
            if question10 == 'si':
                print('El guarda bosques te entrega un mapa y te indica en donde estas y como volver a tu hogar. Has tenido éxito en tu aventura!')
            if question10 == 'no':
                print('No has logrado llegar a ningun lugar, moriste solo y perdido en la inmensidad del bosque.')
                dead = True
if dead:
    print('Game Over!')
    exit()
            

            


