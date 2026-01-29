"""Alternative Foo Bar - Print Foo and Bar in alternating pattern."""

# Altenative thread Sync using Python event thread
import threading


class FooBar:
    """FooBar class."""

    def __init__(self, n):
        """__init__ function."""
        self.n = n
        self.ev_foo = threading.Event()
        self.ev_bar = threading.Event()

    def foo(self, printFoo: "Callable[[], None]") -> None:
        """foo function."""

        for _ in range(self.n):
            if self.ev_foo.is_set():
                self.ev_bar.wait()
            # printFoo() outputs "foo". Do not change or remove this line.
            self.ev_bar.clear()
            printFoo()
            self.ev_foo.set()

    def bar(self, printBar: "Callable[[], None]") -> None:
        """bar function."""

        for _ in range(self.n):
            self.ev_foo.wait()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.ev_bar.set()
            self.ev_foo.clear()
