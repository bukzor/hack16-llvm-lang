import pytest


@pytest.fixture(scope="session", autouse=True)
def fixed_environment_vars():
    import os
    for var in dict(os.environ):
        # TODO: probably need to set PATH
        del os.environ[var]
