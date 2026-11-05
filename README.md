<!-- Profile README · Apple-clean · charcoal on #f5f5f7 / near-black · Nov 2026 -->

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/banner-dark.svg?v=2026110506" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/banner-light.svg?v=2026110506" />
    <img alt="Mangesh Raut — Software Engineer" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/banner-dark.svg?v=2026110506" />
  </picture>
</p>

> [!IMPORTANT]
> **Open to Software Engineer roles (Pune · Philadelphia · remote).** Portfolio systems: real-time speech VAD with an F1 gate, offline RAG eval, agents with tool calling and failure handling, and the full stack around them. Benchmark figures link to their reports or CI runs; account statistics link to dated snapshots. Stub metrics are labelled stub.
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
| [**agent-console · Incident Desk**](https://github.com/mangeshraut712/agent-console) — seeded on-call investigation + protocol console | Labelled, key-free replay of Northwind incidents; planner/tool trace, verdict and seed-based scorecard | Live-capable Nemotron planner via Nebius (**not executed**); telemetry stays seeded. Original WebSocket reorder/dedupe and `RESUME` console retained | [Agent implementation](https://github.com/mangeshraut712/agent-console/tree/main/src/agent) · [Protocol decisions](https://github.com/mangeshraut712/agent-console/blob/main/DECISIONS.md) · [Pages replay demo](https://mangeshraut712.github.io/agent-console/) |
| [**Gravity-SaaS-Agent**](https://github.com/mangeshraut712/Gravity-SaaS-Agent) — multi-tenant agent SaaS starter | MCP-style simulated tool registry, skills scaffold, billing events, operator dashboard | Tier rate limits, Supabase RLS policies, OpenRouter retries/circuit breaker and labelled echo fallback. Channel adapters are **simulators**, not live Business API | [README](https://github.com/mangeshraut712/Gravity-SaaS-Agent#readme) · [CI](https://github.com/mangeshraut712/Gravity-SaaS-Agent/actions/workflows/ci.yml) |

**Run the benchmark and acceptance gates** (Python 3.10–3.12, no API keys; latency depends on hardware):

```bash
git clone https://github.com/mangeshraut712/ai-ml-portfolio && cd ai-ml-portfolio
make install && make verify-all      # mlfs tests + VAD FULL_PASS + offline LLM eval
```

On Debian/Ubuntu, install `build-essential` and `libsndfile1` first. Initial setup needs network access for dependencies and audio.

---

### Engineering metrics — measured, with baselines and a failure case

[Source audit and verification limits](docs/PROFILE-AUDIT.md) · checked November 3, 2026.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/metrics-dark.svg?v=20261102-readability" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/metrics-light.svg?v=20261102-readability" />
    <img alt="Verified engineering metrics" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/metrics-dark.svg?v=20261102-readability" />
  </picture>
</p>

The VAD figures come from Sep 11, 2026 CI. Latency measures batch whole-file processing and excludes warmup; the VAD gate runs on Python 3.11. Exact labels are constructed from real speech and synthetic silence; soft labels use energy, not human annotation. Baselines and failure cases:

| Metric | Measured | Gate / baseline | Source |
| --- | ---: | ---: | --- |
| VAD exact F1, noisy — **known failure mode** | **0.7768** | ≥ 0.75 (clean ≥ 0.92) | [challenge_pass.py](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/labs/vad/challenge_pass.py) · [MODEL_CARD](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/labs/vad/MODEL_CARD.md) |
| VAD soft F1 | **0.8135** | ≥ 0.78 | same |
| RAG retrieval **(offline stub)** — TF-IDF Recall@5 · MRR · nDCG@5 | **1.000 · 0.981 · 0.986** | 40 gold QA + 15 adversarial on 10 FAQ docs. BM25-fusion stub Recall@3 **0.975**. Hallucination 0.000 = stub abstaining | [RESULTS.md](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/labs/llm-eval/RESULTS.md) (STUB, 2026-07-24) · [DATA_CARD](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/labs/llm-eval/DATA_CARD.md) |
| Stub cost / latency matrix | Stub p95 ms and estimated $/1k queries from configured prices/token estimates | live path is `EVAL_LIVE=1`; CI forces `EVAL_LIVE=0` (stub) | same RESULTS.md |
| CI labs + VAD acceptance gate | green | — | [Sep 11, 2026](https://github.com/mangeshraut712/ai-ml-portfolio/actions/runs/34574401205) |

---

### Open-source contributions

```text
48 / 50  ███████████████████▏  96%
```

**48 merged pull requests** across company and lab orgs on the allowlist (GitHub Merged badge only).

#### By organization (allowlist scoreboard)

| Org | Merged | Focus |
| --- | ---: | --- |
| [Meta](https://github.com/meta/lexical/pull/9707) | 1 | Lexical |
| [AWS Labs](https://github.com/awslabs/visual-asset-management-system/pull/860) | 15 | MCP, Stickler, billing-cost fixes & Visual Asset Management System |
| [Microsoft](https://github.com/microsoft/physical-ai-toolchain/pull/2093) | 8 | hve-core, winget-pkgs, physical-ai-toolchain, [Semantic Kernel](https://github.com/microsoft/semantic-kernel/pull/14668) |
| [Apple](https://github.com/apple/password-manager-resources/pull/1851) | 7 | Password-manager resources & schema |
| [NVIDIA](https://github.com/NVIDIA/cuda-python/pull/3241) | 5 | CUDA Python tests & TensorRT tooling/CI |
| [Adobe](https://github.com/adobe/react-spectrum/pull/10869) | 3 | React Aria / Spectrum (incl. ColorField Form validation) |
| [Sarvam AI](https://github.com/sarvamai/sarvam-ai-cookbook/pull/185) | 2 | Cookbook CI |
| [Google](https://github.com/google/sbsim/pull/187) | 2 | sbsim BUILD cleanup + [Gemini cookbook](https://github.com/google-gemini/cookbook/pull/1449) link checker |
| [OpenAI](https://github.com/openai/codex-security/pull/754) | 1 | codex-security CLI guidance |
| [Netflix](https://github.com/Netflix/dgs-codegen/pull/997) | 1 | DGS codegen Kotlin client generation |
| [Samsung](https://github.com/Samsung/CredSweeper/pull/997) | 1 | CredSweeper install-guide docs |
| [Moonshot](https://github.com/MoonshotAI/kimi-code/pull/2416) | 1 | kimi-code models.dev fallback |
| [AMD](https://github.com/amd/gaia/pull/6656) | 1 | GAIA memory bootstrap confidence parsing |

**Open pull requests:** 101 across allowlist orgs, including Anthropic (11), Walmart (4), xAI (2), JPMorgan (2), Tesla (2) and LG/webOS (1).

#### Selected Engineering Impact

Five merged upstream fixes, with regression tests, corrected assertions or schema validation.

<details open>
<summary><b>Meta · Lexical — <a href="https://github.com/meta/lexical/pull/9707">meta/lexical#9707</a></b></summary>

- **Problem:** When the caret sat after a block decorator inside an element whose DOM slot has a `before` boundary, the block cursor got appended after the slot's trailing decoration, outside the range the editor manages ([#9680](https://github.com/meta/lexical/issues/9680)).
- **What I did:** Changed `$updateDOMBlockCursorElement` to insert the cursor before `slot.before`, falling back to append when there is no boundary or it was detached. Added unit tests for both cases.
- **Result:** Merged by @etrepum. The new test fails before the fix and passes after, and the lexical, rich-text and selection unit suites stay green. Custom slot layouts now keep the cursor where the editor expects it.

</details>

<details>
<summary><b>Netflix · DGS Codegen — <a href="https://github.com/Netflix/dgs-codegen/pull/997">Netflix/dgs-codegen#997</a></b></summary>

- **Problem:** Kotlin 2 client generation always added `_alias` and `_projection` parameters to projection methods, so a GraphQL field with an argument of the same name produced duplicate parameters and failed to compile ([#930](https://github.com/Netflix/dgs-codegen/issues/930)).
- **What I did:** Renamed the generated alias and projection parameters only when they collide with a field argument, so existing schemas keep the same names. Added codegen tests that compile client queries using `_alias` and `_projection` arguments.
- **Result:** Merged by @iuliiasobolevska, who kept the commit and added a follow-up for related shadowing cases. Slated for the 8.8.1 release.

</details>

<details>
<summary><b>Microsoft · Semantic Kernel — <a href="https://github.com/microsoft/semantic-kernel/pull/14668">microsoft/semantic-kernel#14668</a></b></summary>

- **Problem:** The Python OpenAPI plugin checked `allowed_base_urls` with a raw path-prefix match, so `/api/../admin` and `/api/%2e%2e/admin` passed an `/api` allowlist. For the literal dot-segment path, httpx actually requested `/admin` ([#14662](https://github.com/microsoft/semantic-kernel/issues/14662)).
- **What I did:** Checked the prefix after dot-segment normalization in both raw and percent-decoded forms, preserving internal empty segments to match httpx. Added tests for the escapes and for paths that must still pass, like `/api/./users` and `/api/`.
- **Result:** Merged by @eavanvalkenburg. The tested dot-segment escapes are rejected by the OpenAPI URL allowlist, and `/apiusers` is still rejected.

</details>

<details>
<summary><b>AWS · MCP servers — <a href="https://github.com/awslabs/mcp/pull/4849">awslabs/mcp#4849</a></b></summary>

- **Problem:** On Windows, the postgres-mcp-server PG-wire path broke because psycopg's async mode does not support the default Proactor event loop ([#4825](https://github.com/awslabs/mcp/issues/4825)).
- **What I did:** Set `WindowsSelectorEventLoopPolicy` at the start of the server entry point, before startup validation or MCP creates a loop, so other platforms keep their default. Added mocked tests for both the Windows and non-Windows paths.
- **Result:** Merged by @kennthhz. The PG-wire startup path now selects the Windows event-loop policy required by psycopg; mocked tests cover Windows and non-Windows policy selection.

</details>

<details>
<summary><b>Adobe · React Spectrum — <a href="https://github.com/adobe/react-spectrum/pull/10863">adobe/react-spectrum#10863</a></b></summary>

- **Problem:** React Aria's `ColorField` ignored a parent `Form`'s `validationBehavior`, unlike `TextField` and `NumberField` ([#10862](https://github.com/adobe/react-spectrum/issues/10862)).
- **What I did:** Read `FormContext` through `useSlottedContext` and resolved the value as prop, then form, then `'native'`, matching the other fields. Added a regression test that `validationBehavior="aria"` gives `aria-required` without native `required`.
- **Result:** Merged by @devongovett. ColorField now inherits Form ARIA validation behavior, matching the existing TextField and NumberField pattern.

</details>

---

### More projects

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/projects-dark.svg?v=20261102-readability" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/projects-light.svg?v=20261102-readability" />
    <img alt="More projects: Hindai, Stanford CS336, Codex Insights, Vitals.AI, erdos142, sarvam-ai-cookbook" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/projects-dark.svg?v=20261102-readability" />
  </picture>
</p>

- [**Actions Nurse**](https://github.com/mangeshraut712/actions-nurse) — Open Agent Hackathon 2026 Wildcard track (author-recorded submission: 28 Oct 2026 4:30 AM IST, [hub](https://hackathon.genai.works/submissions?hackathon_id=019fd164-82b9-7382-a536-d9093c576ed2)). CI triage agent: Rules + optional Gemma, Meterless H-MEM, labelled Zetaris fixtures with optional live read-only evidence. [submission stamp](https://github.com/mangeshraut712/actions-nurse/blob/main/docs/OPEN-AGENT-SUBMISSION.md).

- [**Asset Intelligence Copilot**](https://github.com/mangeshraut712/asset-intelligence-copilot) — FlytBase challenge entry (AI Hackers Collective × Hacktoberfest 2026 Hack Day). Chat copilot for oil-field operators: deterministic tools compute numbers, answers cite record IDs and SOP passages, Gemma 4 for planning/phrasing. Local; MIT.

---

<details>
<summary><b>Architecture</b> — patterns across these projects</summary>

Conceptual patterns across separate projects; arrows do not assert one integrated deployment.

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
    OR[OpenRouter / Workers AI<br/>project-specific routing]
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
<summary><b>AI engineering stack</b> — tools and dependency evidence</summary>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/stack-dark.svg?v=20261102-audit" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/stack-light.svg?v=20261102-audit" />
    <img alt="AI stack" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/stack-dark.svg?v=20261102-audit" />
  </picture>
</p>

The card lists tools I use or explore. **The manifests below verify declared dependencies in these repos, rather than installed versions or live deployment.**

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
<summary><b>Now</b> — what I'm building in Q4 2026</summary>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/focus-dark.svg?v=20261102-audit" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/focus-light.svg?v=20261102-audit" />
    <img alt="Currently building" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/focus-dark.svg?v=20261102-audit" />
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
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/trajectory-dark.svg?v=20261102-audit" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/trajectory-light.svg?v=20261102-audit" />
    <img alt="Contribution trajectory by year" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/trajectory-dark.svg?v=20261102-audit" />
  </picture>
</p>

<p align="center">
  <a href="https://github.com/mangeshraut712?tab=overview&from=2021-01-01&to=2026-12-31">Contribution graph</a>
  ·
  <a href="https://github.com/mangeshraut712/mangeshraut712/blob/main/data/github-snapshot.json">yearly snapshot JSON</a>
</p>

</details>

