# AptoCom Proposal Evaluation Agent

AI-powered proposal evaluation system for AptoCom DAO using Google Gemini and LangChain.

## 🎯 Overview

This agent evaluates DAO proposals using 8 criteria and automatically calculates reserve prices for auction-based funding.

### Evaluation Criteria (100 points total):
1. **Strategic Alignment** (15 pts) - Alignment with AptoCom's mission
2. **Feasibility** (15 pts) - Realistic execution plan
3. **Team Capability** (15 pts) - Proven track record
4. **Financial Reasonableness** (15 pts) - Justified budget
5. **ROI Potential** (15 pts) - Expected returns
6. **Risk Assessment** (10 pts) - Risk identification & mitigation
7. **Milestones & Accountability** (10 pts) - Clear deliverables
8. **Transparency** (5 pts) - Information clarity

### Reserve Price Formula:
```
Reserve Price = (AI Score / 100) × Requested Amount × 0.5
```

## 🚀 API Endpoints

### 1. Health Check
```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "AptoCom Proposal Agent"
}
```

### 2. Evaluate Proposal
```http
POST /evaluate
Content-Type: application/json
```

**Request Body:**
```json
{
  "title": "DeFi Integration Project",
  "description": "Build cross-chain bridge for Aptos",
  "requested_amount": 50000,
  "team_info": "3 developers, 5 years blockchain experience",
  "budget_breakdown": "Development: 30k, Audit: 15k, Marketing: 5k",
  "milestones": "M1: Smart contract (3 months), M2: Frontend (2 months)",
  "expected_roi": "20% annual yield",
  "risk_factors": "Smart contract security, regulatory changes"
}
```

**Response:**
```json
{
  "total_score": 82,
  "reserve_price": 20500.0,
  "requested_amount": 50000,
  "criteria_scores": {
    "strategic_alignment": 13,
    "feasibility": 14,
    "team_capability": 12,
    "financial_reasonableness": 13,
    "roi_potential": 12,
    "risk_assessment": 8,
    "milestones": 7,
    "transparency": 3
  },
  "strengths": [
    "Strong technical team with blockchain experience",
    "Clear budget allocation and milestones",
    "High ROI potential with DeFi integration"
  ],
  "weaknesses": [
    "Risk mitigation strategies could be more detailed",
    "Transparency on team members needs improvement"
  ],
  "recommendations": [
    "Provide detailed profiles of team members",
    "Add more specific security audit plans",
    "Include contingency budget for unforeseen risks"
  ],
  "risk_level": "MEDIUM",
  "funding_recommendation": "CONDITIONAL"
}
```

### 3. Progress Check
```http
POST /progress-check
Content-Type: application/json
```

**Request Body:**
```json
{
  "proposal_id": "123",
  "milestone_number": 1
}
```

**Response:**
```json
{
  "message": "Dear AptoCom Team,\n\nWe hope this message finds you well...[generated email]"
}
```

## 🔧 Environment Variables

Create a `.env` file in the project root:

```env
# Google Gemini API Key (Required)
# Get from: https://aistudio.google.com
GOOGLE_API_KEY=your_gemini_api_key_here

# Server Port (Optional, default: 5000)
PORT=5000
```

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. **Create Virtual Environment:**
```bash
python -m venv venv
```

2. **Activate Virtual Environment:**

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure Environment:**
```bash
# Copy example env file
cp .env.example .env

# Edit .env and add your Google Gemini API key
```

## 🧪 Testing Locally

Run the test script:

```bash
python test.py
```

Or start the Flask server:

```bash
python api.py
```

Test with curl:

```bash
curl -X POST http://localhost:5000/evaluate \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Test Proposal",
    "description": "Testing AI evaluation",
    "requested_amount": 10000,
    "team_info": "Experienced team",
    "budget_breakdown": "Dev: 7k, Marketing: 3k",
    "milestones": "M1: MVP in 2 months",
    "expected_roi": "15% yield",
    "risk_factors": "Market volatility"
  }'
```

## 🌐 Deployment to Axicov

### Prerequisites
- Axicov account (sign up at https://axicov.com)
- Axicov CLI installed: `npm install -g @axicov/cli`
- Axicov API key (from dashboard)

### Deploy

```bash
# Deploy to Axicov
axicov deploy -k YOUR_AXICOV_API_KEY

# With verbose output
axicov deploy -k YOUR_AXICOV_API_KEY -v
```

After deployment, you'll receive:
- **API URL:** `https://api.axicov.com/agents/YOUR_AGENT_ID/`
- **API Key:** For authentication

## 🔗 Integration with Backend

### Node.js/Express Example

```javascript
const axios = require('axios');

const axicovAgent = {
  baseURL: process.env.AXICOV_AGENT_URL,
  apiKey: process.env.AXICOV_API_KEY,
  
  async evaluateProposal(proposalData) {
    const response = await axios.post(
      `${this.baseURL}/evaluate`,
      proposalData,
      {
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'Content-Type': 'application/json'
        }
      }
    );
    return response.data;
  }
};

module.exports = axicovAgent;
```

## 📊 Response Fields Explained

| Field | Type | Description |
|-------|------|-------------|
| `total_score` | Number | Overall score (0-100) |
| `reserve_price` | Number | Calculated reserve price for auction |
| `requested_amount` | Number | Original requested amount |
| `criteria_scores` | Object | Breakdown by 8 criteria |
| `strengths` | Array | Identified strengths |
| `weaknesses` | Array | Identified weaknesses |
| `recommendations` | Array | Improvement suggestions |
| `risk_level` | String | LOW, MEDIUM, or HIGH |
| `funding_recommendation` | String | APPROVE, CONDITIONAL, or REJECT |

## 🛠️ Troubleshooting

### Common Issues

**1. Import Error: No module named 'langchain_google_genai'**
```bash
pip install --upgrade langchain-google-genai
```

**2. API Key Error**
- Verify your `GOOGLE_API_KEY` in `.env`
- Check it starts with `AIza...`
- Ensure no extra spaces or quotes

**3. JSON Parse Error**
- The AI sometimes returns markdown. The code handles this automatically
- If issues persist, check the `raw_response` field in error responses

**4. Port Already in Use**
```bash
# Change PORT in .env file
PORT=5001
```

## 📝 License

MIT License - Built for AptoCom DAO

## 🤝 Support

For issues or questions:
- Check Axicov documentation: https://axicov-ai.gitbook.io/axicov-docs
- Visit Axicov: https://axicov.com
- Google Gemini API: https://aistudio.google.com

---

**Version:** 1.0.0  
**Last Updated:** November 1, 2025
