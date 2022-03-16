#
# Copyright 2019-2021 Lukas Schmelzeisen
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import (
    Any,
    ContextManager,
    Iterable,
    MutableMapping,
    Optional,
    TextIO,
    TypeVar,
    Union,
)

_T = TypeVar("_T")

class tqdm(Iterable[_T], ContextManager["tqdm[None]"]):  # noqa: N801
    # Using T_=None for ContextManager so that tqdm() can be called without specifying a
    # type. Not sure exactly why that works.
    def __init__(
        self,
        iterable: Iterable[_T] = ...,
        desc: Optional[str] = ...,
        total: Optional[Union[int, float]] = ...,
        leave: bool = ...,
        # file
        ncols: Optional[int] = ...,
        mininterval: float = ...,
        maxinterval: float = ...,
        miniters: Optional[Union[int, float]] = ...,
        ascii: Optional[Union[bool, str]] = ...,  # noqa: A002
        disable: bool = ...,
        unit: str = ...,
        unit_scale: Union[bool, int, float] = ...,
        dynamic_ncols: bool = ...,
        smoothing: float = ...,
        bar_format: Optional[str] = ...,
        initial: Union[int, float] = ...,
        position: Optional[int] = ...,
        postfix: Optional[Any] = ...,
        unit_divisor: Union[int, float] = ...,
        write_bytes: Optional[bool] = ...,
        # lock_args
        nrows: Optional[int] = ...,
        gui: bool = ...,
    ): ...
    def __iter__(self) -> Iterator[_T]: ...
    @property
    def format_dict(self) -> MutableMapping[str, object]: ...
    def format_meter(
        self,
        n: Union[int, float],
        total: Union[int, float],
        elapsed: float,
        ncols: Optional[int] = ...,
        prefix: str = ...,
        ascii: Union[bool, str] = ...,  # noqa: A002
        unit: str = ...,
        unit_scale: Union[bool, int, float] = ...,
        rate: Optional[float] = ...,
        bar_format: Optional[str] = ...,
        postfix: object = ...,
        unit_divisor: float = ...,
        **extra_kwargs: object,
    ) -> str: ...
    def refresh(
        self,
        nolock: bool = ...,
        lock_args: Optional[Any] = ...,
    ) -> bool: ...
    def update(self, n: Union[int, float] = ...) -> None: ...
    @classmethod
    def write(
        cls, s: str, file: Optional[TextIO] = ..., end: str = ..., nolock: bool = ...
    ) -> None: ...
    def close(self) -> None: ...
    n: Union[int, float] = ...

class trange(tqdm[int]):  # noqa: N801
    def __init__(
        self,
        start: int,
        stop: Optional[int] = ...,
        step: Optional[int] = ...,
        desc: Optional[str] = ...,
        total: Optional[Union[int, float]] = ...,
        leave: bool = ...,
        # file
        ncols: Optional[int] = ...,
        mininterval: float = ...,
        maxinterval: float = ...,
        miniters: Optional[Union[int, float]] = ...,
        ascii: Optional[Union[bool, str]] = ...,  # noqa: A002
        disable: bool = ...,
        unit: str = ...,
        unit_scale: Union[bool, int, float] = ...,
        dynamic_ncols: bool = ...,
        smoothing: float = ...,
        bar_format: Optional[str] = ...,
        initial: Union[int, float] = ...,
        position: Optional[int] = ...,
        postfix: Optional[Any] = ...,
        unit_divisor: Union[int, float] = ...,
        write_bytes: Optional[bool] = ...,
        # lock_args
        nrows: Optional[int] = ...,
        gui: bool = ...,
    ): ...
