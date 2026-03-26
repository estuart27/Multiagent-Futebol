from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import server # Importa o arquivo criado acima

app = FastAPI(title="Painel Multi-Agentes Esportivos")
templates = Jinja2Templates(directory="templates")

class Consulta(BaseModel):
    confronto: str

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Renderiza o painel principal."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analisar")
async def analisar_confronto(consulta: Consulta):
    """Inicia a cadeia de agentes e retorna a conversa."""
    resultado_comite = server.executar_comite_esportivo(consulta.confronto)
    return {"status": "sucesso", "conversa": resultado_comite}