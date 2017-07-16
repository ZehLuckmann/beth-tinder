#Configuração do ambiente de desenvolvimento

### Instalação
* Instale e configure o [Docker][1] no seu computador
* Clone o repositório do projeto [Roger][2]
  ```bash
  git clone https://github.com/ZehLuckmann/Roger.git
  ```
* Entre na pasta do projeto
    ```bash
    cd ./Roger
    ```
* Com o Docker vocẽ irá criar uma imagem do projeto:
  ```bash
  sudo docker build -t roger_img --file ./DockerFile .
  ```
* Pronto, aogra você já tem uma imagem do ambiente para começar a desenvolver

###Iniciando desenvolvimento

* Todos os códigos fontes se encontram na pasta __src__
* Os códigos podem ser editados com o editor de sua prefêrencia (vim, atom, sublime...)
* Para dar inicio em seu ambiente de testes, deve executar os seguintes comandos dentro da pasta __src__:
  * "Sobe" o container com as configurações:
    ```bash
    sudo docker run -d -it --name roger-desenv -v `pwd`:/src roger_img
    ```
  * Acessa o modo interativo do container:
    ```bash
    docker exec -it roger-desenv bash
    ```
* Agora o console está dentro do ambiente virtual do projeto, comandos linux vão funcionar pela linha de comando (ls, mkdir...)
* Para executar a aplicação principal, digite:
  ```bash
  python run.py
  ```
* Sempre que você fizer uma alteração no código, só é necessário executar o último passo
* Para finalizar o container digite:
  ```bash
  sudo docker kill roger-desenv
  ```

[1]: https://www.docker.com/
[2]: https://github.com/ZehLuckmann/Roger
