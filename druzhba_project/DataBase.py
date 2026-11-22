import pandas as pd
import json


class Image: pass

class DB:
    def __init__(self, path: str = "data.json"):
        self.path = path
        self.df_data = None


    def create(self) -> pd.DataFrame:
        self.df_data = pd.DataFrame({
        "taskId": pd.Series(dtype="Int64"),
        "subjectId": pd.Series(dtype="str"),
        "positionId": pd.Series(dtype="Int64"),
        "prototypeId": pd.Series(dtype="Int64"),
        "topicId": pd.Series(dtype="str"),
        "difficulty": pd.Series(dtype="Int64"),
        "typeAns": pd.Series(dtype="str"),
        "text": pd.Series(dtype="str"),
        "image": pd.Series(dtype="object"),
        "answer": pd.Series(dtype="str"),
        "answerImages": pd.Series(dtype="object")
    })
        return self.df_data
        

    def load(self):
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                raw = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.create()
            return self.df_data
        self.df_data = pd.DataFrame(raw)
        for col in ["taskId", "positionId", "prototypeId", "difficulty"]:
            if col in self.df_data.columns:
                self.df_data[col] = self.df_data[col].astype("Int64")
        if "answer" not in self.df_data.columns:
            self.df_data["answer"] = ""
        return self.df_data
        

    def save(self) -> None:
        data = self.df_data.to_dict(orient="records")
        for item in data:
            if isinstance(item.get("image"), list):
                item["image"] = [str(x) for x in item["image"]]
            elif item.get("image") is None:
                item["image"] = []
            if isinstance(item.get("answerImages"), list):
                item["answerImages"] = [str(x) for x in item["answerImages"]]
            elif item.get("answerImages") is None:
                item["answerImages"] = []
            if item.get("answer") is None:
                item["answer"] = ""
            #приводим numpy-типы к обычным для json
            for k in ["taskId", "positionId", "prototypeId", "difficulty"]:
                if k in item and item[k] is not None:
                    try:
                        item[k] = int(item[k])
                    except (ValueError, TypeError):
                        pass
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


    def push(self, task_id: int, subject_id: str, position_id: int, prototype_id: int, topic_id: str, difficulty: int, type_ans: str, text: str, image: list = None, answer: str = "", answer_images: list = None) -> None:
        if image is None:
            image = []
        if answer_images is None:
            answer_images = []
        new_row = pd.DataFrame([{
            "taskId": task_id,
            "subjectId": subject_id,
            "positionId": position_id,
            "prototypeId": prototype_id,
            "topicId": topic_id,
            "difficulty": difficulty,
            "typeAns": type_ans,
            "text": text,
            "image": image,
            "answer": answer,
            "answerImages": answer_images
        }])
        self.df_data = pd.concat([self.df_data, new_row], ignore_index=True)
        self.df_data = self.df_data.sort_values(
            by=["subjectId", "positionId", "prototypeId", "difficulty", "taskId"],
            ascending=True, ignore_index=True,
        )


    def delete(self, task_id: int) -> None:
        if task_id not in self.df_data["taskId"].values:
            return False
        idx = self.df_data.index[self.df_data["taskId"] == task_id]
        self.df_data = self.df_data.drop(idx)                   
        self.df_data = self.df_data.reset_index(drop=True)
        return True


    def get(self, subject_id: str, task_id = None, position_id = None, prototype_id = None, topic_id = "", difficulty = None, type_ans = None, text = None, image = None, answer = None) -> list[dict]:
        mask = self.df_data["subjectId"] == subject_id
        if task_id is not None:
            mask &= self.df_data["taskId"] == task_id 
        if position_id is not None:
            mask &= self.df_data["positionId"] == position_id
        if prototype_id is not None:
            mask &= self.df_data["prototypeId"] == prototype_id
        if topic_id is not None:
            mask &= self.df_data["topicId"] == topic_id
        if difficulty is not None:
            mask &= self.df_data["difficulty"] == difficulty
        if type_ans is not None:
            mask &= self.df_data["typeAns"] == type_ans
        if text is not None:
            mask &= self.df_data["text"] == text
        if image is not None:
            mask &= self.df_data["image"] == image
        if answer is not None:
            mask &= self.df_data["answer"] == answer
        return self.df_data[mask].to_dict(orient="records")