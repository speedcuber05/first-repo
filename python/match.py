x=int(input('enter x   '))
match x:
    case 1:
        print('hello')
    case 2:
        print('there')
    case 3 | 4:       # this is OR
        print('maybe')
    case x if x>4:
        print('guys')

    case _ :          # the case where nothing matches
        print('nah')


        
#still unexplored