import os
import random

lifes = ['''

    +----+
         |
         |
         |
         |  
          
''',
'''

    +----+
    O    |
         |
         |
         |  
          
''',
'''

    +----+
    O    |
    |    |
         |
         |  
          
''',
'''

    +----+
    O/   |
    |    |
         |
         |  
          
''',
'''

    +----+
   \O/   |
    |    |
         |
         |  
          
''',
'''

    +----+
   \O/   |
    |    |
     \   |
         |  
          
''',
 '''

    +----+
   \O/   |
    |    |
   / \   |
         |  
          
''',
'''
██████╗ ███████╗██████╗ ██████╗ ██╗███████╗████████╗███████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝██╔════╝
██████╔╝█████╗  ██████╔╝██║  ██║██║███████╗   ██║   █████╗  
██╔═══╝ ██╔══╝  ██╔══██╗██║  ██║██║╚════██║   ██║   ██╔══╝  
██║     ███████╗██║  ██║██████╔╝██║███████║   ██║   ███████╗
╚═╝     ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚══════╝   
''']

win = '''
 ██████╗  █████╗ ███╗   ██╗ █████╗ ███████╗████████╗███████╗
██╔════╝ ██╔══██╗████╗  ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝
██║  ███╗███████║██╔██╗ ██║███████║███████╗   ██║   █████╗  
██║   ██║██╔══██║██║╚██╗██║██╔══██║╚════██║   ██║   ██╔══╝  
╚██████╔╝██║  ██║██║ ╚████║██║  ██║███████║   ██║   ███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝      
'''

run = os.system
run('cls')

box = {'es un lenguaje de programacion muy popular': 'python', 'unico animal mamifero que puede volar': 'murcielago', 'instrumento que tiene 6 cuerdas': 'guitarra', 'pais mas grande del mundo': 'rusia'}


while True:    
    print('''
        
        BIENVENIDOS AL AHORCADO
        
        
        Tecla enter para continuar o exit para salir..      

    ''')
    option =str(input(": "))
    if option == 'exit':
        break
    else:
        pass
    
    run('cls')
    
    random_keys = random.choice(list(box.keys()))  
    respuesta = box[random_keys]
    
    
    
    array = []
    
    for char in respuesta:
        array.append(char)
    veces = len(array) - 1
    print(random_keys)
    print(array)
    print(lifes[0])
    x = 0
    
    while True:
        print()
        var = str(input('digite una letra: '))
        var.lower()
        for i in array:
            if i == var:
                pass
            else:
                x += 1
                run('cls')
                print(random_keys)
                print(array)
                print(lifes[x])
                break
        if veces == x:
            run('cls')
            print(lifes[veces])
            break
        
        
        
            
            
    
    
    
    
    
