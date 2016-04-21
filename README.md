##How to multithread:

Turns out you can multithread things in python pretty easily.  There are a few ways you can do this:

The highest level of abstraction:

```
from multiprocessing import Process,Queue

def func(x,q):
	q.put(x*x)

results = []
for i in xrange(10000):
	p = Process(target=func,args=(i,q,))
	p.start()
	results.append(q.get())
print results
```

The core specific way:

on mac osx: `sysctl -n hw.ncpu` to get the number of cores, on my machine there are 4.

```
from multiprocessing import Pool

def func(x):
	return x*x

pool = Pool()
results = []
for i in xrange(1,100):
    results.append(pool.apply_async(f,args=(i,)).get())
pool.close()
pool.join()
print results
```