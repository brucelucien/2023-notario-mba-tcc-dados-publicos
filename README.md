# 2023. Notario, Bruce. Trabalho de Conclusão de Curso. MBA em Ciências de Dados.

Repositório de dados públicos associados ao Trabalho de Conclusão de Curso (TCC) do MBA em Ciências de Dados iniciado por Bruce Notario no ano de 2023.

## Dados públicos

|Arquivo|Descrição|Detalhamento|Formato|
|---------------|------------|------------|------------|
|[space_dataset_final_anonimizado.csv](space_dataset_final_anonimizado.csv)|*Dataset* final construído durante o estudo e utilizado como base para o desenvolvimento de uma estratégia geral para **alocação de novos desenvolvedores em times de desenvolvimento**.|É uma **lista de desenvolvedores** de software obtida a partir de dados dos projetos *open source* da plataforma *.NET* ([github.com/dotnet](https://github.com/dotnet/)). Cada desenvolvedor está associado a um **time** (repositório/projeto) e a **estimativas** de seu nível de *satisfação e bem-estar*, *atividade* e *comunicação*. Os desenvolvedores cujo time associado é o *INDEFINIDO* são aqueles que ainda não tem time definido.|No formato CSV, o *dataset* é composto pelos atributos **ID** *(string, unique, not null)*, **TIME** *(string)*, **SATISFACAO** *(float, normalizado, intervalo [0; 1])*, **ATIVIDADE** *(float, normalizado, intervalo [0; 1])* e **COMUNICACAO** *(float, normalizado, intervalo [0; 1])*.|
