from text_handler import Summarizer

import typing as tp


class TextManager:
    def __init__(self) -> None:
        self.text: tp.Optional[str] = None
        self.summarizer = Summarizer()

    def set_text(self, text: str) -> None:
        self.text = text

    def get_summarized_text(self) -> str:
        if self.text is None:
            raise RuntimeError("There is no value")
        else:
            answer = self.summarizer.summarize(self.text)
            return answer
