from fastapi import FastAPI

from app.models import MoveItemRequest, MoveItemResponse
from app.service import InventoryService

app = FastAPI(
    title="Equipment Reallocation API",
    version="1.0.0",
    description="API para movimentação de itens entre locais",
)

inventory_service = InventoryService()


@app.post("/api/items/move", response_model=MoveItemResponse, tags=["Movimentação"])
def move_item(payload: MoveItemRequest) -> MoveItemResponse:
    """Move um item de um local de origem para um local de destino."""
    return inventory_service.move_item(payload)


@app.get("/health", tags=["Infra"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}
