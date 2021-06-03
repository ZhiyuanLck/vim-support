import unittest
from ..popup import *


class TestPopupPos(unittest.TestCase):
    def setUp(self):
        self.position = PopupPos(
                line=3,
                col=5,
                pos="botleft",
                posinvert=None
                )

    def test_type(self):
        with self.assertRaises(ValueError):
            PopupPos(line=1.2)
        with self.assertRaises(ValueError):
            PopupPos(line="cursor+_")
        with self.assertRaises(ValueError):
            PopupPos(col=2.4)
        with self.assertRaises(ValueError):
            PopupPos(col="cursor+_")
        with self.assertRaises(ValueError):
            PopupPos(pos=2)
        with self.assertRaises(ValueError):
            PopupPos(pos="abc")
        with self.assertRaises(ValueError):
            PopupPos(posinvert=1)

    def test_val(self):
        self.assertEqual(self.position.line, 3)
        self.assertEqual(self.position.col, 5)
        self.assertEqual(self.position.pos, "botleft")
        self.assertIsNotNone(self.position.posinvert)


def test():
    #  import vim
    #  vim.command("setline('.', 'test')")
    try:
        unittest.main()
    except:
        pass
