from numpy import array, linspace, sin, pi, cos
from ddeint import ddeint


def test_lotka_volterra_example():
    def model(Y, t, d):
        x, y = Y(t)
        xd, yd = Y(t - d)
        return array([0.5 * x * (1 - yd), -0.5 * y * (1 - xd)])

    g = lambda t: array([1, 2])
    tt = linspace(2, 30, 20000)
    dd = [0, 0.2]
    expected_values = array([
        [0.502, 1.640],
        [4.576, 0.577]
    ])
    for d, expected_value in zip(dd, expected_values):
        print("Computing for d=%.02f" % d)
        yy = ddeint(model, g, tt, fargs=(d,))
        err = yy[-1] - expected_value
        assert err.dot(err.T) < 0.001


def test_sine_example():
    def model(Y, t):
        return Y(t - 3 * pi / 2)  # Model

    tt = linspace(0, 50, 10000)  # Time start, time end, nb of pts/steps
    g = sin  # Expression of Y(t) before the integration interval
    yy = ddeint(model, g, tt)  # Solving
    assert abs(yy[-1] - (-0.63)) < 0.01


def test_variable_delay():
    def model(Y, t):
        return -Y(t - 3 * cos(Y(t)) ** 2)

    tt = linspace(0, 30, 2000)
    yy = ddeint(model, lambda t: 1, tt)
    assert abs(yy[-1] - 0.716) < 0.01
