# LC 933
# Slow af, beats only 25% in speed but beats 75% in memory
# TODO: Make a faster soln
class RecentCounter:

    def __init__(self):
        self.recent_requests = 0
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.insert(0, t)
        self.recent_requests += 1
        while t - self.requests[-1] > 3000:
            del self.requests[-1]
            self.recent_requests -= 1
        return self.recent_requests


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
