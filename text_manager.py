import typing as tp


class TextManager:

    def __init__(self):
        self.text: tp.Optional[str] = None

    def set_text(self, text: str) -> None:
        self.text = text

    def get_summarized_text(self) -> str:
        if self.text is None:
            raise RuntimeError("There is no value")
        else:
            end = min(21, len(self.text))
            return self.text[:end]
