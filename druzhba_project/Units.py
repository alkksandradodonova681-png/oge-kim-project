import base64

class Task():
    def __init__(self, text: str, picture: list = None, answer: str = "", answer_images: list = None) -> None:
        self.text = text
        self.picture = picture if picture is not None else []
        self.answer = answer
        self.answer_images = answer_images if answer_images is not None else []