import timeit

import fire
import numpy as np

import faiss


def test_faiss(dim=1024, db_size=100000, query_size=10000, k=1, num_loops=100, seed=0):
    np.random.seed(seed)
    db = np.random.random((db_size, dim)).astype('float32')
    query = np.random.random((query_size, dim)).astype('float32')
    index = faiss.IndexFlatL2(dim)
    index.add(db)
    elapsed = timeit.timeit(lambda: index.search(query, k), number=num_loops)
    print(f'Elapsed time: {elapsed / num_loops * 1000:.3f} ms')


if __name__ == '__main__':
    fire.Fire(test_faiss)
