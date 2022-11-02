"""
Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent
"""
while True:
    choice = input("what type of number do you want to convert 'd' decimal or 'b' binary? ")
    if choice.lower() == 'd':
        while True:
            n = int( input( 'Введите десятичное число: ' ) )
            try:
                print( f'{n}(10) -------> {str( bin( int(n) ) )[2:]}(2)' )
                break
            except:
                print('Ввод некорректный.')
                print()
        break
    elif choice.lower() == 'b':
        while True:
            n = input( 'Введите двоичное число: ' )
            try:
                print( f'{n}(2) -------> {str( int(n,2) )}(10)' )
                break
            except:
                print('Ввод некорректный.')
                print()
        break
    else:
        print("Please type 'd' or 'b' ")
        continue