class Settings:
    def __init__(self, model_name: str, role: str, prompt: str):
        self.model_name = model_name
        self.role = role
        self.prompt = prompt

    def export_settings(self):
        return dict(model_name=self.model_name, role=self.role, prompt=self.prompt)
