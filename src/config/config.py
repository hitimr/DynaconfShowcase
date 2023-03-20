from dynaconf import Validator
from dynaconf import Dynaconf
from pathlib import Path

validators=[
    Validator("TCP_SERVER_HOST", "TCP_SERVER_PORT", must_exist=True),
    Validator('TCP_SERVER_PORT', gte=1000,  lte=9000),
]

settings = Dynaconf(
    validators=validators,
    envvar_prefix="DYNACONF",
    settings_files=['settings.toml', '.secrets.toml'],
    root_path=Path(__file__).parent.parent.parent,
    environments=True
)


# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.

