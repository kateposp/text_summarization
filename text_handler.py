import sys

from werkzeug import exceptions
import typing as tp
import nlpcloud


class Summarizer:

    def __init__(self) -> None:
        self.token = "4a1831cef3e573f1e56b820209c0f149feacc325"
        self.model_name = "bart-large-cnn"
        self.part_size = 750
        self.client = nlpcloud.Client(self.model_name, self.token)

    def summarize(self, text: str) -> str:
        paragraphs = self._split_text(text)
        answer = ""
        if len(paragraphs) > 3:
            raise exceptions.BadRequest("The text is too long")

        for paragraph in paragraphs:
            result = self.client.summarization(paragraph)
            answer += result["summary_text"]
        return answer

    def _split_text(self, text: str) -> tp.List[str]:
        paragraphs: tp.List[str] = text.split("\n")
        current_paragraph: str = ""
        answer: tp.List[str] = list()
        for paragraph in paragraphs:
            parts = self._split_paragraph(paragraph)
            answer.extend(self._concatenate_parts(current_paragraph, parts))
            current_paragraph = answer[-1]
            answer.pop()
        if current_paragraph != "":
            answer.append(current_paragraph)
        return answer

    def _split_paragraph(self, paragraph: str) -> tp.List[str]:
        if len(paragraph.split(' ')) <= self.part_size:
            return [paragraph]
        sentences: tp.List[str] = paragraph.split(".")
        return self._concatenate_parts("", sentences)

    def _concatenate_parts(self, current_paragraph: str, parts: tp.List[str]) -> tp.List[str]:
        answer: tp.List[str] = list()
        current_size: int = len(current_paragraph.split(' '))
        for part in parts:
            current_part_size: int = len(part.split(' '))
            if current_size + current_part_size <= self.part_size:
                current_paragraph += part
                current_size += current_part_size
            else:
                answer.append(current_paragraph)
                current_size = current_part_size
                current_paragraph = part

        answer.append(current_paragraph)
        return answer
