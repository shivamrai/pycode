"""Maximum Frequency Stack - Stack with max frequency element."""

# maximum frequency stack
import collections


class FreqStack:
    """FreqStack class."""

    def __init__(self):
        """__init__ function."""
        self.freq = collections.Counter()  # HasMap {Ele -> Freq}
        self.hashmap = collections.defaultdict(list)  # HashMap {Freq -> List of Ele}
        self.maxFreq = 0

    def push(self, ele):
        """push function."""
        self.freq[ele] += 1  # Update freq in Map
        f = self.freq[ele]

        self.hashmap[f].append(ele)  # Update hashmap stack
        self.maxFreq = max(f, self.maxFreq)

    def pop(self):
        """pop function."""
        ele = self.hashmap[self.maxFreq].pop()  # Get most freq ele
        self.freq[ele] -= 1

        if not self.hashmap[self.maxFreq]:  # This hashmap is now empty
            self.maxFreq -= 1

        return ele

    def print_stack(self):
        """print_stack function."""
        print(self.hashmap)


if __name__ == "__main__":
    pass
