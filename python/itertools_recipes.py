#!/usr/bin/env python

from itertools import islice

def take(n, iterable):
    '''Return first n items of the iterable.'''
    return islice(iterable, n)

def tabulate(function, start=0):
    '''Return function(n) for n=0 up to start.'''
    return (function(n) for n in range(start))

def consume(iterator, n=None):
    '''Advance the iterator by n steps, or consume entirely if no n given.'''
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)

def nth(iterable, n, default=None):
    '''Returns the nth item, or a default value.'''
    return next(islice(iterable, n, None), default)

def quantify(iterable, predicate=bool):
    '''Count how many times the predicate is true.'''
    return sum(imap(predicate, iterable))

def padnone(iterable):
    '''Returns the sequence elements and then returns None indefinitely.

    Useful for emulating the behavior of the built-in map() function.
    '''
    return chain(iterable, repeat(None))

def ncycles(iterable, n):
    '''Returns the sequence elements n times.'''
    return chain.from_iterable(repeat(tuple(iterable), n))

def dotproduct(v1, v2):
    return sum(imap(operator.mul, v1, v2))

def flatten(lists):
    '''Flatten one level of nesting.'''
    return chain.from_iterable(lists)

def repeatfunc(func, times=None, *args):
    '''Repeat calls to func with the specified arguments.

    Example: repeatfunc(random.random)
    '''
    if times is None:
        return starmap(func, repeat(args))
    return starmap(func, repeat(args, times))

def pairwise(iterable):
    '''Breaks a sequence into an iterator of its elements in pairs.

    Example: s -> (s0, s1), (s1, s2), (s2, s3), ...
    '''
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

def grouper(n, iterable, fillvalue=None):
    '''Collect data into fixed-length chunks or blocks.

    Example: grouper(3, 'ABCDEFG', 'x') -> ABC, DEF, Gxx
    '''
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def roundrobin(*iterables):
    '''Example: roundrobin('ABC', 'D', 'EF') -> A, D, E, B, F, C'''
    pending = len(iterables)
    nexts = cycle(iter(i).next for i in iterables)
    while pending:
        try:
            for n in nexts:
                yield n()
            except StopIteration:
                pending -= 1
                nexts = cycle(islice(nexts, pending))

def powerset(*iterable):
    '''Example:
    powerset((1, 2, 3)) -> (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)
    '''
    return chain.from_iterable(combinations(iterable, n)
                               for n in range(len(iterable) + 1))

def unique_everseen(iterable, key=None):
    '''Lists unique elements, preserving order. Remember all elements
    ever seen.

    Examples:
        unique_everseen('AAAABBBBBCCCDAABBB') -> A, B, C, D
        unique_everseen('ABBCcAD', str.lower) -> A, B, C, D
    '''
    seen = set()
    if key is None:
        for el in ifilter(lambda el: el not in seen, iterable):
            seen.add(el)
            yield el
    else:
        for el in imap(key, iterable):
            if el not in seen:
                seen.add(el)
                yield el

def unique_justseen(iterable, key=None):
    '''Lists unique elements, preserving order. Remembers only the
    element just seen.

    Examples:
        unique_justseen('AAAABBBCCDAABBB') -> A, B, C, D, A, B
        unique_justseen('ABBCcAD', str.lower) -> A, B, C, A, D
    '''
    return imap(next, imap(itemgetter(1), groupby(iterable, key)))

def iter_except(func, exception, first=None):
    '''Call a function repeatedly until an exception is raised.

    Converts a call-until-exception interface to an interator interface.
    Like iter(func, sentinel) but uses an exception instead of a
    sentinel to end the loop.

    Examples:
        bsddb_biter = iter_except(db.next, bsdb.error, db.first)
        heap_iter = iter_except(functools.partial(heappop, h), IndexError)
        dict_iter = iter_except(d.popitem, KeyError)
        deque_iter = iter_except(d.popleft, IndexError)
        queue_iter = iter_except(q.get_nowait, Queue.Empty)
        set_iter = iter_except(s.pop, KeyError)
    '''
    try:
        if first is not None:
            yield first()
        while True:
            yield func()
    except exception:
        pass

def random_product(*args, **kwargs):
    '''Random selection from itertools.product(*args, **kwargs).'''
    pools = map(tuple, args) * kwargs.get('repeat', 1)
    return tuple(random.choice(pool) for pool in pools)

def random_permutation(iterable, order):
    '''Random selection from itertools.permutations(iterable, r).'''
    pool = tuple(iterable)
    if order is None:
        order = len(pool)
    return tuple(random.sample(pool, order))

def random_combination(iterable, order):
    '''Random selection from itertools.combinations(iterable, r).'''
    pool = tuple(iterable)
    indices = sorted(random.sample(range(len(pool)), order))
    return tuple(pool[i] for i in indices)

def random_combination_with_replacement(iterable, order):
    '''Random selection from
    itertools.combinations_with_replacement(iterable, r).
    '''
    pool = tuple(iterable)
    indices = sorted(random.randrange(len(pool)) for _ in range(r))
    return tuple(pool[i] for i in indices)

# Many of these recipes can be optimized by replacing global lookups
# with local variables defined as default values, like below.

def dotproduct(v1, v2, sumf=sum, mapf=imap, mulf=operator.mul):
    return sumf(mapf(mulf, v1, v2))

