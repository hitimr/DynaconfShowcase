# How it works

DynaConf supports multiple formats such as .toml (recommended), .ini, .yaml, .json
Since .toml is recommended I suggest sticking to that.

DynaConf usually consists of 3 files:

- config.toml: for all settings including settings for different environments such as production, debug, etc.
- .secrets.toml: for all secrets
- config.py: Small script for providing an instatiated settings class. Here we also have the option to run config related code. This may include validators (more on that later), or fetching settings from an online source

For this showcase config.toml is tracked by git. For later use id recommend adding it to .gitignore

Loading settings will usually work as follows:

```
from config.config import settings

```

# Running the app with different configs

```bash
export ENV_FOR_DYNACONF=PRODUCTION
python3 src/app.py
>>>> current config: production
>>>> host: 8.8.8.8

export ENV_FOR_DYNACONF=TESTING
python3 src/app.py
>>>> current config: testing
>>>> host: 127.0.0.1
```


# Overloading configs

Overloading can be achieved by exporting `DYNACONF_[setting]=[value]`
The prefix `DYNACONF_` can be changed in config.py

```bash
export ENV_FOR_DYNACONF=PRODUCTION
export DYNACONF_TCP_SERVER_HOST="192.168.0.1"
python3 src/app.py
>>>> current config: production
>>>> host: 192.168.0.1
```

# Validation

Dynaconf provides the ability to define validators. There are 2 ways to accomplish that:

- Define validators in config.py. A bit less readable in my opinion but provides more flexibility. Also we can invoke all validators at any point in the program. We can also pass custom validation functions to a validator
- define validators in `dynaconf_validators.toml`. Can currently only be invoked from CLI with `dynaconf validate`

I suggest using options 1. 

Example of failing a validation

```
export DYNACONF_TCP_SERVER_PORT=1
python3 src/app.py

>>> [stacktrace]
>>> dynaconf.validator.ValidationError: TCP_SERVER_PORT must gte 1000 but it is 1 in env PRODUCTION
```


# Exporting

Dynaconf is not really designed to write configurations back to a settings file.
But it is still possible to export toml using

```python
loaders.write('out.toml', settings.as_dict(), env="testing")
```

This will create a file calld `out.toml` with a single environment named "testing".
Writing back to the original file (`settings.toml`) would cause an override.

Therefore I suggest writing any settings to a separate file (i.e. `runtime_settings.toml`) and sync the current settings in there.
`settings.toml` can then be used to provide default values if the app is launched the first time
