import unittest

from .stack import Stack


class TestStack(unittest.TestCase):

    def test_stack(self):
        stack = Stack()
        self.assertEqual(stack.size, 0)
        self.assertTrue(stack.is_empty)

        stack.push(5)
        self.assertEqual(stack.get_top(), 5)
        self.assertEqual(stack.size, 1)
        self.assertFalse(stack.is_empty)

        stack.push(10)
        self.assertEqual(stack.get_top(), 10)
        self.assertEqual(stack.size, 2)
        self.assertFalse(stack.is_empty)

        self.assertEqual(stack.pop(), 10)
        self.assertEqual(stack.get_top(), 5)
        self.assertEqual(stack.size, 1)
        self.assertFalse(stack.is_empty)

        self.assertEqual(stack.pop(), 5)
        self.assertIsNone(stack.get_top())
        self.assertEqual(stack.size, 0)
        self.assertTrue(stack.is_empty)


if __name__ == "__main__":
    unittest.main()
