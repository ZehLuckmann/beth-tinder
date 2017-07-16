# -*- coding: utf-8 -*-
import roger.intention, roger.preprocessing, roger.load_data

def start():

    train_set = roger.load_data.csv_file('./roger/database/intention_train_set.csv')
    test_set = roger.load_data.csv_file('./roger/database/intention_test_set.csv')

    print(train_set)
    print(test_set)
    
    roger.intention.train(train_set, test_set)

    print('')
    while True:
        print('')
        print('Informe a frase que você deseja obter o resultado: ')
        input_phrase = input('');
        print('')
        roger.intention.print_intention(input_phrase)
        print('')
        if input('Deseja buscar uma nova palavra?(S/n):') == 'n':
            break
