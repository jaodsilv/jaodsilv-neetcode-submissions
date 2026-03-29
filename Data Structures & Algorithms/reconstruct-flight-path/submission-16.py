class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key=lambda x: x[0] + x[1], reverse=True)
        trip = {}
        for t in tickets:
            if t[0] not in trip:
                trip[t[0]] = [t[1]]
            else:
                trip[t[0]].append(t[1])

        def fly(orig: str, trip: dict) -> list[str]:
            if orig not in trip:
                return [orig]
            res = []
            dests = trip[orig]
            while dests:
                dest = dests.pop()
                res.extend(fly(dest, trip))
            res.append(orig)
            return res
            
        return fly('JFK', trip)[::-1]
