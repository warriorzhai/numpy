# Compatibility module containing deprecated names

__all__ = ['asarray', 'array', 'concatenate',
           'NewAxis',
           'UFuncType', 'UfuncType', 'ArrayType', 'arraytype',
           'LittleEndian', 'Bool',
           'Character', 'UnsignedInt8', 'UnsignedInt16', 'UnsignedInt',
           'UInt8','UInt16','UInt32', 'UnsignedInt32', 'UnsignedInteger',
           # UnsignedInt64 and Unsigned128 added below if possible
           # same for Int64 and Int128, Float128, and Complex128
           'Int8', 'Int16', 'Int32',
           'Int0', 'Int', 'Float0', 'Float', 'Complex0', 'Complex',
           'PyObject', 'Float32', 'Float64', 'Float16', 'Float8',
           'Complex32', 'Complex64', 'Complex8', 'Complex16',
           'typecodes', 'sarray', 'arrayrange', 'cross_correlate',
           'matrixmultiply', 'outerproduct', 'innerproduct',
           # from cPickle
           'dump', 'dumps',
           # functions that are now methods
           'take', 'reshape', 'choose', 'repeat', 'put', 'putmask',
           'swapaxes', 'transpose', 'sort', 'argsort', 'argmax', 'argmin',
           'searchsorted', 'alen',
           'resize', 'diagonal', 'trace', 'ravel', 'nonzero', 'shape',
           'compress', 'clip', 'sum', 'product', 'prod', 'sometrue', 'alltrue',
           'any', 'all', 'cumsum', 'cumproduct', 'cumprod', 'ptp', 'ndim',
           'rank', 'size', 'around', 'round_', 'mean', 'std', 'var', 'squeeze',
           'amax', 'amin',
          ]

import multiarray as mu
import umath as um
import numerictypes as nt
from numeric import asarray, array, asanyarray, correlate, outer, concatenate
from umath import sign, absolute, multiply
import numeric as _nx
import sys
_dt_ = nt.sctype2char

import types

try:
    _gentype = types.GeneratorType
except AttributeError:
    _gentype = types.NoneType
#Use this to add a new axis to an array
#compatibility only
NewAxis = None

#deprecated
UFuncType = type(um.sin)
UfuncType = type(um.sin)
ArrayType = mu.ndarray
arraytype = mu.ndarray

LittleEndian = (sys.byteorder == 'little')

# save away Python sum
_sum_ = sum

# backward compatible names from old Precision.py

Character = 'S1'
UnsignedInt8 = _dt_(nt.uint8)
UInt8 = UnsignedInt8
UnsignedInt16 = _dt_(nt.uint16)
UInt16 = UnsignedInt16
UnsignedInt32 = _dt_(nt.uint32)
UInt32 = UnsignedInt32
UnsignedInt = _dt_(nt.uint)

try:
    UnsignedInt64 = _dt_(nt.uint64)
except AttributeError:
    pass
else:
    UInt64 = UnsignedInt64
    __all__ += ['UnsignedInt64', 'UInt64']
try:
    UnsignedInt128 = _dt_(nt.uint128)
except AttributeError:
    pass
else:
    UInt128 = UnsignedInt128
    __all__ += ['UnsignedInt128','UInt128']

Int8 = _dt_(nt.int8)
Int16 = _dt_(nt.int16)
Int32 = _dt_(nt.int32)

try:
    Int64 = _dt_(nt.int64)
except AttributeError:
    pass
else:
    __all__ += ['Int64']

try:
    Int128 = _dt_(nt.int128)
except AttributeError:
    pass
else:
    __all__ += ['Int128']

Bool = _dt_(bool)
Int0 = _dt_(int)
Int = _dt_(int)
Float0 = _dt_(float)
Float = _dt_(float)
Complex0 = _dt_(complex)
Complex = _dt_(complex)
PyObject = _dt_(nt.object_)
Float32 = _dt_(nt.float32)
Float64 = _dt_(nt.float64)

Float16='f'
Float8='f'
UnsignedInteger='L'
Complex8='F'
Complex16='F'

try:
    Float128 = _dt_(nt.float128)
except AttributeError:
    pass
else:
    __all__ += ['Float128']

Complex32 = _dt_(nt.complex64)
Complex64 = _dt_(nt.complex128)

try:
    Complex128 = _dt_(nt.complex256)
except AttributeError:
    pass
else:
    __all__ += ['Complex128']

typecodes = {'Character':'S1',
             'Integer':'bhilqp',
             'UnsignedInteger':'BHILQP',
             'Float':'fdg',
             'Complex':'FDG',
             'AllInteger':'bBhHiIlLqQpP',
             'AllFloat':'fdgFDG',
             'All':'?bhilqpBHILQPfdgFDGSUVO'}

def sarray(a, dtype=None, copy=False):
    return array(a, dtype, copy)

# backward compatibility
arrayrange = mu.arange
cross_correlate = correlate

# deprecated names
matrixmultiply = mu.dot
outerproduct = outer
innerproduct = mu.inner

from cPickle import dump, dumps

# functions that are now methods

def _wrapit(obj, method, *args, **kwds):
    try:
        wrap = obj.__array_wrap__
    except AttributeError:
        wrap = None
    result = getattr(asarray(obj),method)(*args, **kwds)
    if wrap:
        result = wrap(result)
    return result

def take(a, indices, axis=0):
    try:
        result = a.take(indices, axis)
    except AttributeError:
        result = _wrapit(a, 'take', indices, axis)
    return result

def reshape(a, newshape):
    """Change the shape of a to newshape.  Return a new view object.
    """
    try:
        result = a.reshape(newshape)
    except AttributeError:
        result = _wrapit(a, 'reshape', newshape)
    return result

def choose(a, choices):
    try:
        result = a.choose(choices)
    except AttributeError:
        result = _wrapit(a, 'choose', choices)
    return result

def repeat(a, repeats, axis=0):
    """repeat elements of a repeats times along axis
       repeats is a sequence of length a.shape[axis]
       telling how many times to repeat each element.
       If repeats is an integer, it is interpreted as
       a tuple of length a.shape[axis] containing repeats.
       The argument a can be anything array(a) will accept.
    """
    try:
        result = a.repeat(repeats, axis)
    except AttributeError:
        result = _wrapit(a, 'repeat', repeats, axis)
    return result

def put (a, ind, v):
    """put(a, ind, v) results in a[n] = v[n] for all n in ind
       If v is shorter than mask it will be repeated as necessary.
       In particular v can be a scalar or length 1 array.
       The routine put is the equivalent of the following (although the loop
       is in C for speed):

           ind = array(indices, copy=False)
           v = array(values, copy=False).astype(a.dtype)
           for i in ind: a.flat[i] = v[i]
       a must be a contiguous numpy array.
    """
    return a.put(v,ind)

def putmask (a, mask, v):
    """putmask(a, mask, v) results in a = v for all places mask is true.
       If v is shorter than mask it will be repeated as necessary.
       In particular v can be a scalar or length 1 array.
    """
    return a.putmask(v, mask)

def swapaxes(a, axis1, axis2):
    """swapaxes(a, axis1, axis2) returns array a with axis1 and axis2
    interchanged.
    """
    try:
        result = a.swapaxes(axis1, axis2)
    except AttributeError:
        result = _wrapit(a, 'swapaxes', axis1, axis2)
    return result

def transpose(a, axes=None):
    """transpose(a, axes=None) returns array with dimensions permuted
    according to axes.  If axes is None (default) returns array with
    dimensions reversed.
    """
    try:
        result = a.transpose(axes)
    except AttributeError:
        result = _wrapit(a, 'transpose', axes)
    return result

def sort(a, axis=-1):
    """sort(a,axis=-1) returns array with elements sorted along given axis.
    """
    a = asanyarray(a, copy=True)
    a.sort(axis)
    return a

def argsort(a, axis=-1):
    """argsort(a,axis=-1) return the indices into a of the sorted array
    along the given axis, so that take(a,result,axis) is the sorted array.
    """
    try:
        result = a.argsort(axis)
    except AttributeError:
        result = _wrapit(a, 'argsort', axis)
    return result

def argmax(a, axis=-1):
    """argmax(a,axis=-1) returns the indices to the maximum value of the
    1-D arrays along the given axis.
    """
    try:
        result = a.argmax(axis)
    except AttributeError:
        result = _wrapit(a, 'argmax', axis)
    return result

def argmin(a, axis=-1):
    """argmin(a,axis=-1) returns the indices to the minimum value of the
    1-D arrays along the given axis.
    """
    try:
        result = a.argmin(axis)
    except AttributeError:
        result = _wrapit(a, 'argmin', axis)
    return result
    
def searchsorted(a, v):
    """searchsorted(a, v)
    """
    try:
        result = a.searchsorted(v)
    except AttributeError:
        result = _wrapit(a, 'searchsorted', v)
    return result

def resize(a, new_shape):
    """resize(a,new_shape) returns a new array with the specified shape.
    The original array's total size can be any size. It
    fills the new array with repeated copies of a.

    Note that a.resize(new_shape) will fill array with 0's
    beyond current definition of a.
    """

    if isinstance(new_shape, (int, nt.integer)):
        new_shape = (new_shape,)
    a = ravel(a)
    Na = len(a)
    if not Na: return mu.zeros(new_shape, a.dtype.char)
    total_size = um.multiply.reduce(new_shape)
    n_copies = int(total_size / Na)
    extra = total_size % Na

    if total_size == 0:
        return a[:0]

    if extra != 0:
        n_copies = n_copies+1
        extra = Na-extra

    a = concatenate( (a,)*n_copies)
    if extra > 0:
        a = a[:-extra]

    return reshape(a, new_shape)

def squeeze(a):
    "Returns a with any ones from the shape of a removed"
    try:
        result = a.squeeze()
    except AttributeError:
        result = _wrapit(a, 'squeeze')
    return result

def diagonal(a, offset=0, axis1=0, axis2=1):
    """diagonal(a, offset=0, axis1=0, axis2=1) returns the given diagonals
    defined by the last two dimensions of the array.
    """
    return asarray(a).diagonal(offset, axis1, axis2)

def trace(a, offset=0, axis1=0, axis2=1, dtype=None):
    """trace(a,offset=0, axis1=0, axis2=1) returns the sum along diagonals
    (defined by the last two dimenions) of the array.
    """
    return asarray(a).trace(offset, axis1, axis2, dtype)

def ravel(m):
    """ravel(m) returns a 1d array corresponding to all the elements of it's
    argument.
    """
    return asarray(m).ravel()

def nonzero(a):
    """nonzero(a) returns the indices of the elements of a which are not zero,
    a must be 1d
    """
    try:
        result = a.nonzero()
    except AttributeError:
        result = _wrapit(a, 'nonzero')
    return result

def shape(a):
    """shape(a) returns the shape of a (as a function call which
       also works on nested sequences).
    """
    try:
        result = a.shape
    except AttributeError:
        result = asarray(a).shape
    return result

def compress(condition, m, axis=-1):
    """compress(condition, x, axis=-1) = those elements of x corresponding
    to those elements of condition that are "true".  condition must be the
    same size as the given dimension of x."""
    try:
        result = m.compress(condition, axis)
    except AttributeError:
        result = _wrapit(m, 'compress', condition, axis)
    return result

def clip(m, m_min, m_max):
    """clip(m, m_min, m_max) = every entry in m that is less than m_min is
    replaced by m_min, and every entry greater than m_max is replaced by
    m_max.
    """
    try:
        result = m.clip(m_min, m_max)
    except AttributeError:
        result = _wrapit(m, 'clip', m_min, m_max)
    return result

def sum(x, axis=0, dtype=None):
    """Sum the array over the given axis.  The optional dtype argument
    is the data type for intermediate calculations.

    The default is to upcast (promote) smaller integer types to the
    platform-dependent Int.  For example, on 32-bit platforms:

        x.dtype                         default sum() dtype
        ---------------------------------------------------
        bool, Int8, Int16, Int32        Int32

    Examples:
    >>> sum([0.5, 1.5])
    2.0
    >>> sum([0.5, 1.5], dtype=Int32)
    1
    >>> sum([[0, 1], [0, 5]])
    array([0, 6])
    >>> sum([[0, 1], [0, 5]], axis=1)
    array([1, 5])
    """
    if isinstance(x, _gentype):
        return _sum_(x)
    try:
        result = x.sum(axis, dtype)
    except AttributeError:
        result = _wrapit(x, 'sum', axis, dtype)
    return result

def product (x, axis=0, dtype=None):
    """Product of the array elements over the given axis."""
    try:
        result = x.prod(axis, dtype)
    except AttributeError:
        result = _wrapit(x, 'prod', axis, dtype)
    return result

def sometrue (x, axis=0):
    """Perform a logical_or over the given axis."""
    try:
        result = x.any(axis)
    except AttributeError:
        result = _wrapit(x, 'any', axis)
    return result

def alltrue (x, axis=0):
    """Perform a logical_and over the given axis."""
    try:
        result = x.all(axis)
    except AttributeError:
        result = _wrapit(x, 'all', axis)
    return result

def any(x,axis=None):
    """Return true if any elements of x are true:  
    """
    try:
        result = x.any(axis)
    except AttributeError:
        result = _wrapit(x, 'any', axis)
    return result

def all(x,axis=None):
    """Return true if all elements of x are true:  
    """
    try:
        result = x.all(axis)
    except AttributeError:
        result = _wrapit(x, 'all', axis)
    return result

def cumsum (x, axis=0, dtype=None):
    """Sum the array over the given axis."""
    try:
        result = x.cumsum(axis, dtype)
    except AttributeError:
        result = _wrapit(x, 'cumsum', axis, dtype)
    return result

def cumproduct (x, axis=0, dtype=None):
    """Sum the array over the given axis."""
    try:
        result = x.cumprod(axis, dtype)
    except AttributeError:
        result = _wrapit(x, 'cumprod', axis, dtype)
    return result

def ptp(a, axis=0):
    """Return maximum - minimum along the the given dimension
    """
    try:
        result = a.ptp(axis)
    except AttributeError:
        result = _wrapit(a, 'ptp', axis)
    return result

def amax(a, axis=0):
    """Return the maximum of 'a' along dimension axis.
    """
    try:
        result = a.max(axis)
    except AttributeError:
        result = _wrapit(a, 'max', axis)
    return result

def amin(a, axis=0):
    """Return the minimum of a along dimension axis.
    """
    try:
        result = a.min(axis)
    except AttributeError:
        result = _wrapit(a, 'min', axis)
    return result

def alen(a):
    """Return the length of a Python object interpreted as an array
    of at least 1 dimension.
    """
    try:
        return len(a)
    except TypeError:
        return len(atleast_1d(a))

def prod(a, axis=0, dtype=None):
    """Return the product of the elements along the given axis
    """
    try:
        result = a.prod(axis, dtype)
    except AttributeError:
        result = _wrapit(a, 'prod', axis, dtype)
    return result

def cumprod(a, axis=0, dtype=None):
    """Return the cumulative product of the elments along the given axis
    """
    try:
        result = a.cumprod(axis, dtype)
    except AttributeError:
        result = _wrapit(a, 'cumprod', axis, dtype)
    return result

def ndim(a):
    try:
        return a.ndim
    except AttributeError:
        return asarray(a).ndim

def rank(a):
    """Get the rank of sequence a (the number of dimensions, not a matrix rank)
       The rank of a scalar is zero.
    """
    try:
        return a.ndim
    except AttributeError:
        return asarray(a).ndim

def size (a, axis=None):
    "Get the number of elements in sequence a, or along a certain axis."
    if axis is None:
        try:
            return a.size
        except AttributeError:
            return asarray(a).size
    else:
        try:
            return a.shape[axis]
        except AttributeError:
            return asarray(a).shape[axis]

def round_(a, decimals=0):
    """Round 'a' to the given number of decimal places.  Rounding
    behaviour is equivalent to Python.

    Return 'a' if the array is not floating point.  Round both the real
    and imaginary parts separately if the array is complex.
    """
    try:
        result = a.round(decimals)
    except AttributeError:
        result = _wrapit(a, 'round', decimals)
    return result

around = round_

def mean(a, axis=0, dtype=None):
    try:
        result = a.mean(axis, dtype)
    except AttributeError:
        result = _wrapit(a, 'mean', axis, dtype)
    return result        

def std(a, axis=0, dtype=None):
    try:
        result = a.std(axis, dtype)
    except AttributeError:
        result = _wrapit(a, 'std', axis, dtype)
    return result

def var(a, axis=0, dtype=None):
    try:
        result = a.std(axis, dtype)
    except AttributeError:
        result = _wrapit(a, 'var', axis, dtype)
    return result
