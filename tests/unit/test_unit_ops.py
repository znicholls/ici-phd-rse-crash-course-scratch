import re

import pint
import pint.testing
import pytest

from ici_phd_rse.unit_aware import add_unit_aware

Q = pint.get_application_registry().Quantity


def test_add_unit_aware():
    a = Q(1.0, "m")
    b = Q(1.0, "cm")

    exp = Q(1.01, "m")

    res = add_unit_aware(a, b)

    pint.testing.assert_equal(res, exp)


# Tests to write:
# - can add plain floats
# - plain floats give different answer to unit-aware quantities
#   if I add 1 m and 1 cm
# - get an error if I try to add 1 m and 1 kg
def test_incompatible_units_raise():
    a = Q(1.0, "m")
    b = Q(1.0, "kg")

    with pytest.raises(TypeError, match=re.escape("Expected error message")):
        add_unit_aware(a, b)
