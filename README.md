<!-- Profile README · Apple-clean · charcoal on #f5f5f7 / near-black · Nov 2026 -->

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/banner-dark.svg?v=2026110206" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/banner-light.svg?v=2026110206" />
    <img alt="Mangesh Raut — Software Engineer" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/banner-dark.svg?v=2026110206" />
  </picture>
</p>

> [!IMPORTANT]
> **Open to Software Engineer roles (Pune · Philadelphia · remote).** Portfolio systems: real-time speech VAD with an F1 gate, offline RAG eval, agents with tool calling and failure handling, and the full stack around them. Every number below links to the file or CI run that produced it — stub metrics are labelled stub.
>
> Fastest contact: [mbr63drexel@gmail.com](mailto:mbr63drexel@gmail.com)

<p align="center">
  <a href="https://mangeshraut712.github.io/mangeshrautarchive/"><img src="https://img.shields.io/badge/Portfolio-0071E3?style=for-the-badge&logo=githubpages&logoColor=white" alt="Portfolio" /></a>
  <a href="https://www.linkedin.com/in/mangeshraut71298/"><img src="https://img.shields.io/badge/LinkedIn-0071E3?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://www.instagram.com/mangesh_d_charming_guy/"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram" /></a>
  <a href="https://wa.me/917276819090"><img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp" /></a>
  <a href="https://x.com/mrcommando712"><img src="https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white" alt="X" /></a>
  <a href="mailto:mbr63drexel@gmail.com"><img src="https://img.shields.io/badge/Email-1D1D1F?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
</p>

<p align="center">
  <a href="https://github.com/sponsors/mangeshraut712"><img src="https://img.shields.io/badge/GitHub-ea4aaa?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="GitHub Sponsors" /></a>
  <a href="https://buy.stripe.com/14A3cufGUgcV5ePfuA14401"><img src="https://img.shields.io/badge/Stripe-635BFF?style=for-the-badge&logo=stripe&logoColor=white" alt="Stripe" /></a>
  <a href="https://www.paypal.com/ncp/payment/LXNHJ5SUGNP82"><img src="https://img.shields.io/badge/PayPal-0071E3?style=for-the-badge&logo=paypal&logoColor=white" alt="PayPal" /></a>
  <a href="https://www.buymeacoffee.com/mangeshraut"><img src="https://img.shields.io/badge/Coffee-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black" alt="Buy Me a Coffee" /></a>
</p>

---

### Start here — three systems, end to end

| Project | What it proves | Guardrails | Proof |
| --- | --- | --- | --- |
| [**ai-ml-portfolio**](https://github.com/mangeshraut712/ai-ml-portfolio) — speech VAD + RAG eval + NumPy ML from scratch | Measured VAD F1 gates (real audio + synthetic labels). Offline RAG/LLM eval with retrieval metrics; CI uses **stub** providers | Acceptance gate fails CI below fixed thresholds; eval falls back to stubs when keys are missing | [MODEL_CARD](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/labs/vad/MODEL_CARD.md) · [RESULTS](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/labs/llm-eval/RESULTS.md) |
| [**agent-console**](https://github.com/mangeshraut712/agent-console) — real-time agent debug UI over WebSocket | Streaming tokens, tool-call traces, protocol observability | Seq reorder + dedupe, `RESUME {last_seq}` replay, single-fire `TOOL_ACK`, chaos verify | [DECISIONS.md](https://github.com/mangeshraut712/agent-console/blob/main/DECISIONS.md) · [Pages replay demo](https://mangeshraut712.github.io/agent-console/) |
| [**Gravity-SaaS-Agent**](https://github.com/mangeshraut712/Gravity-SaaS-Agent) — multi-tenant agent SaaS starter | MCP client, skills engine, billing events, operator dashboard | Tier rate limits, Supabase RLS, circuit breaker, OpenRouter fallback. Channel adapters are **simulators**, not live Business API | [README](https://github.com/mangeshraut712/Gravity-SaaS-Agent#readme) · [CI](https://github.com/mangeshraut712/Gravity-SaaS-Agent/actions/workflows/ci.yml) |

**Reproduce the headline number** (Python 3.10–3.12, no API keys):

```bash
git clone https://github.com/mangeshraut712/ai-ml-portfolio && cd ai-ml-portfolio
make install && make verify-all      # mlfs tests + VAD FULL_PASS + offline LLM eval
```

---

### Engineering metrics — measured, with baselines and a failure case

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/metrics-dark.svg?v=202611020605" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/metrics-light.svg?v=202611020605" />
    <img alt="Verified engineering metrics" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/metrics-dark.svg?v=202611020605" />
  </picture>
</p>

Headline on the card: VAD clean F1 **0.9569**, VAD p95 **~19 ms** (gate ≤100 ms), CI Python **3.10–3.12**. Detail the card does not show:

| Metric | Measured | Gate / baseline | Source |
| --- | ---: | ---: | --- |
| VAD exact F1, noisy — **known failure mode** | **0.7768** | ≥ 0.75 (clean ≥ 0.92) | [challenge_pass.py](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/labs/vad/challenge_pass.py) · [MODEL_CARD](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/labs/vad/MODEL_CARD.md) |
| VAD soft F1 | **0.8135** | ≥ 0.78 | same |
| RAG retrieval **(offline stub)** — TF-IDF Recall@5 · MRR · nDCG@5 | **1.000 · 0.981 · 0.986** | 40 gold QA + 15 adversarial on 10 FAQ docs. BM25-fusion stub Recall@3 **0.975**. Hallucination 0.000 = stub abstaining | [RESULTS.md](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/labs/llm-eval/RESULTS.md) (STUB, 2026-07-24) · [DATA_CARD](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/labs/llm-eval/DATA_CARD.md) |
| Stub cost / latency matrix | p95 ms and $/1k queries per **stub** provider | live path is `EVAL_LIVE=1`; CI never sets it | same RESULTS.md |
| CI run for `make verify-all` | green | — | [Sep 11, 2026](https://github.com/mangeshraut712/ai-ml-portfolio/actions/runs/34574401205) |

---

### Open-source contributions

```text
29 / 50  ███████████▌░░░░░░░░  58%
```

#### By organization (allowlist scoreboard)

| Org | GitHub merged | Focus |
| --- | ---: | --- |
| [Apple](https://github.com/apple/password-manager-resources) | 7 | Password-manager resources & schema |
| [Microsoft](https://github.com/microsoft) | 5 | hve-core + winget-pkgs + physical-ai-toolchain |
| [Adobe](https://github.com/adobe/react-spectrum) | 2 | React Aria / Spectrum (incl. ColorField Form validation) |
| [AWS Labs](https://github.com/awslabs/mcp) | 4 | MCP, Stickler & billing-cost fixes |
| [NVIDIA](https://github.com/NVIDIA/TensorRT-Model-Connect) | 4 | CUDA Python tests & TensorRT tooling/CI |
| [Sarvam AI](https://github.com/sarvamai/sarvam-ai-cookbook) | 2 | Cookbook CI |
| [OpenAI](https://github.com/openai/codex-security) | 1 | codex-security CLI guidance |
| [Google](https://github.com/google/sbsim) | 1 | sbsim BUILD cleanup |
| [Moonshot](https://github.com/MoonshotAI/kimi-code) | 1 | kimi-code models.dev fallback |
| [Samsung](https://github.com/Samsung/CredSweeper) | 1 | CredSweeper install-guide docs |
| [Meta](https://github.com/meta/lexical) | 1 | Lexical; plus 14 accepted Pyrefly CodeSync landings on `main` (separate) |
| Anthropic · Netflix · Tesla · SpaceX/xAI · LG · Walmart · JPMorgan | 0 | — |

#### Selected Engineering Impact

Five merged upstream fixes, each with a test that reproduces the bug.

**Meta · Lexical — [meta/lexical#9707](https://github.com/meta/lexical/pull/9707)**
- **Problem:** When the caret sat after a block decorator inside an element whose DOM slot has a `before` boundary, the block cursor got appended after the slot's trailing decoration, outside the range the editor manages ([#9680](https://github.com/meta/lexical/issues/9680)).
- **What I did:** Changed `$updateDOMBlockCursorElement` to insert the cursor before `slot.before`, falling back to append when there is no boundary or it was detached. Added unit tests for both cases.
- **Result:** Merged by @etrepum. The new test fails before the fix and passes after, and the lexical, rich-text and selection unit suites stay green. Custom slot layouts now keep the cursor where the editor expects it.

**NVIDIA · cuda-python — [NVIDIA/cuda-python#3224](https://github.com/NVIDIA/cuda-python/pull/3224)**
- **Problem:** The program-cache permission test failed on Linux hosts whose `TMPDIR` is setgid, because the new directory inherits `S_ISGID` and reads as `0o2700` instead of `0o700` ([#3214](https://github.com/NVIDIA/cuda-python/issues/3214)).
- **What I did:** Masked the mode with `& 0o777` in both owner-only assertions. Setgid only changes group ownership, not access, so the security check still holds.
- **Result:** Merged by @Andy-Jost. `cuda_core` tests now pass on shared or setgid temp directories without weakening the owner-only check.

**Apple · Password Manager Resources — [apple/password-manager-resources#1178](https://github.com/apple/password-manager-resources/pull/1178)**
- **Problem:** The README documents an `exact-domain-match-only` flag for password rules, but the JSON schema rejected it ([#1165](https://github.com/apple/password-manager-resources/issues/1165)).
- **What I did:** Added the optional boolean to `password-rules-schema.json`, following maintainer guidance, and checked with `ajv` that existing data stays valid, that the flag is accepted and that unknown properties are still rejected.
- **Result:** Merged by @rmondello. The schema and the docs now agree, so password managers can use the flag.

**AWS · MCP servers — [awslabs/mcp#4849](https://github.com/awslabs/mcp/pull/4849)**
- **Problem:** On Windows, the postgres-mcp-server PG-wire path broke because psycopg's async mode does not support the default Proactor event loop ([#4825](https://github.com/awslabs/mcp/issues/4825)).
- **What I did:** Set `WindowsSelectorEventLoopPolicy` at the start of the server entry point, before startup validation or MCP creates a loop, so other platforms keep their default. Added mocked tests for both the Windows and non-Windows paths.
- **Result:** Merged by @kennthhz. Windows users can connect to Postgres over PG-wire through the MCP server.

**Adobe · React Spectrum — [adobe/react-spectrum#10863](https://github.com/adobe/react-spectrum/pull/10863)**
- **Problem:** React Aria's `ColorField` ignored a parent `Form`'s `validationBehavior`, unlike `TextField` and `NumberField` ([#10862](https://github.com/adobe/react-spectrum/issues/10862)).
- **What I did:** Read `FormContext` through `useSlottedContext` and resolved the value as prop, then form, then `'native'`, matching the other fields. Added a regression test that `validationBehavior="aria"` gives `aria-required` without native `required`.
- **Result:** Merged by @devongovett. Forms that use ARIA validation now behave the same for color inputs as for every other field.

---

### More projects

Flagship systems stay in **Start here**. Everything else:

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/projects-dark.svg?v=20261030-claims" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/projects-light.svg?v=20261030-claims" />
    <img alt="More projects: Hindai, Stanford CS336, Codex Insights, Vitals.AI, erdos142, sarvam-ai-cookbook" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/projects-dark.svg?v=20261030-claims" />
  </picture>
</p>

**Also:** [**Actions Nurse**](https://github.com/mangeshraut712/actions-nurse) — Open Agent Hackathon 2026 Wildcard (submitted 28 Oct 2026 4:30 AM IST, [hub](https://hackathon.genai.works/submissions?hackathon_id=019fd164-82b9-7382-a536-d9093c576ed2)). CI triage agent: Rules + optional Gemma, Meterless H-MEM, Zetaris evidence. [submission stamp](https://github.com/mangeshraut712/actions-nurse/blob/main/docs/OPEN-AGENT-SUBMISSION.md).

**Also:** [**Asset Intelligence Copilot**](https://github.com/mangeshraut712/asset-intelligence-copilot) — FlytBase challenge entry (AI Hackers Collective × Hacktoberfest 2026 Hack Day). Chat copilot for oil-field operators: deterministic tools compute numbers, answers cite record IDs and SOP passages, Gemma 4 for planning/phrasing. Local; MIT.

---

<details>
<summary><b>Architecture</b> — patterns across these projects</summary>

```mermaid
flowchart LR
  subgraph Client
    B[Browser<br/>Next.js · React]
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
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/stack-dark.svg?v=20261030-claims" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/stack-light.svg?v=20261030-claims" />
    <img alt="AI stack" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/stack-dark.svg?v=20261030-claims" />
  </picture>
</p>

The card lists tools I use. **Only the dependency manifests below are claims about these repos.**

| Stack claim | Source |
| --- | --- |
| NumPy · webrtcvad · rank-bm25 · scikit-learn | [ai-ml-portfolio/pyproject.toml](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/pyproject.toml) |
| Next.js 16.4.3 · React 19.1 · Turbopack | [agent-console/package.json](https://github.com/mangeshraut712/agent-console/blob/main/package.json) |
| Next.js 15.5 · React 19.2 · Cloudflare Workers AI | [Hindai/package.json](https://github.com/mangeshraut712/Hindai/blob/main/package.json) · [workers/hindai-gemma](https://github.com/mangeshraut712/Hindai/tree/main/workers) |
| Next.js 16.4 dashboard · Express gateway · Supabase | [Gravity-SaaS-Agent/apps](https://github.com/mangeshraut712/Gravity-SaaS-Agent/tree/main/apps) |
| FastAPI | [mangeshrautarchive/requirements.txt](https://github.com/mangeshraut712/mangeshrautarchive/blob/main/requirements.txt) · [career-agent-pro/backend](https://github.com/mangeshraut712/career-agent-pro/blob/main/backend/requirements.txt) |
| Sarvam SDK | [Realtime_Speech_Captioning/requirements.txt](https://github.com/mangeshraut712/sarvam-ai-cookbook/blob/main/examples/Realtime_Speech_Captioning/requirements.txt) |

</details>

<details>
<summary><b>Now</b> — what I'm building this quarter</summary>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/focus-dark.svg?v=20261030-claims" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/focus-light.svg?v=20261030-claims" />
    <img alt="Currently building" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/focus-dark.svg?v=20261030-claims" />
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
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/trajectory-dark.svg?v=2026102810" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/trajectory-light.svg?v=2026102810" />
    <img alt="Contribution trajectory by year" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/trajectory-dark.svg?v=2026102810" />
  </picture>
</p>

<p align="center">
  <a href="https://github.com/mangeshraut712?tab=overview&from=2021-01-01&to=2026-12-31">Contribution graph</a>
  ·
  <a href="https://github.com/mangeshraut712/mangeshraut712/blob/main/data/github-snapshot.json">yearly snapshot JSON</a>
</p>

</details>

