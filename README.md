# 2024. Notario, Bruce. Trabalho de Conclusão de Curso. MBA em Ciências de Dados.

Repositório de dados públicos associados ao [Trabalho de Conclusão de Curso (TCC)](tcc/2024_NOTARIO_MBA_TCC.pdf) do MBA em Ciências de Dados iniciado por Bruce Notario no ano de 2023 e concluído em 2024.

## Dados públicos

|Arquivo|Descrição|Detalhamento|Formato|
|---------------|------------|------------|------------|
|[space_dataset_final_anonimizado.csv](space_dataset_final_anonimizado.csv)|*Dataset* final construído durante o estudo e utilizado como base para o desenvolvimento de uma estratégia geral para **alocação de novos desenvolvedores em times de desenvolvimento**.|É uma **lista de 180 desenvolvedores de software** obtida a partir de dados dos projetos *open source* da plataforma *.NET* ([github.com/dotnet](https://github.com/dotnet/)). Cada desenvolvedor está associado a um **time** (repositório/projeto) e a **estimativas** de seu nível de *satisfação e bem-estar*, *atividade* e *comunicação*. Os 33 desenvolvedores cujo time associado é o *INDEFINIDO* são aqueles que ainda não tem time definido.|No formato CSV, o *dataset* é composto pelos atributos **ID** *(string, unique, not null)*, **TIME** *(string)*, **SATISFACAO** *(float, normalizado, intervalo [0; 1])*, **ATIVIDADE** *(float, normalizado, intervalo [0; 1])* e **COMUNICACAO** *(float, normalizado, intervalo [0; 1])*.|
|[experimento.ipynb](experimento.ipynb)|Notebook utilizado para busca por soluções do problema de otimização.|Contém a implementação do problema proposto com o uso da biblioteca **pymoo** ([pymoo.org/](https://pymoo.org/)) e foco em **NSGA-II**. Também contém outras implementações utilizadas para avaliação do problema, como o cálculo do *hypervolume* associado a cada conjunto de soluções ótimas.|Faz uso do arquivo [dataset final](space_dataset_final_anonimizado.csv) e gera arquivos de logs, arquivos CSV com as soluções ótimas encontradas e atualiza um arquivo com todas as medias de *hypervolume* encontradas em cada experimento.|
