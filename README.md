# SCTec

## Requisitos

- Linux, macOS ou Windows.
- Conexão com a internet para instalar o `uv` e o Python.

## Instalar o uv

No Linux ou macOS, execute o instalador oficial:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

No Windows, execute este comando no PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Abra um novo terminal e confirme a instalação:

```sh
uv --version
```

## Instalar o Python mais recente

Na raiz do projeto, instale a versão estável mais recente do Python gerenciada pelo `uv`:

```sh
uv python install
```

O projeto requer Python 3.14 ou superior.

## Instalar as dependências

Ainda na raiz do projeto, sincronize o ambiente e instale as dependências declaradas no `pyproject.toml` e no `uv.lock`:

```sh
uv sync
```

Esse comando cria o ambiente virtual `.venv` se necessário.

## Executar o script

```sh
uv run python src/01_lesson/main.py
```

O script lê `src/01_lesson/data/estimativa_dou_2026.xlsx`, grava ou atualiza `src/01_lesson/data/brazilian_population.csv` e imprime até 20 linhas do CSV.
