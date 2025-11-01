// Axicov Configuration for AptoCom Proposal Agent
const axicovConfig = {
  name: "aptocom-proposal-agent",
  description: "AI-powered proposal evaluation system for AptoCom DAO using LangChain and Google Gemini. Scores proposals on 8 criteria and calculates reserve prices.",
  readmePath: "./README.md",
  env: "./.env",
  
  params: {
    title: {
      type: String,
      description: "Proposal title",
      required: true
    },
    description: {
      type: String,
      description: "Detailed proposal description",
      required: true
    },
    requested_amount: {
      type: Number,
      description: "Amount of ACT tokens requested",
      required: true
    },
    team_info: {
      type: String,
      description: "Information about the team (experience, members, track record)",
      required: false
    },
    budget_breakdown: {
      type: String,
      description: "Detailed breakdown of how funds will be used",
      required: false
    },
    milestones: {
      type: String,
      description: "Project milestones and timeline",
      required: false
    },
    expected_roi: {
      type: String,
      description: "Expected return on investment",
      required: false
    },
    risk_factors: {
      type: String,
      description: "Identified risks and mitigation strategies",
      required: false
    },
    proposal_id: {
      type: String,
      description: "Proposal ID for progress check requests",
      required: false
    },
    milestone_number: {
      type: Number,
      description: "Milestone number for progress check",
      required: false
    }
  },
  
  port: 5000,
  tags: ["LangChain", "AI", "DAO", "Proposal", "Gemini", "Aptos", "Governance", "TypeScript"]
};

export default axicovConfig;
