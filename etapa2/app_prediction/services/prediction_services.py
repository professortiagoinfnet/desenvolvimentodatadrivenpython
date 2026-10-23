class Predictor:
    def __init__(self, prompt):
        self.prompt = prompt
        self.response = ""

    def run(self):
        
        if self.prompt == "Em qual continente fica o Brasil?":
            self.response = "América do Sul"
            return self.response
        else:
            self.response = "Desculpe, não posso responder essa pergunta no momento."
            return self.response
