from config.config import settings

# Read some settings
print(f"current config: {settings.CURRENT_CONFIG}")
print(f"host: {settings.TCP_SERVER_HOST}")

# Invoke validators manually
settings.validators.validate_all()
