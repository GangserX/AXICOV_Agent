import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

class AptoCom_ProposalAgent:
    def __init__(self):
        # Initialize Gemini model directly (avoiding LangChain API version issues)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        
    def evaluate_proposal(self, proposal_data):
        """
        Evaluates a DAO proposal and returns a score (0-100) with analysis.
        
        Args:
            proposal_data: Dictionary containing proposal details
                - title: str
                - description: str
                - requested_amount: float
                - team_info: str
                - budget_breakdown: str
                - milestones: str
                - expected_roi: str
                - risk_factors: str
        
        Returns:
            Dictionary with score, reserve_price, analysis, and recommendations
        """
        
        # Create evaluation prompt
        evaluation_prompt = f"""
You are an expert AI evaluator for AptoCom DAO's investment proposals. 
Analyze the following proposal using these 8 criteria:

1. Strategic Alignment (15 points): Does it align with AptoCom's mission?
2. Feasibility (15 points): Is the execution plan realistic?
3. Team Capability (15 points): Does the team have proven track record?
4. Financial Reasonableness (15 points): Is the budget justified?
5. ROI Potential (15 points): Expected return on investment
6. Risk Assessment (10 points): Are risks identified and mitigated?
7. Milestones & Accountability (10 points): Clear deliverables and timeline?
8. Transparency (5 points): Is all information provided clearly?

PROPOSAL DETAILS:
Title: {proposal_data.get('title', 'N/A')}
Description: {proposal_data.get('description', 'N/A')}
Requested Amount: {proposal_data.get('requested_amount', 0)} ACT tokens
Team Information: {proposal_data.get('team_info', 'N/A')}
Budget Breakdown: {proposal_data.get('budget_breakdown', 'N/A')}
Milestones: {proposal_data.get('milestones', 'N/A')}
Expected ROI: {proposal_data.get('expected_roi', 'N/A')}
Risk Factors: {proposal_data.get('risk_factors', 'N/A')}

RESPONSE FORMAT (JSON):
{{
    "total_score": <0-100>,
    "criteria_scores": {{
        "strategic_alignment": <0-15>,
        "feasibility": <0-15>,
        "team_capability": <0-15>,
        "financial_reasonableness": <0-15>,
        "roi_potential": <0-15>,
        "risk_assessment": <0-10>,
        "milestones": <0-10>,
        "transparency": <0-5>
    }},
    "strengths": ["strength 1", "strength 2", "strength 3"],
    "weaknesses": ["weakness 1", "weakness 2"],
    "recommendations": ["recommendation 1", "recommendation 2"],
    "risk_level": "<LOW|MEDIUM|HIGH>",
    "funding_recommendation": "<APPROVE|CONDITIONAL|REJECT>"
}}

Provide only the JSON response, no additional text.
"""
        
        # Invoke the model
        try:
            # Use direct Gemini API
            response = self.model.generate_content(evaluation_prompt)
            content = response.text
            # Remove markdown code blocks if present
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                content = content.split("```")[1].split("```")[0].strip()
            
            evaluation = json.loads(content)
            
            # Calculate reserve price using formula: (Score/100) × Requested × 0.5
            requested_amount = float(proposal_data.get('requested_amount', 0))
            score = float(evaluation.get('total_score', 0))
            reserve_price = (score / 100) * requested_amount * 0.5
            
            # Add reserve price to evaluation
            evaluation['reserve_price'] = round(reserve_price, 2)
            evaluation['requested_amount'] = requested_amount
            
            return evaluation
            
        except json.JSONDecodeError as e:
            # Fallback if JSON parsing fails
            return {
                "total_score": 50,
                "reserve_price": requested_amount * 0.25,
                "error": f"Failed to parse evaluation: {str(e)}",
                "raw_response": response.content
            }
    
    def generate_progress_check(self, proposal_id, milestone_number):
        """
        Generates a progress check request for funded proposals.
        """
        check_prompt = f"""
Generate a professional progress update request email for AptoCom DAO proposal #{proposal_id}, Milestone {milestone_number}.

Include:
1. Friendly greeting
2. Reminder of milestone deliverables
3. Request for evidence (code repos, reports, metrics)
4. Deadline (7 days from now)
5. Next steps

Keep it professional but encouraging.
"""
        
        response = self.model.generate_content(check_prompt)
        return response.text

# API endpoint functions (for Axicov deployment)
agent = AptoCom_ProposalAgent()

def evaluate(proposal_data):
    """Main evaluation endpoint"""
    return agent.evaluate_proposal(proposal_data)

def progress_check(proposal_id, milestone_number):
    """Progress check endpoint"""
    return agent.generate_progress_check(proposal_id, milestone_number)
