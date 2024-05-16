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

Importante: Se tiver o seguinte erro:

```
SWI-Prolog: [FATAL ERROR:
        Could not find system resources]
```

Defina a variável de ambiente `SWI_HOME_DIR` como o seu diretório de instalação do SWI Prolog (geralmente `C:\Program Files\swipl`)
