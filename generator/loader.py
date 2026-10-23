import json
import os

class Loader:
    def __init__(self, base_path="."):
        self.base_path = base_path

    def load_json(self, relative_path):
        full_path = os.path.join(self.base_path, relative_path)
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"Файл не найден: {full_path}")
        
        # Добавляем encoding="utf-8-sig" вместо "utf-8"
        with open(full_path, "r", encoding="utf-8-sig") as f:
            return json.load(f)

    def load_plan(self, subject="math"):
        return self.load_json(f"data/plans/plan_{subject}.json")

    def load_bank(self, subject="math"):
        return self.load_json(f"data/banks/bank_{subject}.json")