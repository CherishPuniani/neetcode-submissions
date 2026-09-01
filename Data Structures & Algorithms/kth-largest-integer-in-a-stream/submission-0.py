class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = nums
        self.k = k

    def add(self, val: int) -> int:
        self.stream.append(val)
        stream_sort = sorted(self.stream, reverse=True)
        return stream_sort[self.k-1]
