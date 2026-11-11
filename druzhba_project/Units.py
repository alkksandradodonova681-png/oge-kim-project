import base64

class Task():
    def __init__(self,text: str ,picture: base64) -> None:
        self.text = text
        self.picture = picture