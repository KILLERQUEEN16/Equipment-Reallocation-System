from datetime import datetime, timezone
from uuid import uuid4

from fastapi import HTTPException

from app.models import MoveItemRequest, MoveItemResponse, StockRecord


class InventoryService:
    def __init__(self) -> None:
        # Estoque em memória para exemplo.
        self._stock: dict[tuple[str, str], StockRecord] = {
            ("NOTEBOOK-DELL-14", "SP-CENTRO"): StockRecord(
                item_id="NOTEBOOK-DELL-14", location_id="SP-CENTRO", quantity=10
            ),
            ("NOTEBOOK-DELL-14", "RJ-BARRA"): StockRecord(
                item_id="NOTEBOOK-DELL-14", location_id="RJ-BARRA", quantity=2
            ),
            ("MONITOR-24", "SP-CENTRO"): StockRecord(
                item_id="MONITOR-24", location_id="SP-CENTRO", quantity=15
            ),
        }

    def move_item(self, payload: MoveItemRequest) -> MoveItemResponse:
        source_key = (payload.item_id, payload.from_location_id)
        destination_key = (payload.item_id, payload.to_location_id)

        source = self._stock.get(source_key)
        if source is None:
            raise HTTPException(status_code=404, detail="Item não encontrado no local de origem")

        if source.quantity < payload.quantity:
            raise HTTPException(
                status_code=409,
                detail=(
                    "Saldo insuficiente no local de origem: "
                    f"disponível={source.quantity}, solicitado={payload.quantity}"
                ),
            )

        destination = self._stock.get(destination_key)
        if destination is None:
            destination = StockRecord(
                item_id=payload.item_id,
                location_id=payload.to_location_id,
                quantity=0,
            )
            self._stock[destination_key] = destination

        source.quantity -= payload.quantity
        destination.quantity += payload.quantity

        return MoveItemResponse(
            movement_id=str(uuid4()),
            item_id=payload.item_id,
            moved_quantity=payload.quantity,
            from_location_id=payload.from_location_id,
            to_location_id=payload.to_location_id,
            from_location_balance=source.quantity,
            to_location_balance=destination.quantity,
            moved_at=datetime.now(timezone.utc),
        )
