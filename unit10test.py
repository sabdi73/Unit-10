
from lab10 import adjust_rotation
def test_rotation_invalid_input():
with pytest.raises(ValueError):
adjust_rotation("abc")