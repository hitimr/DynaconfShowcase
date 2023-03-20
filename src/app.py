from config.config import settings
from dynaconf.utils.boxing import DynaBox
from dynaconf import loaders

# Read some settings
print(f"current config: {settings.CURRENT_CONFIG}")
print(f"host: {settings.TCP_SERVER_PORT}")

# Invoke validators manually
settings.validators.validate_all()

loaders.write('out.toml', settings.as_dict(), env="testing")