import caesar_cypher as cc
import transposition_cypher as tc
import sys



def menu():
    methods = {1: 'Caesar Cypher', 2: 'Transposition Cypher', 3: 'Quit'}
    print ('\n**********  CypherProgram v1.02 **********')

    
    while True:
        print ('\nSelect a decryption method\n')
        for key, value in methods.items():
            print(f'{key}: {value}')
            
        
        selection = input('\nSelection: ')

        if selection == '1':
            path = input('What message do you want do encrypt/decrypt? (insert path): ')
            key = int(input('What is the secret key?: '))
            choice = int(input('Do you want to perform encryption or decryption?\nWrite 1 encryption or 2 for decryption:'))
            
            if choice == 1:
                cc.encrypt(path, key)
            elif choice == 2:
                cc.decrypt(path, key)
            break

        elif selection == '2':
            path = input('What message do you want do encrypt/decrypt? (insert path): ')
            key = int(input('What is the secret key?: '))
            choice = int(input('Do you want to perform encryption or decryption?\nWrite 1 encryption or 2 for decryption:'))
            
            if choice == 1:
                tc.encryption(path, key)
            elif choice == 2:
                tc.decryption(path, key)

            break

        elif selection == '3':
            sys.exit()

        else :
            print ('\nWrong input, try again')
        
menu()

