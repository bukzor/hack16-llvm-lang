# NOTE WELL: No side-effects are allowed in __init__ files. This means you!
from py._path.local import LocalPath as Path
from re import compile as Regex, MULTILINE

TOP = Path(__file__) / '../../..'


def requirements(reqs):
    """Write a requirements.txt file to the current working directory."""
    Path('requirements.txt').write(reqs)


def run(*cmd, **env):
    if env:
        from os import environ
        tmp = env
        env = environ.copy()
        env.update(tmp)
    else:
        env = None

    from .capture_subprocess import capture_subprocess
    capture_subprocess(('echo', '\nTEST>', cmd))
    out, err = capture_subprocess(cmd, env=env)
    err = strip_coverage_warnings(err)
    return out, err


def venv_update(*args, **env):
    # we get coverage for free via the (patched) pytest-cov plugin
    return run(
        'venv-update',
        *args,
        HOME=str(Path('.').realpath()),
        **env
    )


# coverage.py adds some helpful warnings to stderr, with no way to quiet them.
coverage_warnings_regex = Regex(
    r'^Coverage.py warning: (Module .* was never imported\.|No data was collected\.)\n',
    flags=MULTILINE,
)


def strip_coverage_warnings(stderr):
    return coverage_warnings_regex.sub('', stderr)


def uncolor(text):
    # the colored_tty, uncolored_pipe tests cover this pretty well.
    from re import sub
    return sub('\033\\[[^A-z]*[A-z]', '', text)
