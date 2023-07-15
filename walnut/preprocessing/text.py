"""text preprocessing module"""

from __future__ import annotations
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from walnut.tensor import Tensor


def remove_punctuation(data: str):
    """Removes punctuation characters from a string.

    Parameters
    ----------
    data : str
        String containing punctuation characters.

    Returns
    ----------
    str
        Clean string.
    """
    punctuations = """!()-[]{};:'",<>./?@#$%^&*_~"""
    data_clean = data
    for punctuation in punctuations:
        data_clean = data_clean.replace(punctuation, "")

    for i in range(5):
        i = 5 - i
        data_clean = data_clean.replace("\n" * i, " ")
    return data_clean


@dataclass(slots=True)
class Tokenizer(ABC):
    """Tokenizer base class."""

    tokens: dict[str, int] = field(default_factory=dict)

    @property
    def vocab_size(self) -> int:
        """Number of tokens."""
        return len(self.tokens)

    @abstractmethod
    def fit(self, data: str, max_tokens: int = 100) -> None:
        """Fits the tokenizer to data."""

    @abstractmethod
    def encode(self, string: str) -> Tensor:
        """Encodes a string."""

    @abstractmethod
    def decode(self, tokens: Tensor) -> str:
        """Decodes tokens."""


@dataclass(slots=True)
class CharacterTokenizer(Tokenizer):
    """Creates character tokens."""

    oov_token: str = "|"

    def fit(self, data: str, max_tokens: int = 100) -> None:
        """Fits the tokenizer to data.

        Parameters
        ----------
        data : str
            Text the tokens should be extracted from.
        max_tokens : int, optional
            Maximum number of tokens to be generated, by default 100.
        """
        data_sorted = sorted(set(data))
        data_sorted.insert(0, self.oov_token)
        tokens = data_sorted[:max_tokens]
        self.tokens = {s: t for t, s in enumerate(tokens)}

    def encode(self, string: str) -> Tensor:
        """Encodes a string.

        Parameters
        ----------
        data : str
            String to be encoded.

        Returns
        -------
        Tensor
            Tokens.
        """
        return Tensor([self.tokens.get(s, 0) for s in string], dtype="int")

    def decode(self, tokens: Tensor) -> str:
        """Decodes tokens.

        Parameters
        ----------
        tokens : Tensor
            Tensor of integer tokens to be decoded.

        Returns
        -------
        str
            Concatenated tokens.
        """
        reverse_tokens = {t: s for t, s in enumerate(self.tokens)}
        return "".join(
            [reverse_tokens.get(token.item(), self.oov_token) for token in tokens.data]
        )


@dataclass(slots=True)
class WordTokenizer(Tokenizer):
    """Creates word tokens."""

    oov_token: str = "<OOV>"

    def fit(self, data: str, max_tokens: int = 100) -> None:
        """Fits the tokenizer to data.

        Parameters
        ----------
        data : str
            Text the tokens should be extracted from.
        max_tokens : int, optional
            Maximum number of tokens to be generated, by default 100.
        """
        data_clean = remove_punctuation(data).lower()
        data_split = data_clean.split(" ")
        # get unique elements
        data_unique = list(set(data_split))
        # sort elements by occurence in data
        data_sorted = sorted(data_unique, key=data_split.count, reverse=True)
        data_sorted.insert(0, self.oov_token)
        tokens = data_sorted[:max_tokens]
        self.tokens = {token: i for i, token in enumerate(tokens)}

    def encode(self, string: str) -> Tensor:
        """Encodes a string.

        Parameters
        ----------
        data : str
            String to be encoded.

        Returns
        -------
        Tensor
            Tokens.
        """
        string_clean = remove_punctuation(string.lower())
        string_split = string_clean.split(" ")
        return Tensor([self.tokens.get(s, 0) for s in string_split])

    def decode(self, tokens: Tensor) -> str:
        """Decodes a list of tokens.

        Parameters
        ----------
        tokens : Tensor
            Tensor of integer tokens to be decoded.

        Returns
        -------
        str
            Concatenated tokens.
        """
        reverse_tokens = {t: s for t, s in enumerate(self.tokens)}
        return " ".join(
            [reverse_tokens.get(token.item(), self.oov_token) for token in tokens.data]
        )