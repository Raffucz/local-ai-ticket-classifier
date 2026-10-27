from src.ollama import OllamaClient

class TicketAutomation:
    def __init__(self, ollama_client):
        self.ollama_client = ollama_client

    def triage_ticket(self, ticket_description):
        system_prompt = """
        You are a ticket triage system. Given a ticket description, you need to determine the priority and category of the ticket.
        Priorities: Low, Medium, High
        Categories: Support, Bug, Feature Request
        """
        response = self.ollama_client.chat(system_prompt, ticket_description)
        return response

    def generate_response(self, user_message):
        prompt = f"User: {user_message}\nAssistant:"
        response = self.ollama_client.generate(prompt)
        return response
