from dynaconf import Dynaconf
from pathlib import Path

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['data/settings.toml', 'data/.secrets.toml'],
    root_path=Path(__file__).parent.parent,
    environments=True
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.

