import  operator

pools = [
    {
        "name": "data",
        "id": 0,
        "stats": {
            "kb_used": 0,
            "bytes_used": 20,
            "max_avail": 32044842769,
            "objects": 0
        }
    },
    {
        "name": "metadata",
        "id": 1,
        "stats": {
            "kb_used": 0,
            "bytes_used": 60,
            "max_avail": 32044842769,
            "objects": 0
        }
    },
    {
        "name": "rbd",
        "id": 2,
        "stats": {
            "kb_used": 0,
            "bytes_used": 100,
            "max_avail": 32044842769,
            "objects": 0
        }
    },
    {
        "name": ".rgw",
        "id": 3,
        "stats": {
            "kb_used": 0,
            "bytes_used": 0,
            "max_avail": 32044842769,
            "objects": 0
        }
    }
]


def _sort(pools, key, n):
    pools.sort(key=lambda e: e['stats'][key], reverse=True)
    top_pools = list()
    for i in range(n):
        top_pools.append(pools[i])
    return top_pools


def _compute_pool_metric(pools, n):
    top_pool_count = n if len(pools) > n else len(pools)
    pool_stats = {
        'size_bytes': 0,
        'objects': 0,
        'top_pools_by_size': list()
    }
    for p in pools:
        pool_stats['size_bytes'] = pool_stats['size_bytes'] + p['stats']['bytes_used']
        pool_stats['objects'] = pool_stats['objects'] + p['stats']['objects']
    pool_stats['top_pools_by_size'] = _sort(pools, 'bytes_used', top_pool_count)
    return pool_stats


def _pool_stats(pools):
    internal = list()
    user = list()
    for p in pools:
        if p['name'][0] == '.':
            internal.append(p)
        else:
            user.append(p)
    user_stats = _compute_pool_metric(user, 1)
    print(user_stats)

if __name__ == "__main__":
    result = _pool_stats(pools)
