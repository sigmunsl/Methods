from unittest import TestCase

from matricies import *

class TestMatricies(TestCase):
    def test_cda_matrix(self):
        matrix = np.array([[4., 1., 0.],
                           [1., 4., 1.],
                           [0., 1., 4.]])
        a, d, c = cda_matrix(matrix)
        expected_c = np.array([1, 1])
        expected_d = np.array([4, 4, 4])
        expected_a = np.array([1, 1])
        np.testing.assert_almost_equal(expected_a, a)
        np.testing.assert_almost_equal(expected_c, c)
        np.testing.assert_almost_equal(expected_d, d)


    def test_trifactor(self):
        a = np.array([2., 2.])
        d = np.array([4., 4., 4.])
        c = np.array([1., 1.])
        l, u, c = trifactor(a, d, c)
        expected_l = np.array([0.5, 2/3.5])
        expected_u = np.array([4., 3.5, 4 - 2/3.5])
        np.testing.assert_almost_equal(expected_l, l)
        np.testing.assert_almost_equal(expected_u, u)
