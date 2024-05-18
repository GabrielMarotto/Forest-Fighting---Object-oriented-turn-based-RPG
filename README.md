# Forest Fighting

**Forest Fighting** é um jogo de luta por turnos para dois jogadores, desenvolvido em Python, que utiliza conceitos de Programação Orientada a Objetos. No jogo, os jogadores se encontram na misteriosa Floresta dos Elfos Selvagens e devem usar suas habilidades e sorte para vencer o oponente.
Cada jogador pode escolher entre 4 classes de personagens: Ladino, Guerreiro, Mago ou Bardo cada um com habilidades únicas. O Jogo é reproduzido em seu terminal console.

## Classes de Personagens

### Ladino
- **Atributo Principal**: Agilidade
- **Armas**: Adaga, Arco Longo e Espada Longa

### Guerreiro
- **Atributo Principal**: Força
- **Armas**: Machado Pequeno, Lança e Machado de Batalha

### Mago
- **Atributo Principal**: Inteligência
- **Armas**: Faísca arcana, Raio de Eletricidade e Bola de fogo

### Bardo
- **Atributo Principal**: Sabedoria
- **Armas**: Maracas, Viola e Bateria

## Mecânicas de Jogo

- **Escolha de Personagem**: Cada jogador escolhe seu personagem no início do jogo.
- **Ações de Turno**: Durante seu turno, o jogador pode atacar ou vasculhar a floresta em busca de itens que aumentem suas habilidades.
- **Barra de Vida**: Cada personagem possui uma barra de vida visualizada durante o jogo, que indica a saúde atual e máxima do personagem.
- **Itens**: Os jogadores podem encontrar talismãs na floresta que aumentam sua força ou agilidade, adicionando um elemento de sorte e estratégia ao jogo.
- **Tratativas de erros**: Caso um dos players escolha alguma opção não disponível para jogar, o jogo possui a trativa desse comando errado por parte do jogador. 

## Como Jogar

1. No início do jogo, cada jogador escolhe seu personagem: Ladino, Guerreiro, Mago ou Bardo.
2. Os jogadores vasculham a floresta para encontrar uma arma inicial.
3. O confronto começa, e os jogadores se alternam em turnos, podendo atacar o oponente, procurar por itens na floresta ou utilizar seu ataque especial.
4. O jogo continua até que a vida de um dos jogadores seja reduzida a zero.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do jogo.
- **Programação Orientada a Objetos**: Estruturação do código com classes para personagens, armas, itens aleatórios e barras de vida.
- **Lib OS**: Para limpeza da console entre turnos dos jogadores.
- **Lib Time**: Aprimorar a experiência do jogador, com um timing durante as rodados, deixando o jogo mais fluído. 
- **Lib Random**: Adicionar aleatoriade em escolhas de certos atributos durante o jogo.
- **Arquivo Lib .Py**: Layout para aprimorar a experiência do jogador.

## Instalação e Execução

1. Clone este repositório.
2. Certifique-se de ter o Python instalado em sua máquina.
3. Execute o arquivo `Main.py` para iniciar o jogo em seu console.

```bash
git clone https://github.com/seu-usuario/forest-fighting.git
cd forest-fighting
python Main.py
```

Divirta-se jogando **Forest Fighting** e desafie seus amigos para descobrir quem é o verdadeiro mestre da Floresta dos Elfos Selvagens!

---

## Funcionalidades

- Tela inicial do game: 
    <div aling='center'>
     <img src="./webScraping/Imagens/PaginaInicial.png"/>
    </div> 


- Telas onde o player irá escolher o sua classe e o seu nome no jogo respectivamente:
   <div aling='center'>
    <img src="./webScraping/Imagens/Componentes.png"/>
   </div> 


- Componente de Pesquisa para pesquisar de algum alimento que possa estar cadastrado no banco de dados:
   <div aling='center'>
    <img src="./webScraping/Imagens/OpcaoPesquisa.png"/>
   </div> 
   <div aling='center'>
    <img src="./webScraping/Imagens/PesquisaFeita.png"/>
   </div> 


- Banco de Dados com a tabela Alimentos sem o resgate dos dados:
   <div aling='center'>
    <img src="./webScraping/Imagens/TabelaAlimentosBD.png"/>
   </div> 
- Banco de Dados com a tabela Alimentos após o load da aplicação e resgate de dados:
   <div aling='center'>
    <img src="./webScraping/Imagens/AlimentosSalvosBD.png"/>
   </div> 


- Banco de Dados com a tabela de Componentes antes do usuário selecionar algum alimento para pesquisar:
   <div aling='center'>
    <img src="./webScraping/Imagens/TabelaComponentesBD.png"/>
   </div> 
- Banco de Dados com a tabela de Componentes após cliente clicar em um alimento abrindo nova view, solicitando o resgate e o registro de dados no banco:
   <div aling='center'>
    <img src="./webScraping/Imagens/ComponentesSalvosBd.png"/>
   </div> 
