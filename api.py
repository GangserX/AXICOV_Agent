from flask import Flask, request, jsonify
from agent import evaluate, progress_check
import os

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "service": "AptoCom Proposal Agent"}), 200

@app.route('/evaluate', methods=['POST'])
def evaluate_proposal():
    """
    Endpoint to evaluate a proposal
    
    Expected JSON payload:
    {
        "title": "Project Name",
        "description": "...",
        "requested_amount": 10000,
        "team_info": "...",
        "budget_breakdown": "...",
        "milestones": "...",
        "expected_roi": "...",
        "risk_factors": "..."
    }
    """
    try:
        proposal_data = request.get_json()
        
        if not proposal_data:
            return jsonify({"error": "No proposal data provided"}), 400
        
        # Validate required fields
        required_fields = ['title', 'description', 'requested_amount']
        for field in required_fields:
            if field not in proposal_data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        # Evaluate the proposal
        result = evaluate(proposal_data)
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/progress-check', methods=['POST'])
def check_progress():
    """
    Endpoint to generate progress check request
    
    Expected JSON payload:
    {
        "proposal_id": "123",
        "milestone_number": 1
    }
    """
    try:
        data = request.get_json()
        proposal_id = data.get('proposal_id')
        milestone_number = data.get('milestone_number')
        
        if not proposal_id or not milestone_number:
            return jsonify({"error": "Missing proposal_id or milestone_number"}), 400
        
        message = progress_check(proposal_id, milestone_number)
        
        return jsonify({"message": message}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
