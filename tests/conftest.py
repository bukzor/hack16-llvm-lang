import pytest

env_whitelist = (
    'TERM',
    'PATH',
)


@pytest.fixture(scope="session", autouse=True)
def fixed_environment_vars():
    import os
    for var in dict(os.environ):
        # TODO: probably need to set PATH
        if var not in env_whitelist:
            del os.environ[var]
