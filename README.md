# VENESIS

> One origin. Multiple minds.

Coleção autoral de cinco agentes especializados, inspirados em pioneiros da tecnologia e do design. Generation 01 — v0.1.0 (desenvolvimento).

| Agente | Especialidade |
|---|---|
| V-01 Berners | Front-end |
| V-02 Turing | Back-end |
| V-03 Uncle Bob | QA e qualidade |
| V-04 Codd | Dados |
| V-05 Rams | Design e direção criativa |

## Uso com Codex e OpenCode

Clone este repositório. Execute `python3 scripts/install.py /caminho/do/projeto` para gerar as configurações locais a partir das fontes em `agents/` e `core/`. Use `--help` para opções. No Windows, use `py -3` em vez de `python3`. O instalador não sobrescreve arquivos sem `--force`. Reinicie a sessão do Codex e solicite o especialista pelo nome. A disponibilidade de subagentes e ferramentas depende da versão e permissões do ambiente.

As regras de cada projeto continuam em seu próprio AGENTS.md. Nenhuma integração externa é configurada automaticamente. Rams pode planejar e produzir criativos quando houver ferramentas disponíveis; publicar exige autorização explícita.

## Status

Versão inicial em desenvolvimento; compatibilidade de execução ainda precisa ser validada no Codex. Inspirado em figuras históricas, sem afiliação ou representação dessas pessoas.

## Instalação multiplataforma (Python 3.11+)

```sh
python scripts/install.py /caminho/do/projeto --target codex
python scripts/install.py /caminho/do/projeto --target opencode
python scripts/install.py /caminho/do/projeto --target all
```

Use `--dry-run` para prévia e `--agents berners rams` para selecionar especialistas. OpenCode recebe agentes Markdown em `.opencode/agents/`, com `mode: subagent`. Codex recebe TOML em `.codex/agents/`. Nenhum modelo é fixado; a configuração e permissões existentes permanecem intactas. Valide a descoberta dos agentes na versão instalada. Consulte [OpenCode](https://opencode.ai/docs/agents/).
