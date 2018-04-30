from flask import Flask

app = Flask(__name__)

# accesing blueprints
from blue.api.views import mod
from blue.site.views import mod

# register these blueprints
app.register_blueprint(site.views.mod)
app.register_blueprint(api.views.mod, url_prefix="/api")