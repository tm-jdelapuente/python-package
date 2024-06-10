import unittest
import io
import contextlib

from hello import say_hello  # Replace with the actual filename

class TestSayHello(unittest.TestCase):
  def test_say_hello(self):
    """Tests if the say_hello function prints the expected message."""

    f = io.StringIO()
    # Capture the output of the function using a context manager
    with contextlib.redirect_stdout(f):
      say_hello()

    # Assert that the captured output contains the expected message
    self.assertEqual(f.getvalue(), "Hello, World!\n")

if __name__ == "__main__":
  unittest.main()
