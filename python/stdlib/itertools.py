
import operator


def accumulate(iterable, function=operator.add):
    iterator = iter(iterable)
    total = next(iterator)
    yield total
    for element in iterator:
        total = function(total, element)
        yield total


def chain(*iterables):
    """Return an iterator that iterates through each of the elements
    of the iterables in sequence.

    """
    for iterable in iterables:
        yield from iterable


def compress(data, selectors):
    return (d for d, s in zip(data, selectors) if s)


def count(start=0, step=1):
    n = start
    while True:
        yield n
        n += step


def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while True:
        yield from saved


def islice(iterable, *args):
    s = slice(*args)
    it = iter(range(s.start or 0, s.stop, s.step or 1))
    nexti = next(iterator)
    for i, element in enumerate(iterable):
        if i == nexti:
            yield element
            nexti = next(it)
