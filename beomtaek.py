from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from model import Beomtaek, BeomtaekItem, BeomtaekItems

beomtaek_router = APIRouter()
beomtaek_list = []

templates = Jinja2Templates(directory="templates/")

@beomtaek_router.post("/beomtaek")
async def add_beomtaek(request: Request, beomtaek: Beomtaek = Depends(Beomtaek.as_form)):
    beomtaek.id = len(beomtaek_list) + 1
    beomtaek_list.append(beomtaek)
    return templates.TemplateResponse("beomtaek.html",
    {
        "request": request,
        "beomtaeks": beomtaek_list
    })

@beomtaek_router.get("/beomtaek", response_model=BeomtaekItems)
async def retrieve_beomtaeks(request: Request):
    return templates.TemplateResponse("beomtaek.html", {
        "request": request,
        "beomtaeks": beomtaek_list
    })

@beomtaek_router.get("/beomtaek/{beomtaek_id}")
async def get_single_beomtaek(request: Request, beomtaek_id: int = Path(..., title="The ID of the beomtaek to retrieve.")) -> dict:
    for beomtaek in beomtaek_list:
        if beomtaek.id == beomtaek_id:
            return templates.TemplateResponse(
                    "beomtaek.html", {
                    "request": request,
                    "beomtaek": beomtaek
            })
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Beomtaek with supplied ID doesn't exist",
    )

@beomtaek_router.put("/beomtaek/{beomtaek_id}")
async def update_beomtaek(beomtaek_data: BeomtaekItem, beomtaek_id: int = Path(..., title="The ID of the beomtaek to be updated")) -> dict:
    for beomtaek in beomtaek_list:
        if beomtaek.id == beomtaek_id:
            beomtaek.item = beomtaek_data.item
            return {
                    "message": "Beomtaek updated successfully"
            }
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Beomtaek with supplied ID doesn't exist",
    )

@beomtaek_router.delete("/beomtaek/{beomtaek_id}")
async def delete_single_beomtaek(beomtaek_id: int) -> dict:
    for index in range(len(beomtaek_list)):
        beomtaek = beomtaek_list[index]
        if beomtaek.id == beomtaek_id:
            beomtaek_list.pop(index)
            return {
                    "message": "Beomtaek deleted successfully"
            }
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Beomtaek with supplied ID doesn't exist",
    )

@beomtaek_router.delete("/beomtaek")
async def delete_all_beomtaek() -> dict:
    beomtaek_list.clear()
    return {
            "message": "Beomtaeks deleted successfully"
    }
