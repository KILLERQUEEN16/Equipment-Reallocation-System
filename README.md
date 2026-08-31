# Equipment Reallocation System

Sistema de apoio à realocação de equipamentos de TI, pensado para organizar transferências entre usuários, setores ou localidades com mais rastreabilidade e menos trabalho manual.

## Objetivo

Centralizar o processo de realocação de ativos, registrar movimentações e reduzir inconsistências em controles manuais.

## Problema

Em ambientes corporativos, mudanças de responsável ou localização de equipamentos podem gerar divergências entre inventário, usuário e ativo físico. Este projeto explora uma solução simples para registrar e acompanhar essas movimentações.

## Funcionalidades planejadas

- Cadastro e consulta de equipamentos
- Registro de usuário atual e destino
- Histórico de movimentações
- Status da solicitação
- Validação de dados antes da transferência
- Relatórios e filtros por ativo, usuário ou localidade

## Arquitetura proposta

```text
Interface / Cliente
        ↓
      API REST
        ↓
   Banco de dados
```

## Tecnologias

- Python
- FastAPI
- SQL / PostgreSQL
- REST API
- Git / GitHub

## Status

MVP em evolução. O foco atual é estruturar regras de negócio, persistência e rastreabilidade antes de ampliar a interface.

## O que este projeto demonstra

- Modelagem de fluxo operacional
- Organização de dados
- Desenvolvimento de APIs
- Persistência em banco relacional
- Pensamento orientado a redução de retrabalho
