class Validator:
    def __init__(self, plan, bank):
        self.plan = plan
        self.bank = bank
        self.errors = []

    def validate(self):
        # 1. Проверяем, что для каждой позиции плана есть задание в банке
        for pos in self.plan["positions"]:
            pos_id = pos["positionId"]
            topic_id = pos["allowedTopics"][0]
            
            found = False
            for task in self.bank:
                if task["positionId"] == pos_id and task["topicId"] == topic_id:
                    found = True
                    break
            
            if not found:
                self.errors.append(f"Нет задания для позиции {pos_id} (тема {topic_id})")

        # 2. Проверяем сумму баллов (в плане maxPoints может быть 31, но в банке сумма всех maxPoints тоже должна быть 31)
        total_max_points = sum(task["maxPoints"] for task in self.bank)
        if total_max_points != self.plan["maxPoints"]:
            self.errors.append(f"Сумма баллов в банке ({total_max_points}) не совпадает с планом ({self.plan['maxPoints']})")

        return len(self.errors) == 0, self.errors