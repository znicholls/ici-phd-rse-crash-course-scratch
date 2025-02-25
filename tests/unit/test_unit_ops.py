import pint
import pint.testing

from ici_phd_rse.unit_aware import add_unit_aware

Q = pint.get_application_registry().Quantity


def test_add_unit_aware():
    a = Q(1.0, "m")
    b = Q(1.0, "cm")

    exp = Q(1.01, "m")

    res = add_unit_aware(a, b)

    pint.testing.assert_equal(res, exp)
