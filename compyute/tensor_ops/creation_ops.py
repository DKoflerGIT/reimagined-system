"""Tensor creation and combination operations."""

from collections.abc import Sequence
from typing import Optional

from ..backend import Device, select_device
from ..tensors import DimLike, ShapeLike, Tensor
from ..typing import DType, ScalarLike, select_dtype

__all__ = [
    "append",
    "arange",
    "concat",
    "empty",
    "empty_like",
    "full",
    "full_like",
    "identity",
    "linspace",
    "ones",
    "ones_like",
    "split",
    "stack",
    "zeros",
    "zeros_like",
]


def append(x: Tensor, values: Tensor, dim: int = -1) -> Tensor:
    """Returns a copy of the tensor with appended values.

    Parameters
    ----------
    x : Tensor
        Input tensor.
    values : Tensor
        Values to append.
    dim : int, optional
        Dimension along which to append the values. Defaults to ``-1``.

    Returns
    -------
    Tensor
        Tensor containing appended values.
    """
    return Tensor(x.device.module.append(x.data, values.data, axis=dim))


def arange(
    stop: int | float,
    start: int | float = 0.0,
    step: int | float = 1.0,
    *,
    device: Optional[Device] = None,
    dtype: Optional[DType] = None,
) -> Tensor:
    """Returns a tensor of evenly spaced values using a step size within
    a given interval .:math:`[start, stop)`.

    Parameters
    ----------
    stop : int | float
        Stop value (not included).
    start : int | float, optional
        Start value. Defaults to ``0``.
    step : int | float, optional
        Spacing between values. Defaults to ``1``.
    device : Device, optional
        The device the tensor is stored on. Defaults to ``None``.
    dtype : DtypeLike, optional
        Datatype of the tensor data. Defaults to ``None``.

    Returns
    -------
    Tensor
        Tensor of evenly spaced samples.
    """
    device = select_device(device)
    dtype = select_dtype(dtype)
    return Tensor(device.module.arange(start, stop, step, dtype.t))


def concat(tensors: Sequence[Tensor], dim: DimLike = -1) -> Tensor:
    """Returns a new tensor by joining a sequence of tensors along a given dimension.

    Parameters
    ----------
    tensors : Sequence[Tensor]
        Sequence of Tensors to be joined.
    dim : DimLike, optional
        Dimension along which to join the tensors. Defaults to ``-1``.

    Returns
    -------
    Tensor
        Concatenated tensor.
    """
    data = tensors[0].device.module.concatenate([t.data for t in tensors], axis=dim)
    return Tensor(data)


def empty(
    shape: ShapeLike,
    *,
    device: Optional[Device] = None,
    dtype: Optional[DType] = None,
) -> Tensor:
    """Returns an tensor with uninitialized values.

    Parameters
    ----------
    shape : ShapeLike
        Shape of the new tensor.
    device : Device, optional
        The device the tensor is stored on. Defaults to ``None``.
    dtype : DtypeLike, optional
        Datatype of the tensor data. Defaults to ``None``.

    Returns
    -------
    Tensor
        Tensor with uninitialized values.
    """
    device = select_device(device)
    dtype = select_dtype(dtype)
    return Tensor(device.module.empty(shape, dtype.t))


def empty_like(x: Tensor) -> Tensor:
    """Returns a tensor based on a given other tensor with uninitialized values.

    Parameters
    ----------
    x : Tensor
        Tensor whose shape, dtype and device are used.

    Returns
    -------
    Tensor
        Tensor with uninitialized values.
    """
    return empty(x.shape, dtype=x.dtype, device=x.device)


def full(
    shape: ShapeLike,
    value: ScalarLike,
    *,
    device: Optional[Device] = None,
    dtype: Optional[DType] = None,
) -> Tensor:
    """Returns a tensor of a given shape filled with a specified value.

    Parameters
    ----------
    shape : ShapeLike
        Shape of the new tensor.
    value : ScalarLike
        Value to fill the tensor with.
    device : Device, optional
        The device the tensor is stored on. Defaults to ``None``.
    dtype : DtypeLike, optional
        Datatype of the tensor data. Defaults to ``None``.

    Returns
    -------
    Tensor
        Tensor filled with a specified value.
    """
    dtype = select_dtype(dtype)
    device = select_device(device)
    return Tensor(device.module.full(shape, value, dtype.t))


def full_like(x: Tensor, value: ScalarLike) -> Tensor:
    """Returns a tensor of a given shape filled with a specified value.

    Parameters
    ----------
    x : Tensor
        Tensor whose shape, dtype and device are used.
    value : ScalarLike
        Value to fill the tensor with.

    Returns
    -------
    Tensor
        Tensor filled with a specified value.
    """
    return full(x.shape, value=value, dtype=x.dtype, device=x.device)


def identity(
    n: int,
    *,
    device: Optional[Device] = None,
    dtype: Optional[DType] = None,
) -> Tensor:
    """Returns a diagonal tensor of shape ``(n, n)``.

    Parameters
    ----------
    n : int
        Size of the new tensor. The shape will be ``(n, n)``.
    device : Device, optional
        The device the tensor is stored on. Defaults to ``None``.
    dtype : DtypeLike, optional
        Datatype of the tensor data. Defaults to ``None``.

    Returns
    -------
    Tensor
        Diagonal tensor.
    """
    dtype = select_dtype(dtype)
    device = select_device(device)
    return Tensor(device.module.identity(n, dtype.t))


def linspace(
    start: float,
    stop: float,
    n: int,
    *,
    device: Optional[Device] = None,
    dtype: Optional[DType] = None,
) -> Tensor:
    """Returns a tensor of num evenly spaced values within
    a given interval :math:`[start, stop]`.

    Parameters
    ----------
    start : float
        Start value.
    stop : float
        Stop value.
    n : int
        Number of samples.
    device : Device, optional
        The device the tensor is stored on. Defaults to ``None``.
    dtype : DtypeLike, optional
        Datatype of the tensor data. Defaults to ``None``.

    Returns
    -------
    Tensor
        Tensor of evenly spaced samples.
    """
    dtype = select_dtype(dtype)
    device = select_device(device)
    return Tensor(device.module.linspace(start, stop, n, dtype=dtype.t))


def ones(
    shape: ShapeLike,
    *,
    device: Optional[Device] = None,
    dtype: Optional[DType] = None,
) -> Tensor:
    """Returns a tensor of a given shape filled with ones.

    Parameters
    ----------
    shape : ShapeLike
        Shape of the new tensor.
    device : Device, optional
        The device the tensor is stored on. Defaults to ``None``.
    dtype : DtypeLike, optional
        Datatype of the tensor data. Defaults to ``None``.

    Returns
    -------
    Tensor
        Tensor filled with ones.
    """
    dtype = select_dtype(dtype)
    device = select_device(device)
    return Tensor(device.module.ones(shape, dtype.t))


def ones_like(x: Tensor) -> Tensor:
    """Returns a tensor based on a given other tensor filled with ones.

    Parameters
    ----------
    x : Tensor
        Tensor whose shape, dtype and device are used.

    Returns
    -------
    Tensor
        Tensor filled with ones.
    """
    return ones(x.shape, dtype=x.dtype, device=x.device)


def split(x: Tensor, splits: int | Sequence[int], dim: int = -1) -> list[Tensor]:
    """Returns a list of new tensors by splitting the tensor.

    Parameters
    ----------
    x : Tensor
        Input tensor.
    splits : int | list[int]
        | Where to split the tensor.
        | ``int``: the tensor is split into n equally sized tensors.
        | ``Sequence[int]``: the tensor is split at the given indices.
    dim : int, optional
        Dimension along which to split the tensor. Defaults to ``-1``.

    Returns
    -------
    list[Tensor]
        List of tensors containing the split data.
    """
    return [Tensor(s) for s in x.device.module.split(x.data, splits, dim)]


def stack(tensors: Sequence[Tensor], dim: DimLike = 0) -> Tensor:
    """Returns a new tensor by stacking a sequence of tensors along a given dimension.

    Parameters
    ----------
    tensors : Sequence[Tensor]
        Sequence of Tensors to be stacked.
    dim : DimLike, optional
        Dimension along which to stack the tensors. Defaults to ``0``.

    Returns
    -------
    Tensor
        Stacked tensor.
    """
    return Tensor(tensors[0].device.module.stack([t.data for t in tensors], dim))


def zeros(
    shape: ShapeLike,
    *,
    device: Optional[Device] = None,
    dtype: Optional[DType] = None,
) -> Tensor:
    """Returns a tensor of a given shape filled with zeros.

    Parameters
    ----------
    shape : ShapeLike
        Shape of the new tensor.
    device : Device, optional
        The device the tensor is stored on. Defaults to ``None``.
    dtype : DtypeLike, optional
        Datatype of the tensor data. Defaults to ``None``.

    Returns
    -------
    Tensor
        Tensor filled with zeros.
    """
    dtype = select_dtype(dtype)
    device = select_device(device)
    return Tensor(device.module.zeros(shape, dtype.t))


def zeros_like(x: Tensor) -> Tensor:
    """Returns a tensor based on a given other tensor filled with zeros.

    Parameters
    ----------
    x : Tensor
        Tensor whose shape, dtype and device are used.

    Returns
    -------
    Tensor
        Tensor filled with zeros.
    """
    return zeros(x.shape, dtype=x.dtype, device=x.device)