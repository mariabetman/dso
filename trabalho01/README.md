# Sistema de Gerenciamento de Campeonatos de Futebol Universitário

## Introdução

Este trabalho tem como objetivo apresentar a documentação e a divisão de tarefas para o desenvolvimento do sistema de gerenciamento de campeonatos de futebol universitário, desenvolvido para a disciplina de Desenvolvimento de Sistemas Orientados a Objetos I, da Universidade Federal de Santa Catarina.

Para a documentação do sistema, foi desenvolvido um diagrama na Linguagem de Modelagem Unificada (UML), utilizando o padrão de projeto Model-View-Controller (MVC). A partir da documentação e do diagrama, o sistema foi desenvolvido na linguagem de programação Python.

## Menus do Sistema

No padrão Model-View-Controller (MVC), as "views" são responsáveis pela apresentação dos dados ao usuário final. Elas representam a camada de interação com o usuário, traduzindo os dados do modelo (Model) em uma forma compreensível para os usuários e respondendo às interações do utilizador, encaminhando-as para o controlador (Controller) correspondente para processamento adicional.

### TelaSistema

A TelaSistema é a tela inicial de interação com o usuário. Nela, são apresentadas as opções que o usuário tem ao utilizar o sistema de gerenciamento, levando-o aos demais menus, que são apresentados a seguir.

### TelaAluno

Na TelaAluno, são disponibilizadas as opções relativas às operações que envolvem o cadastro de alunos, como o cadastro, consulta, edição e exclusão. A consulta é feita com base na matrícula do aluno.

### TelaArbitro

Assim como na TelaAluno, a TelaArbitro possui as operações básicas de cadastro, consulta, edição e exclusão, com a diferença de que a consulta utiliza o CPF como parâmetro.

### TelaCampeonato

Na TelaCampeonato, as funcionalidades são: criação, consulta por código, edição, exclusão, adição e remoção de equipes, adição e remoção de partidas, inicialização do campeonato e geração de relatórios. Ao iniciar um campeonato, os confrontos são gerados com apenas os atributos dos times que se enfrentarão. Posteriormente, na TelaPartida, o usuário inclui informações como data da partida, árbitro responsável, gols marcados e autores dos gols.

Além disso, na opção "relatório", é gerado um relatório do campeonato, informando os três primeiros colocados, o artilheiro e sua quantidade de gols, a equipe que mais sofreu gols e a quantidade, e a equipe que mais marcou gols e a quantidade.

### TelaCurso

Na TelaCurso, estão disponíveis as opções básicas de criação, consulta, edição e exclusão dos cursos.

### TelaEquipe

Na TelaEquipe, as opções são: criação, consulta, edição, exclusão, adição de alunos à equipe e remoção de alunos da equipe.

### TelaPartida

Na TelaPartida, além das opções básicas de criação, consulta, edição e exclusão, há a opção de realizar a partida, na qual são inseridos os gols e seus autores.

## Regras de Negócio

- A identificação dos alunos é feita pela matrícula. Portanto, uma mesma pessoa (CPF) pode ter duas matrículas, mas elas nunca poderão ser repetidas.
- Uma vez cadastrado, não é possível alterar a matrícula e o CPF do aluno.
- A identificação dos árbitros é feita pelo CPF, não permitindo duplicidade. O CPF não pode ser alterado após o cadastro.
- Os cursos são identificados pelo seu código, não sendo permitido o cadastro de cursos com o mesmo código, que não pode ser alterado.
- As equipes são identificadas pelo seu código, não sendo permitido o cadastro de equipes com o mesmo código, que não pode ser alterado.
- Uma equipe só pode ter alunos do seu curso.
- Cada curso deve ter pelo menos uma equipe.
- Cada equipe deve ter pelo menos 11 alunos.
- O sistema é capaz de gerenciar apenas um campeonato por vez.
- Para iniciar o campeonato, é necessário haver pelo menos duas equipes.
- Uma vez iniciado o campeonato, as partidas são geradas de modo que todas as equipes se enfrentem uma vez.
- Dados como data e árbitro da partida são gerados de maneira aleatória após a inicialização do campeonato.
- O usuário registra cada partida, inserindo o número de gols de cada equipe e seus autores. Não é possível editar uma partida após sua realização.
- O campeonato é finalizado pelo usuário.
- O critério para classificação dos times é a quantidade de pontos. O critério de desempate é o saldo de gols.
- Ao finalizar o campeonato, é gerado um relatório contendo informações sobre os três primeiros colocados e o artilheiro do campeonato.
- O programa é encerrado quando o campeonato é finalizado, não sendo possível fazer mais nenhuma alteração.
