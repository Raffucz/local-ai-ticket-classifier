from src.ollama import OllamaClient
import json
import requests

class TicketAutomation:
    def __init__(self, ollama_client, discord_webhook_url="SEU URL"):
        self.ollama_client = ollama_client
        self.discord_webhook_url = discord_webhook_url

    def enviar_para_discord(self, description, triage_result):
        # Cor vermelha para tickets críticos, amarela para os demais
        cor = 16711680 if triage_result.get("urgencia") == "Crítica" else 16766720
        
        payload = {
            "embeds": [{
                "title": "🚨 Novo Ticket Triado pela IA",
                "color": cor,
                "fields": [
                    {"name": "Departamento", "value": triage_result.get("departamento", "N/A"), "inline": True},
                    {"name": "Urgência", "value": triage_result.get("urgencia", "N/A"), "inline": True},
                    {"name": "Descrição Original", "value": description, "inline": False}
                ]
            }]
        }
        requests.post(self.discord_webhook_url, json=payload)

    def triage_ticket(self, ticket_description):
        system_prompt = """
        Você é um especialista em triagem de suporte de TI. 
        Analise a descrição do ticket e classifique-o.
        
        Opções de Urgência: [Baixa, Média, Alta, Crítica]
        Opções de Departamento: [Redes, Hardware, Banco de Dados, Desenvolvimento, Atendimento ao Cliente]
        
        Retorne APENAS um JSON válido no seguinte formato:
        {
            "urgencia": "sua_resposta",
            "departamento": "sua_resposta"
        }
        """
        
        response_text = self.ollama_client.chat(system_prompt, ticket_description)
        
        try:
            parsed_json = json.loads(response_text)
            
            # Envia o alerta para o Discord se a URL estiver configurada
            if self.discord_webhook_url != "COLE_SUA_URL_AQUI":
                self.enviar_para_discord(ticket_description, parsed_json)
                
            return parsed_json
        except json.JSONDecodeError:
            return {"error": "A IA não retornou um JSON válido", "raw_response": response_text}

    def generate_response(self, user_message):
        prompt = f"User: {user_message}\nAssistant:"
        response = self.ollama_client.generate(prompt)
        return response
