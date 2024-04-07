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
    
    x = 0 
    y = 0
    
    def imprimir():
        print()
        print(random_keys)
        print(list2)
        print(lifes[y])
    
    imprimir()
    
    while x < 7:
        if list1 == list2:
            print(win)
            break
                             
        print()
        var = str(input('digite una letra: '))
        var.lower()
        
        if var in list1:
            for i in range(len(list2)):
                if list1[i] == var:
                    list2[i] = var
                    run('cls')
                    imprimir()
                    
        else:
            x += 1
            y += 1
            run('cls')
            imprimir()
        
        
        
        
            
            
    
    
    
    
    
