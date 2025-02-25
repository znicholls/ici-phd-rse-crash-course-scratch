def test_add_unit_aware():
    a = Q(1.0, "m")
    b = Q(1.0, "cm")

    exp = Q(1.01, "m")

    res = add_unit_aware(a, b)

    pint.testing.assert_equal(res, exp)
