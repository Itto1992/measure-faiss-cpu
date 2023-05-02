```bash
docker build -t faiss .
```

```bash
docker run --rm -it -v $PWD:/home -w /home faiss python test_faiss.py --db_size 10001 --query_size 100 --dim 1024 --k 1 --num_loops 10
```
- `db_size`: Size of DB.
- `query_size`: Size of query.
- `dim`: Dimension of DB and query vectors.
- `k`: Top-k for nearest neighbor.
- `num_loops`: The number of loops (querying). The total elapsed time will be divided by `num_loops`.
