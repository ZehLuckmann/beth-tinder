# -*- coding: utf-8 -*-
from roger.talk import Talk
import roger.export_conversations
import roger.manage_files
import logging

class Roger(object):
    def talk(self):
        train_set_arq =  './roger/database/dados_treino_ze.csv'
        
        test_set_arq =  './roger/database/dados_teste_ze.csv'

        logging.debug('Busca dados de treino em {}'.format(train_set_arq))
        train_set = roger.manage_files.get_csv_file(train_set_arq)
        logging.debug('Busca dados de teste em {}'.format(test_set_arq))
        test_set = roger.manage_files.get_csv_file(test_set_arq)
       
        logging.debug('Inicia processos da IA')

        t = Talk()

        t.train(train_set)
        t.test(test_set)

        self.user_interface_request_phrase(t.response)

    def user_interface_request_phrase(self, method):
        print('')
        print('Comece a conversar, diga "tchau" para sair: ')
        while True:
            input_phrase = input('Você: ')

            if input_phrase == 'tchau':
                print('Tchau!')
                return

            result = method(input_phrase)
            print('Roger: {}'.format(result))

    def start(self):
        opt = -1
        while opt != '0':
            print('Qual função você deseja acessar?')
            print('1 - Conversar')
            print('2 - Exportar conversas')
            print('0 - Sair')
            opt = input('Digite a opção: ')

            if opt == '1':
                self.talk()
            if opt == '2':
                roger.export_conversations.start()
            elif opt != '0':
                print('Opção inválida')

        print('Até logo!!')
