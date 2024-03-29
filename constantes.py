#
# GERAIS
SEED = 42
INDICADOR_DEV_DISPONIVEL = "INDEFINIDO"
#
# DATASETS
ENDERECO_DATASET_DESENVOLVEDORES = "space_dataset_final_anonimizado.csv"
ENDERECO_DATASET_SOLUCOES_ENCONTRADAS = "./solucoes/solucoes_encontradas"
#
# IMAGENS
ENDERECO_IMAGENS = "./imagens/"
#
# LATEX
ENDERECO_LATEX = "./latex/"
#
# LOGS
ENDERECO_LOG_OTIMIZACAO = "./log/log_otimizacao"
#
# HYPERVOLUME
ENDERECO_HYPERVOLUME_SOLUCOES_ENCONTRADAS = "./hypervolume/hypervolume.csv"
ENDERECO_CONVERGENCIA_HYPERVOLUME = "./convergencia/convergencia"
#
# EXPERIMENTOS
EXPERIMENTOS = [
    {"POPULACAO": 1500, "GERACOES": 100, "DESCENDENTES": 0.7}, # 0
    {"POPULACAO": 1500, "GERACOES": 50, "DESCENDENTES": 0.7},
    {"POPULACAO": 1375, "GERACOES": 100, "DESCENDENTES": 0.7},
    {"POPULACAO": 1250, "GERACOES": 1000, "DESCENDENTES": 0.7},
    {"POPULACAO": 1250, "GERACOES": 100, "DESCENDENTES": 0.7},

    {"POPULACAO": 1125, "GERACOES": 100, "DESCENDENTES": 0.7}, # 5
    {"POPULACAO": 1000, "GERACOES": 500, "DESCENDENTES": 0.7},
    {"POPULACAO": 1000, "GERACOES": 200, "DESCENDENTES": 0.7},
    {"POPULACAO": 1000, "GERACOES": 150, "DESCENDENTES": 0.9},
    {"POPULACAO": 1000, "GERACOES": 150, "DESCENDENTES": 0.7},

    {"POPULACAO": 1000, "GERACOES": 150, "DESCENDENTES": 0.3}, # 10
    {"POPULACAO": 1000, "GERACOES": 100, "DESCENDENTES": 0.7},
    {"POPULACAO": 1000, "GERACOES": 50, "DESCENDENTES": 0.7},
    {"POPULACAO": 680, "GERACOES": 230, "DESCENDENTES": 0.7},
    {"POPULACAO": 500, "GERACOES": 100, "DESCENDENTES": 0.7},

    {"POPULACAO": 500, "GERACOES": 50, "DESCENDENTES": 0.7}, # 15
    {"POPULACAO": 100, "GERACOES": 1000, "DESCENDENTES": 0.7},
    {"POPULACAO": 100, "GERACOES": 500, "DESCENDENTES": 0.7},
    {"POPULACAO": 100, "GERACOES": 300, "DESCENDENTES": 0.7},
    {"POPULACAO": 100, "GERACOES": 250, "DESCENDENTES": 0.7},

    {"POPULACAO": 100, "GERACOES": 200, "DESCENDENTES": 0.7}, # 20
    {"POPULACAO": 100, "GERACOES": 150, "DESCENDENTES": 0.8},
    {"POPULACAO": 100, "GERACOES": 150, "DESCENDENTES": 0.7},
    {"POPULACAO": 100, "GERACOES": 150, "DESCENDENTES": 0.3},
    {"POPULACAO": 100, "GERACOES": 100, "DESCENDENTES": 0.7},

    {"POPULACAO": 100, "GERACOES": 50, "DESCENDENTES": 0.7}, # 25
    {"POPULACAO": 1000, "GERACOES": 2000, "DESCENDENTES": 0.7},
    {"POPULACAO": 100, "GERACOES": 2000, "DESCENDENTES": 0.7},
    {"POPULACAO": 500, "GERACOES": 2000, "DESCENDENTES": 0.7},
    {"POPULACAO": 500, "GERACOES": 3000, "DESCENDENTES": 0.7},

    {"POPULACAO": 500, "GERACOES": 4000, "DESCENDENTES": 0.7}, #30,
    {"POPULACAO": 100, "GERACOES": 4000, "DESCENDENTES": 0.7},
    {"POPULACAO": 100, "GERACOES": 10000, "DESCENDENTES": 0.7},
    {"POPULACAO": 100, "GERACOES": 10000, "DESCENDENTES": 0.3},
    {"POPULACAO": 100, "GERACOES": 10000, "DESCENDENTES": 0.9},

    {"POPULACAO": 500, "GERACOES": 4000, "DESCENDENTES": 0.3}, #35
    {"POPULACAO": 500, "GERACOES": 8000, "DESCENDENTES": 0.3},
    {"POPULACAO": 500, "GERACOES": 8000, "DESCENDENTES": 0.5}
]
#
# HIPERPARAMETROS
HIPERPARAMETROS = EXPERIMENTOS[-2]  # TODO Aqui você escolhe o experimento.
#
# OTIMIZAÇÃO
TAMANHO_POPULACAO_INICIAL = HIPERPARAMETROS["POPULACAO"]
PERCENTUAL_DESCENDENTES_EM_RELACAO_AO_TAMANHO_DA_POPULACAO_INICIAL = HIPERPARAMETROS[
    "DESCENDENTES"
]
QUANTIDADE_DE_GERACOES_QUE_DEFINEM_O_TERMINO_DA_OTIMIZACAO = HIPERPARAMETROS["GERACOES"]
#
# CALCULADAS
QUANTIDADE_DESCENDENTES = int(
    round(
        TAMANHO_POPULACAO_INICIAL
        * PERCENTUAL_DESCENDENTES_EM_RELACAO_AO_TAMANHO_DA_POPULACAO_INICIAL
    )
)
RESUMO_EXECUCAO = {
    "POP_SIZE": TAMANHO_POPULACAO_INICIAL,
    "N_OFFSPRINGS": QUANTIDADE_DESCENDENTES,
    "N_GEN": QUANTIDADE_DE_GERACOES_QUE_DEFINEM_O_TERMINO_DA_OTIMIZACAO,
}
IDENTIFICADOR_EXECUCAO = "".join(
    ["." + key + "_" + str(RESUMO_EXECUCAO[key]) for key in RESUMO_EXECUCAO]
)
