from flask import Blueprint
from controllers.ambiente.campus_controller import CampusController


campus_bp = Blueprint('campus', __name__)

campus_bp.route('/campus', methods=['POST'])(CampusController.create_campus)
campus_bp.route('/campus', methods=['GET'])(CampusController.get_campus)
campus_bp.route('/campus/<int:id>', methods=['GET'])(CampusController.get_campus_by_id)
campus_bp.route('/campus/<int:id>', methods=['PUT'])(CampusController.update_campus)
campus_bp.route('/campus/<int:id>', methods=['DELETE'])(CampusController.delete_campus)
