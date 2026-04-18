from ara_sdk import App, run_cli, sandbox, runtime

app = App(
    "Ara Job Hunt Copilot",
    project_name="ara-job-hunt",
    description="Track applications, tailor resumes per role, prep interview questions, auto-follow-up.",
)


@app.subagent(
    id="job-hunt-copilot",
    instructions="""You are a job hunt copilot running on the user's AI computer.
Capabilities:
1. Track every application: company, role, JD link, status (applied/interview/offer/reject), next step, deadlines.
2. Store the pipeline as JSON on the sandbox filesystem.
3. When the user pastes a JD, tailor their resume bullets to match: mirror keywords, reorder impact, never fabricate.
4. Generate interview prep: likely questions pulled from the JD + company research, STAR-format prompts.
5. Draft follow-up emails after interviews — warm, specific, reference something discussed.
6. Answer questions like "which applications are stalled more than 10 days?".
Keep it honest — never fabricate experience or metrics.""",
    sandbox=sandbox(),
    runtime=runtime(python_packages=["beautifulsoup4", "requests"]),
)
def job_hunt_copilot(event=None):
    """Track apps, tailor resumes, prep interviews."""


@app.local_entrypoint()
def local(input_payload):
    return {"ok": True, "app": "ara-job-hunt", "input": input_payload}


if __name__ == "__main__":
    run_cli(app)
