import os
class Config:
    """
    general configuration parent class
    """
class ProdConfig(Config):
    """
    production configuration child clas
    Args:
       config: The parent configuration class with general configuration settings
    """
    pass
class DevConfig(Config):
    """
    development configuration child class
    Args:
        Config: The parent configuration class with General configuration settings.
    """
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}