from agent import AptoCom_ProposalAgent
import json

# Initialize agent
print("🚀 Initializing AptoCom Proposal Agent...")
agent = AptoCom_ProposalAgent()
print("✅ Agent initialized successfully!\n")

# Test proposal data
test_proposal = {
    "title": "Blockchain Education Platform",
    "description": "Build an interactive learning platform for Aptos blockchain development with hands-on tutorials, live coding environments, and certification programs",
    "requested_amount": 25000,
    "team_info": "Team of 4: 2 senior developers (5+ years blockchain exp), 1 UX designer, 1 blockchain educator with PhD",
    "budget_breakdown": "Development: 15k (platform + smart contracts), Content creation: 7k (10 courses), Marketing: 3k (community outreach)",
    "milestones": "M1: Platform MVP with 3 courses (2 months), M2: 10 complete courses + certification (3 months), M3: Marketing campaign + 500 users (1 month)",
    "expected_roi": "500 students in 6 months, potential course monetization generating 10k+ monthly, strengthens Aptos developer ecosystem",
    "risk_factors": "Content quality assurance, user acquisition in competitive market, platform scalability, maintaining engagement"
}

print("📋 Test Proposal:")
print("="*60)
print(f"Title: {test_proposal['title']}")
print(f"Requested Amount: {test_proposal['requested_amount']} ACT tokens")
print(f"Team: {test_proposal['team_info']}")
print("="*60)
print()

# Evaluate
print("🤖 Sending to AI for evaluation...")
print("(This may take 5-10 seconds)")
print()

try:
    result = agent.evaluate_proposal(test_proposal)
    
    print("✅ EVALUATION COMPLETE!")
    print("="*60)
    print()
    
    # Display results in a formatted way
    print(f"🎯 TOTAL SCORE: {result.get('total_score', 'N/A')}/100")
    print(f"💰 RESERVE PRICE: {result.get('reserve_price', 'N/A')} ACT tokens")
    print(f"📊 RISK LEVEL: {result.get('risk_level', 'N/A')}")
    print(f"✋ RECOMMENDATION: {result.get('funding_recommendation', 'N/A')}")
    print()
    
    # Criteria breakdown
    print("📈 CRITERIA SCORES:")
    print("-"*60)
    criteria = result.get('criteria_scores', {})
    for criterion, score in criteria.items():
        criterion_name = criterion.replace('_', ' ').title()
        print(f"  {criterion_name}: {score}")
    print()
    
    # Strengths
    print("💪 STRENGTHS:")
    for i, strength in enumerate(result.get('strengths', []), 1):
        print(f"  {i}. {strength}")
    print()
    
    # Weaknesses
    print("⚠️  WEAKNESSES:")
    for i, weakness in enumerate(result.get('weaknesses', []), 1):
        print(f"  {i}. {weakness}")
    print()
    
    # Recommendations
    print("💡 RECOMMENDATIONS:")
    for i, rec in enumerate(result.get('recommendations', []), 1):
        print(f"  {i}. {rec}")
    print()
    
    print("="*60)
    print()
    print("📄 Full JSON Response:")
    print(json.dumps(result, indent=2))
    
except Exception as e:
    print(f"❌ ERROR: {str(e)}")
    print()
    print("Troubleshooting:")
    print("1. Check your GOOGLE_API_KEY in .env file")
    print("2. Ensure you have internet connection")
    print("3. Verify all dependencies are installed: pip install -r requirements.txt")
