import pandas as pd

DATA_LOCAL_TABLE_PATH = "new_project/data.json"
COLUMNS = ["univ_iden_num","subject", "num_in_order", "prototype", "difficulty", "task"]
SORT_KEYS = ["subject", "num_in_order", "prototype", "difficulty", "univ_iden_num"]


class Image: pass

class DB:
    def __init__(self):
        self.df_data = None



    def create(self)-> pd.DataFrame:
        self.df_data = pd.DataFrame({
        "univ_iden_num": pd.Series(dtype="Int64"),
        "subject":      pd.Series(dtype="str"),
        "num_in_order": pd.Series(dtype="Int64"),
        "prototype":    pd.Series(dtype="Int64"),
        "difficulty":   pd.Series(dtype="Int64"),
        "task":         pd.Series(dtype="str"),
    })
        return self.df_data
        
        


    def load(self):
        self.df_data = pd.read_json(DATA_LOCAL_TABLE_PATH)
        return self.df_data
        

    def save(self) -> None:
        self.df_data.to_json(DATA_LOCAL_TABLE_PATH, orient="records", force_ascii=False, indent=2)


    def push(self, univ_iden_num: int, subject: str, num_in_order: int, prototype: int, difficulty: int, task: str) -> None:
        new_row = pd.DataFrame([{
            "univ_iden_num": univ_iden_num,
            "subject": subject,
            "num_in_order": num_in_order,
            "prototype": prototype,
            "difficulty": difficulty,
            "task": task,
        }])
        self.df_data = pd.concat([self.df_data, new_row], ignore_index=True)
        self.df_data = self.df_data.sort_values(
            by=SORT_KEYS, ascending=True, ignore_index=True,
        )


    def delete(self, univ_iden_num: int) -> None:
        idx = self.df_data.index[self.df_data["univ_iden_num"] == univ_iden_num]
        self.df_data = self.df_data.drop(idx, ignore_index=True)


    def get(self, subject: str, univ_iden_num = None, num_in_order = None, prototype = None, difficulty = None, task = None) -> list[dict]:
        mask = self.df_data["subject"] == subject
        if univ_iden_num is not None:
            mask &= self.df_data["univ_iden_num"] == univ_iden_num 
        if num_in_order is not None:
            mask &= self.df_data["num_in_order"] == num_in_order
        if prototype is not None:
            mask &= self.df_data["prototype"] == prototype
        if difficulty is not None:
            mask &= self.df_data["difficulty"] == difficulty
        if task is not None:
            mask &= self.df_data["task"] == task
        return self.df_data[mask].to_dict(orient="records")