import random

class Generator:
    def __init__(self, plan, bank):
        self.plan = plan
        self.bank = bank

    def generate_variant(self, variant_id):
        variant_tasks = []
        
        for pos in self.plan["positions"]:
            pos_id = pos["positionId"]
            topic_id = pos["allowedTopics"][0]
            
            # Ищем все подходящие задания по позиции и теме
            candidates = [
                t for t in self.bank 
                if t["positionId"] == pos_id and t["topicId"] == topic_id
            ]
            
            if not candidates:
                raise ValueError(f"Нет заданий для позиции {pos_id}")
            
            # Пока у нас по 1 прототипу на позицию. 
            # Если будет 2 и больше, random.choice выберет случайный
            chosen_task = random.choice(candidates)
            variant_tasks.append(chosen_task)
            
        return {
            "variantId": variant_id,
            "tasks": variant_tasks
        }