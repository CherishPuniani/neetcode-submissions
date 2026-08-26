import bisect
class TimeMap:

    def __init__(self):
        #  This will be key to arr of value mapping where index is timestep
        self.vmap = defaultdict(list)
        self.tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vmap[key].append(value)
        self.tmap[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect_right(self.tmap[key],timestamp) - 1
        if idx == -1:
            return ""
        else:
            return self.vmap[key][idx]
