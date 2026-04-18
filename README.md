# Ara Job Hunt Copilot

Single-agent example from the [Ara Hackathon Tour 2026](https://github.com/cyu60/ara-ai-computer) — track applications, tailor resumes per role, prep interviews, and auto-follow-up, running on the [Ara](https://ara.so) agentic operating system.

**Links:** [Ara docs](https://docs.ara.so/introduction) · [Ara Hackathon Tour](https://github.com/cyu60/ara-ai-computer) · [DayDreamers](https://daydreamers.live)

Part of the **Aragrams** — reference projects built by [DayDreamers](https://daydreamers.live) to show what's possible with agent-first development.

## What it does

Run your entire job hunt via chat. The agent:

- Tracks every application: company, role, JD link, status (applied/interview/offer/reject), next step, deadlines
- Persists the pipeline as JSON on the sandbox filesystem
- Tailors resume bullets to a pasted JD — mirrors keywords, reorders impact, never fabricates
- Generates interview prep: likely questions from JD + company research, STAR-format prompts
- Drafts warm, specific follow-up emails after interviews
- Answers questions like "which applications are stalled more than 10 days?"

No spreadsheet to maintain, no tabs to juggle — text the agent like a career coach who remembers everything.

## Architecture

```
Browser (index.html)
   ↓
/api/run (Vercel serverless function)
   ↓
Ara API (api.ara.so) — Bearer ARA_RUNTIME_KEY
   ↓
job-hunt-copilot subagent running in a sandboxed Python runtime
```

## Local dev

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install ara-sdk
export ARA_ACCESS_TOKEN=<your_token>

python3 app.py setup                           # registers the app → returns APP_ID
python3 app.py deploy --on-existing update     # pushes the agent definition
python3 app.py run --workflow job-hunt-copilot --message "Add application: Anthropic, Forward-Deployed Engineer, applied today"
```

## Deploy

This repo is wired to Vercel. On push to `main`:

1. Vercel builds the static frontend + `api/run.js` edge function.
2. The function proxies `/api/run` calls to `https://api.ara.so/v1/apps/<APP_ID>/run` using `ARA_RUNTIME_KEY`.
3. The Ara runtime spins up the `job-hunt-copilot` sandbox on demand.

## License

MIT
