from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.ticket_service import TicketAutomation # Nome corrigido
from src.ollama import OllamaClient # Importação adicionada

app = FastAPI()
ollama_client = OllamaClient(model_name="llama3.1:latest") # Especifique o modelo que você tem baixado no Ollama
ticket_automation = TicketAutomation(ollama_client)

class TicketDescription(BaseModel):
    description: str

class UserMessage(BaseModel):
    message: str

@app.post("/triage-ticket/")
async def triage_ticket(ticket: TicketDescription):
    try:
        response = ticket_automation.triage_ticket(ticket.description)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-response/")
async def generate_response(message: UserMessage):
    try:
        response = ticket_automation.generate_response(message.message)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=2023)

