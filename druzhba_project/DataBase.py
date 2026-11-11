import pandas as pd

DATA_LOCAL_TABLE_PATH = "data.json"
COLUMNS = ["taskId","subjectId", "position", "prototypeId", "difficulty", "typeAns", "task"]
SORT_KEYS = ["subjectID", "position", "prototypeID", "difficulty", "univ_iden_num"]


class Image: pass

class DB:
    def __init__(self):
        self.df_data = None



    def create(self)-> pd.DataFrame:
        self.df_data = pd.DataFrame({
        "taskId": pd.Series(dtype="Int64"),
        "subjectId": pd.Series(dtype="str"),
        "position": pd.Series(dtype="Int64"),
        "prototype": pd.Series(dtype="Int64"),
        "difficulty": pd.Series(dtype="Int64"),
        "typeAns": pd.Series(dtype="str"),
        "task": pd.Series(dtype="str"),
    })
        return self.df_data
        
        


    def load(self):
        self.df_data = pd.read_json(DATA_LOCAL_TABLE_PATH)
        return self.df_data
        

    def save(self) -> None:
        self.df_data.to_json(DATA_LOCAL_TABLE_PATH, orient="records", force_ascii=False, indent=2)


    def push(self, task_id: int, subject_id: str, position: int, prototype: int, difficulty: int, type_ans: str, task: str) -> None:
        new_row = pd.DataFrame([{
            "taskId": task_id,
            "subjectId": subject_id,
            "position": position,
            "prototype": prototype,
            "difficulty": difficulty,
            "typeAns": type_ans,
            "task": task,
        }])
        self.df_data = pd.concat([self.df_data, new_row], ignore_index=True)
        self.df_data = self.df_data.sort_values(
            by=SORT_KEYS, ascending=True, ignore_index=True,
        )


    def delete(self, task_id: int) -> None:
        idx = self.df_data.index[self.df_data["taskId"] == task_id]
        self.df_data = self.df_data.drop(idx)                   
        self.df_data = self.df_data.reset_index(drop=True)


    def get(self, subject_id: str, task_id = None, position = None, prototype = None, difficulty = None, type_ans = None, task = None) -> list[dict]:
        mask = self.df_data["subjectId"] == subject_id
        if task_id is not None:
            mask &= self.df_data["taskId"] == task_id 
        if position is not None:
            mask &= self.df_data["position"] == position
        if prototype is not None:
            mask &= self.df_data["prototype"] == prototype
        if difficulty is not None:
            mask &= self.df_data["difficulty"] == difficulty
        if type_ans is not None:
            mask &= self.df_data["typeAns"] == type_ans
        if task is not None:
            mask &= self.df_data["task"] == task
        return self.df_data[mask].to_dict(orient="records")