from multiprocessing import Pool

def f(x):
    return x*x

pool = Pool()
print pool.map(f,range(1,10))

results = []
for i in xrange(1,100):
    results.append(pool.apply_async(f,args=(i,)).get())
pool.close()
pool.join()
print results
