<!-- Profile README · Apple-clean · charcoal on #f5f5f7 / near-black · Nov 2026 -->

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/banner-dark.svg?v=2026111203" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/banner-light.svg?v=2026111203" />
    <img alt="Mangesh Raut — Software Engineer" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/banner-dark.svg?v=2026111203" />
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

---

### Engineering metrics — measured, with baselines and a failure case

VAD figures are from the [Sep 11, 2026 CI run](https://github.com/mangeshraut712/ai-ml-portfolio/actions/runs/34574401205) (batch whole-file processing, excluding warmup). RAG figures are offline stubs. [Source audit and verification limits](docs/PROFILE-AUDIT.md).

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/metrics-dark.svg?v=20261102-readability" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/metrics-light.svg?v=20261102-readability" />
    <img alt="Verified engineering metrics" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/metrics-dark.svg?v=20261102-readability" />
  </picture>
</p>

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
57 / 75  ███████████████░░░░░  76.0%
```

**57 merged pull requests** on the allowlist, goal 75, **18 to go**. Verified **2026-11-11**. [All 57 merged PRs and merge dates](data/oss-scoreboard.json).

**88 public external PRs merged overall**, including the 57 on this allowlist ([search](https://github.com/search?q=author%3Amangeshraut712+is%3Apr+is%3Amerged+-user%3Amangeshraut712+is%3Apublic&type=pullrequests)).

#### By company group (allowlist scoreboard)

| Company group | Merged | Focus |
| --- | ---: | --- |
| [Meta](https://github.com/meta/lexical/pull/9707) | 1 | Lexical |
| [Amazon/AWS](https://github.com/awslabs/stickler/pull/474) | 19 | MCP, Stickler, billing-cost fixes & Visual Asset Management System |
| [Microsoft](https://github.com/microsoft/playwright/pull/44030) | 10 | hve-core, winget-pkgs, physical-ai-toolchain, [Semantic Kernel](https://github.com/microsoft/semantic-kernel/pull/14668), Playwright docs |
| [Apple](https://github.com/apple/password-manager-resources/pull/1851) | 7 | Password-manager resources & schema |
| [NVIDIA](https://github.com/NVIDIA/cuda-python/pull/3241) | 5 | CUDA Python tests & TensorRT tooling/CI |
| [Adobe](https://github.com/adobe/react-spectrum/pull/10860) | 4 | React Aria / Spectrum (incl. ColorField Form validation & CheckboxGroup validation behavior) |
| [Sarvam AI](https://github.com/sarvamai/sarvam-ai-cookbook/pull/185) | 2 | Cookbook CI |
| [Google](https://github.com/google/sbsim/pull/187) | 4 | sbsim BUILD cleanup + [Gemini cookbook](https://github.com/google-gemini/cookbook/pull/1449) link checker + [ADK Go](https://github.com/google/adk-go/pull/1983) function-tool validation + [ADK Go executable code parts](https://github.com/google/adk-go/pull/1956) |
| [OpenAI](https://github.com/openai/codex-security/pull/754) | 1 | codex-security CLI guidance |
| [Netflix](https://github.com/Netflix/dgs-codegen/pull/997) | 1 | DGS codegen Kotlin client generation |
| [Samsung](https://github.com/Samsung/CredSweeper/pull/997) | 1 | CredSweeper install-guide docs |
| [Moonshot AI](https://github.com/MoonshotAI/kimi-code/pull/2416) | 1 | kimi-code models.dev fallback |
| [AMD](https://github.com/amd/gaia/pull/6656) | 1 | GAIA memory bootstrap confidence parsing |

#### Selected Engineering Impact

Five case studies selected from those 57 merges. Each links to the merged PR and its tests.

<details open>
<summary><b>Google · ADK-Go: preserve code-execution history across model providers</b></summary>

- **Problem:** Replaying Gemini conversation history through the OpenAI adapter failed when a turn contained executable code or execution output.
- **My contribution:** Converted both part types to labeled, fenced text in the Chat Completions and Responses request paths, preserving their order alongside ordinary text and images.
- **Validation:** Added request-payload regressions for both APIs, including empty code, mixed media and replayed reasoning. [Chat Completions tests](https://github.com/google/adk-go/blob/ded357e351dee44c023398a49d314aa326a59c94/model/openaimodel/internal/completions/request_test.go) · [Responses tests](https://github.com/google/adk-go/blob/ded357e351dee44c023398a49d314aa326a59c94/model/openaimodel/internal/responses/request_test.go).
- **Outcome:** [Merged November 6, 2026 · #1956](https://github.com/google/adk-go/pull/1956). Request conversion preserves the code and its output as context. This does not execute the code or claim live-provider validation.

</details>

<details>
<summary><b>Microsoft · Semantic Kernel: enforce URL allowlists after path normalization</b></summary>

- **Problem:** A raw prefix check let paths such as `/api/../admin` satisfy an `/api` allowlist even though the HTTP client requested `/admin`.
- **My contribution:** Required both raw and percent-decoded paths to pass the allowlist after dot-segment normalization, preserving empty segments and matching httpx's treatment of terminal dot segments.
- **Validation:** Added escaping-path and allowed-path cases, comparisons against httpx's wire path, and runner tests proving rejected targets never invoke authentication or send a request. [Validator tests](https://github.com/microsoft/semantic-kernel/blob/356acb66538a3f0f701a15105304c5c95428e51d/python/tests/unit/connectors/openapi_plugin/test_server_url_validator.py) · [Runner tests](https://github.com/microsoft/semantic-kernel/blob/356acb66538a3f0f701a15105304c5c95428e51d/python/tests/unit/connectors/openapi_plugin/test_openapi_runner.py).
- **Outcome:** [Merged November 2, 2026 · #14668](https://github.com/microsoft/semantic-kernel/pull/14668). The tested traversal and prefix-boundary cases are rejected before outbound work, while valid paths remain accepted.

</details>

<details>
<summary><b>Amazon/AWS · VAMS: handle stale DynamoDB index results during link recreation</b></summary>

- **Problem:** Recreating a deleted asset link could be rejected as a duplicate while DynamoDB's secondary index still returned the deleted row.
- **My contribution:** Verified candidate index hits against the base table with strongly consistent reads before applying duplicate and reverse-link checks.
- **Validation:** Added eight regression cases covering two relationship types, both directions, and stale versus present base-table records. [Regression tests](https://github.com/awslabs/visual-asset-management-system/blob/f1dc71deb25fbeae1d492b4f61cf6eb4261e0af5/backend/tests/handlers/assetLinks/test_createAssetLink_paging.py). The [project review](https://github.com/awslabs/visual-asset-management-system/pull/856#issuecomment-6452455132) reports 78 passing tests and 20 successful live smoke-test cycles; the original timing failure was reproduced in the regression test, not live.
- **Outcome:** [Merged into development November 2, 2026 · #856](https://github.com/awslabs/visual-asset-management-system/pull/856). Deleted rows no longer block recreation through stale index hits, while checks for existing duplicate and reverse links remain.

</details>

<details>
<summary><b>Netflix · DGS Codegen: resolve generated Kotlin parameter collisions</b></summary>

- **Problem:** GraphQL arguments named `_alias` or `_projection` collided with generated client parameters, producing Kotlin that failed to compile.
- **My contribution:** Preserved schema argument names and renamed only colliding generated parameters, leaving non-colliding signatures unchanged. Added tests that compile client queries using those arguments.
- **Validation:** [Compilation tests](https://github.com/Netflix/dgs-codegen/blob/d1ab1393ad05bdbc45408216c2aed91c3755e716/graphql-dgs-codegen-core/src/test/kotlin/com/netflix/graphql/dgs/codegen/Kotlin2CodeGenTest.kt). The [maintainer's follow-up](https://github.com/Netflix/dgs-codegen/pull/997#issuecomment-6617568565) retained my commit and added KotlinPoet name allocation, serializer-shadowing fixes and broader runtime coverage.
- **Outcome:** [Merged November 3, 2026 · #997](https://github.com/Netflix/dgs-codegen/pull/997). Colliding schema arguments can be used by the generated client without duplicate parameter declarations.

</details>

<details>
<summary><b>Meta · Lexical: keep the editor cursor inside custom DOM boundaries</b></summary>

- **Problem:** A block cursor placed after the last decorator could be appended beyond a custom DOM slot's trailing decoration, outside the editor-managed range.
- **My contribution:** Inserted the cursor before the slot boundary when attached, with an append fallback when the boundary is absent or removed.
- **Validation:** Added regressions for correct placement before the decoration and for a detached decoration that must not throw. [DOM-slot tests](https://github.com/meta/lexical/blob/63850fffbc003f44977996c2995d03dd0468aecc/packages/lexical/src/__tests__/unit/LexicalDOMSlot.test.tsx).
- **Outcome:** [Merged November 1, 2026 · #9707](https://github.com/meta/lexical/pull/9707). Custom slot layouts retain the expected cursor position without breaking the detached-boundary case.

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
    WS[WebSocket agent server<br/>seq reorder · dedupe · RESUME replay]
    API[FastAPI / Express gateway<br/>rate limits · circuit breaker]
  end
  subgraph Models_Tools_Data["Models · Tools · Data"]
    OR[OpenRouter / Workers AI<br/>project-specific routing]
    MCP[MCP-style tool registry<br/>tool calling]
    VAD[WebRTC VAD · speech]
    RAG[BM25 / TF-IDF retrieval<br/>eval gates]
    DB[(Supabase Postgres<br/>RLS policies)]
  end
  subgraph Ops
    CI[GitHub Actions CI<br/>F1 gate · offline eval]
    DEP[Docker · Cloudflare · GitHub Pages]
  end
  B <--> WS
  B --> API
  WS --> MCP
  API --> OR
  API --> RAG
  API --> DB
  B --> VAD
  MCP --> OR
  CI --> DEP
```

| Pattern | Where it lives | Evidence |
| --- | --- | --- |
| Ordered, deduplicated streaming + `RESUME` | agent-console | [reorderBuffer.ts](https://github.com/mangeshraut712/agent-console/blob/main/src/lib/reorderBuffer.ts) · [tests](https://github.com/mangeshraut712/agent-console/blob/main/src/lib/__tests__/reorderBuffer.test.ts) · [DECISIONS.md](https://github.com/mangeshraut712/agent-console/blob/main/DECISIONS.md) |
| Rate limits + circuit breaker | Gravity-SaaS-Agent gateway | [rate-limiter.ts](https://github.com/mangeshraut712/Gravity-SaaS-Agent/blob/main/apps/gateway/src/services/rate-limiter.ts) · [circuit-breaker.ts](https://github.com/mangeshraut712/Gravity-SaaS-Agent/blob/main/apps/gateway/src/services/circuit-breaker.ts) · [unit tests](https://github.com/mangeshraut712/Gravity-SaaS-Agent/tree/main/tests/unit/gateway) |
| Tenant isolation (RLS) | Gravity-SaaS-Agent | [supabase/schema.sql](https://github.com/mangeshraut712/Gravity-SaaS-Agent/blob/main/supabase/schema.sql) |
| MCP-style tools (**simulated**) | Gravity-SaaS-Agent | [mcp-client](https://github.com/mangeshraut712/Gravity-SaaS-Agent/blob/main/packages/mcp-client/src/index.ts) |
| Workers AI + optional OpenRouter | Hindai | [hindai-gemma worker](https://github.com/mangeshraut712/Hindai/blob/main/workers/hindai-gemma/src/index.ts) |
| CI gates, live APIs off | ai-ml-portfolio | [ci.yml](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/.github/workflows/ci.yml) (`EVAL_LIVE: "0"`, VAD `challenge_pass.py`) |
| Containers | agent-console · Gravity-SaaS-Agent | [docker-compose.yml](https://github.com/mangeshraut712/agent-console/blob/main/docker-compose.yml) · [docker-compose.yml](https://github.com/mangeshraut712/Gravity-SaaS-Agent/blob/main/docker-compose.yml) |

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

The card lists tools I use or explore. **The manifests below verify declared dependencies (checked 2026-11-10), not installed versions or live deployment.**

| Repo | Declared stack | Manifest |
| --- | --- | --- |
| ai-ml-portfolio | NumPy · webrtcvad · librosa · rank-bm25 · scikit-learn | [pyproject.toml](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/pyproject.toml) |
| agent-console | Next.js 16.4.3 · React 19.1 · TypeScript 5.8 · Turbopack · ws | [package.json](https://github.com/mangeshraut712/agent-console/blob/main/package.json) |
| Hindai | Next.js 15.5 · React 19.2 · Cloudflare Workers AI | [package.json](https://github.com/mangeshraut712/Hindai/blob/main/package.json) · [workers/hindai-gemma](https://github.com/mangeshraut712/Hindai/tree/main/workers/hindai-gemma) |
| Gravity-SaaS-Agent | Next.js 16.4 dashboard · Express 4 gateway · Supabase | [apps](https://github.com/mangeshraut712/Gravity-SaaS-Agent/tree/main/apps) |
| mangeshrautarchive | FastAPI · Uvicorn · Pydantic 2 · httpx | [requirements.txt](https://github.com/mangeshraut712/mangeshrautarchive/blob/main/requirements.txt) |
| career-agent-pro | FastAPI · OpenAI SDK · Pydantic 2 | [backend/requirements.txt](https://github.com/mangeshraut712/career-agent-pro/blob/main/backend/requirements.txt) |
| sarvam-ai-cookbook | Sarvam SDK · Flask-SocketIO · websockets | [Realtime_Speech_Captioning/requirements.txt](https://github.com/mangeshraut712/sarvam-ai-cookbook/blob/main/examples/Realtime_Speech_Captioning/requirements.txt) |

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

| Track | Where | Status (2026-11-10) |
| --- | --- | --- |
| Speech AI / VAD | [ai-ml-portfolio · labs/vad](https://github.com/mangeshraut712/ai-ml-portfolio/tree/main/labs/vad) | CI + VAD FULL_PASS gate green · [Nov 3 run](https://github.com/mangeshraut712/ai-ml-portfolio/actions/runs/41631353871) |
| RAG eval | [ai-ml-portfolio · labs/llm-eval](https://github.com/mangeshraut712/ai-ml-portfolio/tree/main/labs/llm-eval) | Offline stub report; live mode off in CI |
| Agent tooling | [agent-console](https://github.com/mangeshraut712/agent-console) · [actions-nurse](https://github.com/mangeshraut712/actions-nurse) | Incident Desk seeded replay shipped; live Nebius path not executed |
| MCP apps | [Gravity-SaaS-Agent](https://github.com/mangeshraut712/Gravity-SaaS-Agent) · upstream [awslabs/mcp](https://github.com/awslabs/mcp/pull/4846) | Registry simulated · 4 awslabs/mcp merges |
| OSS frameworks | [scoreboard](data/oss-scoreboard.json) | 49 of 57 allowlist merges landed in Q4 |

```text
Q4 2026 allowlist merges   Oct  19  ███████████████████░░░░░░░░░
                           Nov  29  █████████████████████████████  (through Nov 11, IST)
```

</details>

<details>
<summary><b>OSS merge pace</b> — allowlist merges by month</summary>

Merge dates from the [scoreboard](data/oss-scoreboard.json), grouped by IST month. November is partial (through 2026-11-11).

```mermaid
xychart-beta
  title "Allowlist merges per month (2026)"
  x-axis [Jul, Aug, Sep, Oct, Nov]
  y-axis "Merged PRs" 0 --> 30
  bar [2, 3, 3, 19, 29]
```

| Repo (top 5) | Merged |
| --- | ---: |
| [awslabs/visual-asset-management-system](https://github.com/awslabs/visual-asset-management-system/pulls?q=is%3Apr+is%3Amerged+author%3Amangeshraut712) | 12 |
| [apple/password-manager-resources](https://github.com/apple/password-manager-resources/pulls?q=is%3Apr+is%3Amerged+author%3Amangeshraut712) | 7 |
| [microsoft/physical-ai-toolchain](https://github.com/microsoft/physical-ai-toolchain/pulls?q=is%3Apr+is%3Amerged+author%3Amangeshraut712) | 6 |
| [adobe/react-spectrum](https://github.com/adobe/react-spectrum/pulls?q=is%3Apr+is%3Amerged+author%3Amangeshraut712) | 4 |
| [awslabs/mcp](https://github.com/awslabs/mcp/pulls?q=is%3Apr+is%3Amerged+author%3Amangeshraut712) | 4 |

</details>

<details>
<summary><b>In review</b> — open upstream pull requests</summary>

Snapshot **2026-11-10 13:29 IST** from GitHub search: **113 open PRs across 32 owners** ([live list](https://github.com/search?q=author%3Amangeshraut712+is%3Apr+is%3Aopen+-user%3Amangeshraut712&type=pullrequests)).

```text
Awaiting review      70  ████████████░░░░░░░░  62%
No review required   35  ██████░░░░░░░░░░░░░░  31%
Changes requested     5  █░░░░░░░░░░░░░░░░░░░   4%
Draft                 2  ░░░░░░░░░░░░░░░░░░░░   2%
Approved              1  ░░░░░░░░░░░░░░░░░░░░   1%
```

| Owner | Open PRs |
| --- | ---: |
| [awslabs](https://github.com/search?q=author%3Amangeshraut712+is%3Apr+is%3Aopen+org%3Aawslabs&type=pullrequests) | 17 |
| [anthropics](https://github.com/search?q=author%3Amangeshraut712+is%3Apr+is%3Aopen+org%3Aanthropics&type=pullrequests) | 11 |
| [microsoft](https://github.com/search?q=author%3Amangeshraut712+is%3Apr+is%3Aopen+org%3Amicrosoft&type=pullrequests) | 8 |
| [adobe](https://github.com/search?q=author%3Amangeshraut712+is%3Apr+is%3Aopen+org%3Aadobe&type=pullrequests) | 7 |
| [MoonshotAI](https://github.com/search?q=author%3Amangeshraut712+is%3Apr+is%3Aopen+org%3AMoonshotAI&type=pullrequests) | 7 |
| 27 other owners | 63 |

</details>

<details>
<summary><b>Principles, writing, trajectory</b></summary>

**Engineering principles** — each one, where it shows up in code

- **Measure everything; ship the gate with the number** — VAD F1 gate runs in [CI](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/.github/workflows/ci.yml) and fails below threshold
- **Local-first; CI must not depend on a live API** — CI sets `EVAL_LIVE: "0"`; agent-console ships a key-free [replay](https://github.com/mangeshraut712/agent-console/blob/main/src/agent/replay.ts)
- **Reliability over novelty** — tested [circuit breaker](https://github.com/mangeshraut712/Gravity-SaaS-Agent/blob/main/tests/unit/gateway/circuit-breaker.test.ts) and [rate limiter](https://github.com/mangeshraut712/Gravity-SaaS-Agent/blob/main/tests/unit/gateway/rate-limiter.test.ts)
- **AI should augment, not obscure, the system** — Incident Desk shows the planner/tool trace and scorecard ([eval.ts](https://github.com/mangeshraut712/agent-console/blob/main/src/agent/eval.ts))
- **Developer experience matters; simple systems scale better** — `make verify-all` runs the tests, VAD gate and offline eval with no API keys

Details: [INTERVIEW_NOTES.md](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/INTERVIEW_NOTES.md)

**Writing** — [Technical writings RSS](https://mangeshraut712.github.io/mangeshrautarchive/rss.xml) (20 posts in the feed)

| Date | Latest posts |
| --- | --- |
| Oct 29, 2026 | [Touchscreen MacBook Pro field notes](https://mangeshraut712.github.io/mangeshrautarchive/blog/macbook-pro-touchscreen-proled-xdr-2026.html) |
| Oct 28, 2026 | [Gemini 4 Argon and Carbon field notes](https://mangeshraut712.github.io/mangeshrautarchive/blog/gemini-4-argon-and-carbon-deepmind-2026.html) |
| Sep 29, 2026 | [OpenAI DevDay 2026: models, ongoing agents, reliable workflows](https://mangeshraut712.github.io/mangeshrautarchive/blog/openai-devday-2026.html) |
| Sep 10, 2026 | [Razorpay Vulcan: evaluating a payments foundation model](https://mangeshraut712.github.io/mangeshrautarchive/blog/razorpay-vulcan-payments-foundation-model.html) |

**Trajectory**

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/trajectory-dark.svg?v=20261102-audit" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/trajectory-light.svg?v=20261102-audit" />
    <img alt="Contribution trajectory by year" width="820" src="https://raw.githubusercontent.com/mangeshraut712/mangeshraut712/main/trajectory-dark.svg?v=20261102-audit" />
  </picture>
</p>

```text
2026 so far (snapshot 2026-11-10 07:02 IST)   5,021 contributions
  Commits        3,309  █████████████░░░░░░░  66%
  Pull requests  1,396  ██████░░░░░░░░░░░░░░  28%
  Reviews          156  █░░░░░░░░░░░░░░░░░░░   3%
  Issues            67  ░░░░░░░░░░░░░░░░░░░░   1%
```

<p align="center">
  <a href="https://github.com/mangeshraut712?tab=overview&from=2021-01-01&to=2026-12-31">Contribution graph</a>
  ·
  <a href="https://github.com/mangeshraut712/mangeshraut712/blob/main/data/github-snapshot.json">yearly snapshot JSON</a>
</p>

</details>
