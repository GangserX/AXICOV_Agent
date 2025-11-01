# Axicov Deployment Information

**Deployment Date:** November 1, 2025  
**Status:** ✅ Successfully Deployed

---

## Deployment Details

| Field | Value |
|-------|-------|
| **Workflow ID** | 23 |
| **Workflow Name** | aptocom-proposal-agent |
| **Port** | 5000 |
| **File ID** | uyfag3x3ousn |
| **File Name** | project.zip |
| **File Size** | 9,365 bytes (9.15 KB) |
| **Snapshot ID** | snapshot_wsmf8ge5 |
| **Uploaded At** | 2025-10-31T21:29:55.965708466Z |

---

## API Credentials

```env
AXICOV_API_KEY=0xAxi650bbebd04869db30d975e465625f68432a89eb616691d189507cf76a6e99875
GOOGLE_API_KEY=AIzaSyB5ZL6IAcxUMYqz-5b1XUew9GR0ksp8tOI
```

---

## Next Steps

1. **Log in to Axicov Dashboard**
   - Visit: https://axicov.com/dashboard
   - Find your deployed workflow: "aptocom-proposal-agent"

2. **Get API Endpoint URL**
   - Look for the full API URL in the dashboard
   - Should be in format: `https://api.axicov.com/agents/YOUR_AGENT_ID/`
   - Save this URL as `AXICOV_AGENT_URL`

3. **Test the Deployed Agent**
   ```bash
   curl -X POST https://YOUR_AXICOV_URL/evaluate \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_API_KEY" \
     -d '{
       "title": "Test Proposal",
       "description": "Testing deployed agent",
       "requested_amount": 10000
     }'
   ```

4. **Integrate with Backend**
   - Update your backend `.env` file with the Axicov URL
   - Create the Axicov service integration file
   - Test the integration

---

## Deployment Command Used

```bash
axicov deploy -k 0xAxi650bbebd04869db30d975e465625f68432a89eb616691d189507cf76a6e99875 -v
```

---

## Files Deployed

1. agent.py
2. api.py
3. requirements.txt
4. README.md
5. axicov.config.ts
6. .env
7. .env.example
8. .gitignore
9. test.py

**Total:** 9 files

---

## API Endpoints Available

### 1. Health Check
```http
GET /health
```

### 2. Evaluate Proposal
```http
POST /evaluate
Content-Type: application/json

{
  "title": "string",
  "description": "string",
  "requested_amount": number,
  "team_info": "string" (optional),
  "budget_breakdown": "string" (optional),
  "milestones": "string" (optional),
  "expected_roi": "string" (optional),
  "risk_factors": "string" (optional)
}
```

### 3. Progress Check
```http
POST /progress-check
Content-Type: application/json

{
  "proposal_id": "string",
  "milestone_number": number
}
```

---

## Support

- **Axicov Docs:** https://axicov-ai.gitbook.io/axicov-docs
- **Axicov Website:** https://axicov.com
- **Google Gemini:** https://aistudio.google.com

---

**Deployment Successful!** 🎉
