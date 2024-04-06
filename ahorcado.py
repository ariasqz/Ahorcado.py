import os
import random
import copy
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
    
    list1 = []
    list2 = []
    
    for char in respuesta:
        list1.append(char)
        list2.append(char)
        
    veces = len(list1) - 1
    
    for i in range(len(list2)):
        list2[i] = '-'
        
    
        
    
    print(random_keys)
    print(list1)
    print(list2)
    print(lifes[0])
    x = 0
    
    while True:
        print()
        var = str(input('digite una letra: '))
        var.lower()
        for i in list1:
            if i == var:
                pass
            else:
                x += 1
                run('cls')
                print(random_keys)
                print(list1)
                print(list2)
                print(lifes[x])
                break
        if veces == x:
            run('cls')
            print(lifes[veces])
            break
        
        
        
        
            
            
    
    
    
    
    
