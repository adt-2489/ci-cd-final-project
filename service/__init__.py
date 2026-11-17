
"""
Service Package
"""

from flask import Flask
from flask_talisman import Talisman

# Initialize Flask application
app = Flask(__name__)

# Configure security headers
Talisman(app, force_https=False)

# Import routes after creating the Flask application
from service import routes  # pylint: disable=wrong-import-position,cyclic-import
from service.common import log_handlers  # pylint: disable=wrong-import-position

# Initialize application logging
log_handlers.init_logging(app, "gunicorn.error")

# Application startup logs
app.logger.info(70 * "*")
app.logger.info("  S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")
