def assertNear(expected, actual, tolerance=1e-6):
    assert abs(actual - expected) < tolerance

def assertVectorNear(expected, actual, tolerance=1e-6):
    assertNear(expected[0], actual[0], tolerance)
    assertNear(expected[1], actual[1], tolerance)  
