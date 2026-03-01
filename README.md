# Equipment-Reallocation-System

API MVP para movimentar itens entre unidades/estoques.

## Como executar

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoint de movimentação

`POST /api/items/move`

Exemplo de payload:

```json
{
  "item_id": "NOTEBOOK-DELL-14",
  "from_location_id": "SP-CENTRO",
  "to_location_id": "RJ-BARRA",
  "quantity": 3,
  "reason": "Reposição do escritório",
  "requested_by": "julia.silva"
}
```

Resposta (exemplo):

```json
{
  "movement_id": "b7394f9e-1f95-4829-8c5d-5b4f8c17f813",
  "item_id": "NOTEBOOK-DELL-14",
  "moved_quantity": 3,
  "from_location_id": "SP-CENTRO",
  "to_location_id": "RJ-BARRA",
  "from_location_balance": 7,
  "to_location_balance": 5,
  "moved_at": "2026-03-01T12:00:00.000000+00:00"
}
```

## Regras implementadas

- Origem e destino não podem ser iguais.
- Quantidade deve ser maior que zero.
- Item precisa existir no estoque de origem.
- Não permite movimentação com saldo insuficiente.
- Cria o registro no destino caso ainda não exista.
