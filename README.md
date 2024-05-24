# forca

Um exemplo de agente inteligente feito com Python e Prolog.

## Executar localmente

Para executar, você precisa instalar:

- [Python](https://www.python.org/downloads/)
- [SWI Prolog](https://www.swi-prolog.org/download/stable)
- [swipl](https://github.com/yuce/pyswip) - Biblioteca para integração do Prolog com Python
  - A release atual (v0.2.10) não funciona, compile a partir da fonte:

  ```
  pip install git+https://github.com/yuce/pyswip@master#egg=pyswip 
  ```
E então, execute o script:

```
python agent.py
```

Importante: Se tiver o seguinte erro:

```
SWI-Prolog: [FATAL ERROR:
        Could not find system resources]
```

Altere a variável de ambiente `SWI_HOME_DIR` no `agent.py` para o seu diretório de instalação do SWI Prolog

## Lista de palavras

Você precisa fornecer uma lista de palavras para utilizar o agente. Baixe o arquivo "br-sem-acentos.txt", disponível em [https://www.ime.usp.br/~pf/dicios/](https://www.ime.usp.br/~pf/dicios/)

Para a conversão, você pode utilizar o script disponível em `words.py`. Após a execução, um arquivo `words.pl` será gerado, pronto para uso.
