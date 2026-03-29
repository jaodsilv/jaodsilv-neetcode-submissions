import bisect
class TimeMap:

    def __init__(self):
        self.table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.table:
            self.table[key] = []
        self.table[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table:
            return ""
        values = self.table[key]
        index = bisect.bisect_left(values, timestamp, key=lambda x: x[0])
        if index >= len(values):
            return values[-1][1]

        # We know for sure timestamp < values[i][0] for i > index
        # But we may have timestamp == values[i][0] for i == index
        candidate = values[index]
        if candidate[0] == timestamp:
            return candidate[1]
        
        if index == 0:
            return ""
        
        return values[index - 1][1]
        
