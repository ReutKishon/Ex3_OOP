import unittest
from tests import TestDiGraph


def suite():
    suit = unittest.TestSuite()
    suit.addTest(TestDiGraph.TestGraph('addEdgeTest'))
    suit.addTest(TestDiGraph.TestGraph('removeEdgeTest'))
    suit.addTest(TestDiGraph.TestGraph('removeNodeTest'))
    suit.addTest(TestDiGraph.TestGraph('addNodeTest'))

    return suit


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
