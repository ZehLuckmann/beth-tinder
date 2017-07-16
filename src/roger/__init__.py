# -*- coding: utf-8 -*-
from roger.intention import Intention
import roger.manage_data
import logging

class Roger(object):
    def predict_intention(self):
        train_set_arq =  './roger/database/intention_train_set.csv'
        test_set_arq =  './roger/database/intention_test_set.csv'

        logging.debug('Busca dados de treino em ',train_set_arq)
        train_set = roger.manage_data.csv_file(train_set_arq)
        print(train_set)
        logging.debug('Busca dados de teste em ',test_set_arq)
        test_set = roger.manage_data.csv_file(test_set_arq)
        print(test_set)
        logging.debug('Inicia processos da IA')

        intention = Intention()

        intention.train(train_set)
        intention.test(test_set)

        self.user_interface(intention.return_intention)

    def user_interface(self, method):
        print('')
        while True:
            print('')
            print('Informe a frase que você deseja obter o resultado(EX: "Eu odeio você"): ')
            input_phrase = input('');
            print('')
            result = method(input_phrase)
            print(result)
            print('')
            if input('Deseja buscar uma nova palavra?(S/n):') == 'n':
                break

    def start(self):
        opt = -1
        while opt != '0':
            print('Qual função você deseja acessar?')
            print('1 - Prever intenção da frase')
            print('0 - Sair')
            opt = input('Digite a opção: ')

            if opt == '1':
                self.predict_intention()
            elif opt != '0':
                print('Opção inválida')

        print('Até logo!!')
