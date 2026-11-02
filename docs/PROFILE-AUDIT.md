# Profile source audit — November 2, 2026

Reviewed the existing README and all fourteen SVG assets against original repositories, source files, committed reports and upstream PRs. Preserved the existing profile structure and design. Self-described interests, tool preferences and contact links remain author statements; link reachability does not verify account ownership.

## Benchmarks and project scope

- VAD clean/noisy/soft F1: 0.9569 / 0.7768 / 0.8135. Whole-file batch p95: 39.33 ms, excluding warmup. Historical [September 11 CI job](https://github.com/mangeshraut712/ai-ml-portfolio/actions/runs/34574401205/job/103183795486), not a fresh local benchmark or per-frame latency promise. [Measurement code](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/labs/vad/challenge_pass.py).
- RAG figures remain explicitly offline/stub, from the [July 24 report](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/labs/llm-eval/reports/latest_report.json). Estimated cost and stub latency are not live provider measurements. [CI](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/.github/workflows/ci.yml) explicitly disables live mode.
- Agent Console describes its scripted mock server and seeded replay. [Server source](https://github.com/mangeshraut712/agent-console/blob/main/agent-server/src/index.ts).
- Gravity's [MCP-style registry](https://github.com/mangeshraut712/Gravity-SaaS-Agent/blob/main/packages/mcp-client/src/index.ts) is simulated. Its [provider](https://github.com/mangeshraut712/Gravity-SaaS-Agent/blob/main/apps/gateway/src/services/model-provider.ts) and [gateway](https://github.com/mangeshraut712/Gravity-SaaS-Agent/blob/main/apps/gateway/src/app.ts) implement retries/circuit breaking and echo fallback, rather than demonstrated multi-model failover.
- HindAI's [worker](https://github.com/mangeshraut712/Hindai/blob/main/workers/hindai-gemma/src/index.ts) uses Workers AI with optional OpenRouter.
- Architecture illustrations describe patterns across separate projects, not one verified integrated deployment. Dependency manifests establish declared dependencies, not deployed runtime versions.

## Upstream contributions

The 29/50 scoreboard is the personal organization-allowlist goal, separate from contribution-calendar PR counts and 14 CodeSync landings. Selected upstream merges checked against original PRs: [Lexical #9707](https://github.com/meta/lexical/pull/9707), [CUDA Python #3224](https://github.com/NVIDIA/cuda-python/pull/3224), [Apple #1178](https://github.com/apple/password-manager-resources/pull/1178), [AWS #4849](https://github.com/awslabs/mcp/pull/4849), [Adobe #10863](https://github.com/adobe/react-spectrum/pull/10863). Descriptions distinguish new regression tests, corrected assertions, schema validation and mocked platform selection. Windows end-to-end behavior was not independently reproduced.

## Generated statistics

[GitHub snapshot](../data/github-snapshot.json) and [WBM snapshot](../data/whoburnedmore-snapshot.json) record exact refresh timestamps. GitHub inventory now excludes private repositories even when the token can access them. Contribution figures use GitHub contribution-calendar scope; stars/forks sum public non-forks. WBM reports synced usage and provider-estimated cost, not payments. Cached period displays keep their original dates and visibly identify the cached source timestamp. WBM and the public ChatGPT profile have different coverage and are not added together.

The Actions Nurse submission time is an author-recorded repository stamp; this audit did not independently inspect a private portal receipt. No award, employment, enrollment, paid usage or completed theorem claim was added.

## Validation

All fourteen SVGs parse; dark/light text matches. Link audit checked 86 initial URLs: LinkedIn returned HTTP 999 (automation blocked), while the other 85 returned successful responses. Generator regression tests cover historical cached periods, cached source time and exclusion of private repositories. Browser previews inspect desktop/mobile layout and SVG text bounds. Remote project benchmarks and live model/provider behavior were not rerun. Workflow conflicts now stop instead of automatically overwriting concurrent changes.
