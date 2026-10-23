<!-- Apple-inspired engineering portfolio · black / white / #0071E3 · Sep 2026 -->

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/banner-dark.svg?v=2026102304" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/banner-light.svg?v=2026102304" />
    <img alt="Mangesh Raut — Applied AI Engineer" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/banner-dark.svg?v=2026102304" />
  </picture>
</p>

> [!IMPORTANT]
> **Open to AI Engineer roles (Pune · remote).** I build the production *shape* of AI systems: agents with tool calling and failure handling, real-time speech VAD with an F1 gate, an offline RAG eval harness, and the full-stack around them. Every number below links to the file or CI run that produced it — stub metrics are labelled stub.
> Fastest contact: [mbr63drexel@gmail.com](mailto:mbr63drexel@gmail.com)

<p align="center">
  <a href="https://mangeshraut712.github.io/mangeshrautarchive/"><img src="https://img.shields.io/badge/Portfolio-0071E3?style=for-the-badge&logo=githubpages&logoColor=white" alt="Portfolio" /></a>
  <a href="https://www.linkedin.com/in/mangeshraut71298/"><img src="https://img.shields.io/badge/LinkedIn-0071E3?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://www.instagram.com/mangesh_d_charming_guy/"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram" /></a>
  <a href="https://wa.me/917276819090"><img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp" /></a>
  <a href="https://x.com/mrcommando712"><img src="https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white" alt="X" /></a>
</p>

<p align="center">
  <a href="https://github.com/sponsors/mangeshraut712"><img src="https://img.shields.io/badge/GitHub-ea4aaa?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="GitHub Sponsors" /></a>
  <a href="https://buy.stripe.com/14A3cufGUgcV5ePfuA14401"><img src="https://img.shields.io/badge/Stripe-635BFF?style=for-the-badge&logo=stripe&logoColor=white" alt="Stripe" /></a>
  <a href="https://www.paypal.com/ncp/payment/LXNHJ5SUGNP82"><img src="https://img.shields.io/badge/PayPal-0071E3?style=for-the-badge&logo=paypal&logoColor=white" alt="PayPal" /></a>
  <a href="https://www.buymeacoffee.com/mangeshraut"><img src="https://img.shields.io/badge/Coffee-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black" alt="Buy Me a Coffee" /></a>
</p>

---

### Start here — three systems, end to end

| Project | What it proves | Guardrails / failure handling | Proof |
| --- | --- | --- | --- |
| [**ai-ml-portfolio**](https://github.com/mangeshraut712/ai-ml-portfolio) — speech VAD + RAG eval + NumPy ML from scratch | Measured VAD F1 gates (real audio + synthetic labels). Offline RAG/LLM eval harness with retrieval metrics; CI uses **stub** providers, not live APIs | Acceptance gate (`challenge_pass.py`) fails CI below fixed thresholds; eval harness falls back to stubs when keys are missing so CI never depends on a live API | [MODEL_CARD](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/labs/vad/MODEL_CARD.md) · [RESULTS](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/labs/llm-eval/RESULTS.md) |
| [**agent-console**](https://github.com/mangeshraut712/agent-console) — real-time agent debug UI over WebSocket | Streaming tokens, tool-call traces, protocol observability for agent backends | Seq-based reorder buffer with dedupe, `RESUME {last_seq}` replay after disconnect, single-fire `TOOL_ACK`, chaos-mode verification (`npm run verify:chaos`) | [DECISIONS.md](https://github.com/mangeshraut712/agent-console/blob/main/DECISIONS.md) · [live demo](https://mangeshraut712.github.io/agent-console/) |
| [**Gravity-SaaS-Agent**](https://github.com/mangeshraut712/Gravity-SaaS-Agent) — multi-tenant agent SaaS starter (Next.js dashboard + Express gateway) | MCP client, skills engine, billing events, operator dashboard | Tier-based `express-rate-limit`, Supabase RLS policies, circuit breaker, OpenRouter fallback. WhatsApp/Telegram adapters in-repo are **simulators** (`enhanced-channels.ts`), not live Business API traffic | [README](https://github.com/mangeshraut712/Gravity-SaaS-Agent#readme) · [CI](https://github.com/mangeshraut712/Gravity-SaaS-Agent/actions/workflows/ci.yml) |

**Reproduce the headline number in one command** (Python 3.10–3.12, no API keys):

```bash
git clone https://github.com/mangeshraut712/ai-ml-portfolio && cd ai-ml-portfolio
make install && make verify-all      # mlfs tests + VAD FULL_PASS gate + offline LLM eval
```

---

### Engineering metrics — measured, with baselines and a failure case

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/metrics-dark.svg?v=202610230450" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/metrics-light.svg?v=202610230450" />
    <img alt="Verified engineering metrics" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/metrics-dark.svg?v=202610230450" />
  </picture>
</p>

Headline numbers on the card: VAD clean F1 **0.9569**, VAD p95 **~19 ms** (measured; the code gate is ≤100 ms), CI Python **3.10–3.12**. The table is only what the card does not show.

| Metric | Measured | Gate / baseline | Source |
| --- | ---: | ---: | --- |
| VAD exact F1, noisy — **known failure mode** | **0.7768** | gate ≥ 0.75 (clean gate is ≥ 0.92) | [challenge_pass.py](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/labs/vad/challenge_pass.py) · [MODEL_CARD](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/labs/vad/MODEL_CARD.md) |
| VAD soft F1 | **0.8135** | gate ≥ 0.78 | same |
| RAG retrieval **(offline stub, not live models)** — TF-IDF Recall@5 · MRR · nDCG@5 | **1.000 · 0.981 · 0.986** | 40 gold QA + 15 adversarial on 10 FAQ docs. BM25-fusion stub is Recall@3 **0.975** (different cut). Hallucination 0.000 is the stub generator abstaining | [RESULTS.md](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/labs/llm-eval/RESULTS.md) (mode STUB, 2026-07-24) · [DATA_CARD](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/labs/llm-eval/DATA_CARD.md) |
| Stub cost / latency matrix | p95 ms and $/1k queries per **stub** provider | optional live path is `EVAL_LIVE=1`; CI never sets it | same RESULTS.md |
| CI run for `make verify-all` | green | — | [Sep 11, 2026](https://github.com/mangeshraut712/ai-ml-portfolio/actions/runs/34574401205) |

---

### Open-source contributions

**26 merged upstream PRs** as of 2026-10-22. Only merged PRs are listed. Each one was checked with `gh pr view` and has a `mergedAt` date. My own repos are not included.

**Goal: 50 merged PRs.** Progress: 26 / 50 (52%), focused on Apple, Google, Meta, NVIDIA, Microsoft, OpenAI, Anthropic and AWS.

**Big-company orgs**

- **Apple** · password-manager-resources: [#1784 Change-password URL for thriftbooks.com](https://github.com/apple/password-manager-resources/pull/1784) · [#1318 Shared credentials for start.gg](https://github.com/apple/password-manager-resources/pull/1318) · [#1239 Shared credentials for HDFC Bank](https://github.com/apple/password-manager-resources/pull/1239) · [#1179 Shared credentials for Bluesky](https://github.com/apple/password-manager-resources/pull/1179) · [#1178 Exact-domain-only password rules in schema](https://github.com/apple/password-manager-resources/pull/1178)
- **Google** · sbsim: [#187 Remove internal Blaze/Bazel BUILD files](https://github.com/google/sbsim/pull/187)
- **OpenAI** · codex-security: [#754 Shell-neutral env-var removal guidance](https://github.com/openai/codex-security/pull/754)

**Other projects**

- **brekkylab/backlot**: [#788 Notion data sources in database search](https://github.com/brekkylab/backlot/pull/788) · [#762 Jira orderBy validation](https://github.com/brekkylab/backlot/pull/762) · [#711 Google Docs documents.get param validation](https://github.com/brekkylab/backlot/pull/711) · [#710 Linear branchName for unassigned issues](https://github.com/brekkylab/backlot/pull/710) · [#662 S3 response-override validation](https://github.com/brekkylab/backlot/pull/662) · [#661 GitHub issue sort tie-breaking](https://github.com/brekkylab/backlot/pull/661)
- **eugenioenko/ttt**: [#947 Refresh F3 matches after edits](https://github.com/eugenioenko/ttt/pull/947) · [#946 No search matches on image/binary tabs](https://github.com/eugenioenko/ttt/pull/946) · [#927 Restore cursor when undoing line commands](https://github.com/eugenioenko/ttt/pull/927)
- **finos/architecture-as-code**: [#3372 Fix calm-hub seed base URL](https://github.com/finos/architecture-as-code/pull/3372) · [#3331 Theme colours in VS Code canvas preview](https://github.com/finos/architecture-as-code/pull/3331)
- **sarvamai/sarvam-ai-cookbook**: [#185 Skip no-op weekly rules sync](https://github.com/sarvamai/sarvam-ai-cookbook/pull/185) · [#116 Detect unquoted TS/JS model keys in CI](https://github.com/sarvamai/sarvam-ai-cookbook/pull/116)
- **MoonshotAI/kimi-code**: [#2416 Built-in model catalog fallback](https://github.com/MoonshotAI/kimi-code/pull/2416)
- **maester365/maester**: [#2392 Fix ORCA crash on multi-policy domains](https://github.com/maester365/maester/pull/2392)
- **oceanbase/powercontext**: [#2009 Extraction diagnostics in CLI capabilities](https://github.com/oceanbase/powercontext/pull/2009)
- **CapSoftware/Cap**: [#2549 Accept configured web host in share URLs](https://github.com/CapSoftware/Cap/pull/2549)
- **RailtownAI/railtracks**: [#1684 Offline EchoLLM for tests](https://github.com/RailtownAI/railtracks/pull/1684)
- **espnet/espnet**: [#6890 Pass use_sdpa through UniversaBase](https://github.com/espnet/espnet/pull/6890)

[All merged PRs on GitHub](https://github.com/search?q=is%3Apr+author%3Amangeshraut712+is%3Amerged+-user%3Amangeshraut712+-user%3Adayx61&type=pullrequests)

---

### More projects

The three systems above stay in **Start here**. These cards are everything else.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/projects-dark.svg?v=2026091712" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/projects-light.svg?v=2026091712" />
    <img alt="More shipped projects: Hindai, Stanford CS336, Codex Insights, Vitals.AI, erdos142, sarvam-ai-cookbook" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/projects-dark.svg?v=2026091712" />
  </picture>
</p>

**Also new:** [**Asset Intelligence Copilot**](https://github.com/mangeshraut712/asset-intelligence-copilot) — FlytBase challenge entry (AI Hackers Collective × Hacktoberfest 2026 Hack Day). A chat copilot for oil-field operators: deterministic tools compute the numbers, answers cite record IDs and SOP passages, and Gemma 4 handles planning and phrasing. Runs locally; MIT.

---

<details>
<summary><b>Architecture</b> — how the pieces connect (Mermaid, renders natively)</summary>

```mermaid
flowchart LR
  subgraph Client
    B[Browser<br/>Next.js 15 · React 19]
  end
  subgraph Runtime
    WS[WebSocket agent server<br/>seq ordering · RESUME replay]
    API[FastAPI / Express gateway<br/>rate limits · RLS · circuit breaker]
  end
  subgraph Models_Tools_Data["Models · Tools · Data"]
    OR[OpenRouter / Workers AI<br/>multi-model fallback]
    MCP[MCP servers · tool calling]
    VAD[WebRTC VAD · speech]
    RAG[BM25 / TF-IDF retrieval<br/>eval gates]
  end
  subgraph Ops
    CI[GitHub Actions CI<br/>F1 gates · offline eval]
    DEP[Docker · Cloudflare · GitHub Pages]
  end
  B <--> WS
  B --> API
  WS --> MCP
  API --> OR
  API --> RAG
  B --> VAD
  MCP --> OR
  CI --> DEP
```

</details>

<details>
<summary><b>AI engineering stack</b> — every claim points at a dependency file</summary>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/stack-dark.svg?v=20260906f" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/stack-light.svg?v=20260906f" />
    <img alt="AI stack" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/stack-dark.svg?v=20260906f" />
  </picture>
</p>

The card lists tools I use. **Only the lockfiles below are claims about these repos.** PyTorch / Ollama / DeepSeek on the card are local/tooling names, not pinned dependencies here.

| Stack claim | Source |
| --- | --- |
| NumPy · webrtcvad · rank-bm25 · scikit-learn | [ai-ml-portfolio/pyproject.toml](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/pyproject.toml) |
| Next.js 15.3 · React 19.1 · Turbopack | [agent-console/package.json](https://github.com/mangeshraut712/agent-console/blob/main/package.json) |
| Next.js 15.5 · React 19.2 · Cloudflare Workers AI | [Hindai/package.json](https://github.com/mangeshraut712/Hindai/blob/main/package.json) · [workers/hindai-gemma](https://github.com/mangeshraut712/Hindai/tree/main/workers) |
| Next.js 15.5 dashboard · Express gateway · Supabase | [Gravity-SaaS-Agent/apps](https://github.com/mangeshraut712/Gravity-SaaS-Agent/tree/main/apps) |
| FastAPI | [mangeshrautarchive/requirements.txt](https://github.com/mangeshraut712/mangeshrautarchive/blob/main/requirements.txt) · [career-agent-pro/backend](https://github.com/mangeshraut712/career-agent-pro/blob/main/backend/requirements.txt) |
| Sarvam SDK | [Realtime_Speech_Captioning/requirements.txt](https://github.com/mangeshraut712/sarvam-ai-cookbook/blob/main/examples/Realtime_Speech_Captioning/requirements.txt) |

</details>

<details>
<summary><b>Now</b> — what I'm building this quarter</summary>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/focus-dark.svg?v=20260906f" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/focus-light.svg?v=20260906f" />
    <img alt="Currently building" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/focus-dark.svg?v=20260906f" />
  </picture>
</p>

</details>

<details>
<summary><b>Principles, writing, trajectory</b></summary>

**Engineering principles**

- Measure everything; ship the gate with the number
- Local-first whenever possible; CI must not depend on a live API
- Reliability over novelty — an agent with guardrails beats a flashier one without
- AI should augment, not obscure, the system
- Developer experience matters; simple systems scale better

Details: [INTERVIEW_NOTES.md](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/INTERVIEW_NOTES.md)

**Writing**

- [Technical writings RSS](https://mangeshraut712.github.io/mangeshrautarchive/rss.xml)

**Trajectory**

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/trajectory-dark.svg?v=20260906f" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/trajectory-light.svg?v=20260906f" />
    <img alt="Contribution trajectory by year" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/trajectory-dark.svg?v=20260906f" />
  </picture>
</p>

<p align="center">
  <a href="https://github.com/mangeshraut712?tab=overview&from=2021-01-01&to=2026-12-31">Contribution graph</a>
  ·
  <a href="https://github.com/mangeshraut712/mangeshraut712/blob/main/data/github-snapshot.json">yearly snapshot JSON</a>
</p>

</details>
