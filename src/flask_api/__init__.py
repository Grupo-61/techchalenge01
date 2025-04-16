from flask import Flask
from flask_caching import Cache
from flask_api.rotas_api import rotas_bp
# Importe outros blueprints conforme necessário

# Inicializar a aplicação Flask
cache = Cache()

def create_app():
    app = Flask(__name__)
    
    # Configurações do cache
    config = {
        "DEBUG": True,
        "CACHE_TYPE": "SimpleCache",
        "CACHE_DEFAULT_TIMEOUT": 300,
    }
    app.config.from_mapping(config)
    cache.init_app(app)

    # Registrar blueprints
    app.register_blueprint(rotas_bp)

    return app