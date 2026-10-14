# Relatório de qualidade — base de solicitações

| Problema | Linhas afetadas | O que eu fiz |
|---|---:|---|
| Linhas repetidas | 6 | Removi com `drop_duplicates()` |
| Categoria escrita de jeitos diferentes ou não reconhecida | 135 | Padronizei usando o dicionário `padrao`; valores não incluídos no dicionário ficam vazios para revisão |
| Status escrito de jeitos diferentes | 11 | Removi espaços e padronizei para inicial maiúscula |
| Prioridade escrita de jeitos diferentes ou não reconhecida | 10 | Padronizei os níveis conhecidos usando `padrao_prioridade`; valores não reconhecidos ficam vazios para revisão |
| Avaliação fora do intervalo de 1 a 5 | 2 | Desconsiderei essas notas no cálculo das médias |

**Resultado:** a base tinha 246 linhas antes da limpeza e ficou com 240 linhas após a remoção das duplicatas. A soma das quantidades por categoria foi 240, igual ao total da base limpa (240).
