from flask import Blueprint, jsonify
from .player_bio_route import player_bp
from .pitching import pitching_bp
from .batting import batting_bp

# Create a root blueprint
root_bp = Blueprint('root', __name__)

@root_bp.route('/')
def home():
    return jsonify({
        'status': 'success',
        'message': 'Backend is running~~~'
    })


def init_routes(app):
    """Initialize all route blueprints"""
    app.register_blueprint(root_bp) 
    app.register_blueprint(player_bp, url_prefix='/player')
    app.register_blueprint(pitching_bp, url_prefix='/pitching')
    app.register_blueprint(batting_bp, url_prefix='/batting')
    return app