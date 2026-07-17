from dataclasses import dataclass


@dataclass(slots=True)
class Document:

    name: str

    content: str

    source: str = "local"