# Profile source audit — November 3, 2026

Reviewed the existing README and all fourteen SVG assets against original repositories, source files, committed reports and upstream PRs. Preserved the existing profile structure and design. Self-described interests, tool preferences and contact links remain author statements; link reachability does not verify account ownership.

## Benchmarks and project scope

- VAD clean/noisy/soft F1: 0.9569 / 0.7768 / 0.8135. Whole-file batch p95: 39.33 ms, excluding warmup. Historical [September 11 CI job](https://github.com/mangeshraut712/ai-ml-portfolio/actions/runs/34574401205/job/103183795486), not a fresh local benchmark or per-frame latency promise. [Measurement code](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/labs/vad/challenge_pass.py).
- RAG figures remain explicitly offline/stub, from the [July 24 report](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/labs/llm-eval/reports/latest_report.json). Estimated cost and stub latency are not live provider measurements. [CI](https://github.com/mangeshraut712/ai-ml-portfolio/blob/main/.github/workflows/ci.yml) explicitly disables live mode.
- Agent Console now includes **Incident Desk**: three Northwind seeded investigations, labelled key-free recorded replay, planner/tool trace, verdict and seed-based scorecard. The original WebSocket protocol console remains. The [replay implementation](https://github.com/mangeshraut712/agent-console/blob/main/src/agent/replay.ts), [live loop](https://github.com/mangeshraut712/agent-console/blob/main/src/agent/loop.ts), [Nebius client](https://github.com/mangeshraut712/agent-console/blob/main/src/agent/nebius.ts), [scorecard](https://github.com/mangeshraut712/agent-console/blob/main/src/agent/eval.ts) and [mock-fetch tests](https://github.com/mangeshraut712/agent-console/blob/main/src/agent/loop.test.ts) support that scope. Live-capable Nemotron via Nebius is implemented, but the project README records that Token Factory execution was not performed; this audit made no live inference calls. Replay does not call Nebius or Tavily, and the internal telemetry remains seeded even in live mode.
- Gravity's [MCP-style registry](https://github.com/mangeshraut712/Gravity-SaaS-Agent/blob/main/packages/mcp-client/src/index.ts) is simulated. Its [provider](https://github.com/mangeshraut712/Gravity-SaaS-Agent/blob/main/apps/gateway/src/services/model-provider.ts) and [gateway](https://github.com/mangeshraut712/Gravity-SaaS-Agent/blob/main/apps/gateway/src/app.ts) implement retries/circuit breaking and echo fallback, rather than demonstrated multi-model failover.
- HindAI's [worker](https://github.com/mangeshraut712/Hindai/blob/main/workers/hindai-gemma/src/index.ts) uses Workers AI with optional OpenRouter.
- Architecture illustrations describe patterns across separate projects, not one verified integrated deployment. Dependency manifests establish declared dependencies, not deployed runtime versions.

## Upstream contributions

The 41/50 scoreboard is the personal organization-allowlist goal, separate from contribution-calendar PR counts and 14 historically recorded CodeSync landings. November 3 owner-scoped GitHub merged-PR searches confirm Apple 7, Microsoft 8, Adobe 3, AWS Labs 11, NVIDIA 4, Sarvam 2, OpenAI 1, Google plus google-gemini 2, Moonshot 1, Samsung 1 and Meta 1 (total 41). [Search evidence](../data/oss-scoreboard.json) records those nonzero groups. Fresh checks for some zero-count groups were limited by GitHub search throttling; existing zero rows were retained rather than presented as newly verified. Selected upstream merges checked against original PRs: [Lexical #9707](https://github.com/meta/lexical/pull/9707), [CUDA Python #3224](https://github.com/NVIDIA/cuda-python/pull/3224), [Semantic Kernel #14668](https://github.com/microsoft/semantic-kernel/pull/14668), [AWS #4849](https://github.com/awslabs/mcp/pull/4849), [Adobe #10863](https://github.com/adobe/react-spectrum/pull/10863). Descriptions distinguish new regression tests, corrected assertions, schema validation and mocked platform selection. The Semantic Kernel merged patch normalizes both raw and fully percent-decoded paths; its implementation, rather than the narrower PR summary, controls the profile wording. Windows end-to-end behavior was not independently reproduced.

## Generated statistics

[GitHub snapshot](../data/github-snapshot.json) and [WBM snapshot](../data/whoburnedmore-snapshot.json) record exact refresh timestamps. GitHub inventory now excludes private repositories even when the token can access them. Contribution figures use GitHub contribution-calendar scope; stars/forks sum public non-forks. WBM reports synced usage and provider-estimated cost, not payments. Cached period displays keep their original dates and visibly identify the cached source timestamp. WBM and the public ChatGPT profile have different coverage and are not added together.

The Actions Nurse submission time is an author-recorded repository stamp; this audit did not independently inspect a private portal receipt. No award, employment, enrollment, paid usage or completed theorem claim was added.

## Validation

All fourteen SVGs parse; dark/light text matches. The November 2 link audit checked 105 URLs: LinkedIn returned HTTP 999 (automation blocked); the other 104 returned successful responses. November 3 rechecks use original source files for the existing project, dependency and benchmark claims; the historical benchmark results are not presented as newly reproduced. Generator regression tests cover historical cached periods, cached source time and exclusion of private repositories, and preservation of the authored benchmark card during refresh. Browser previews inspect desktop/mobile layout and SVG text bounds. Remote project benchmarks and live model/provider behavior were not rerun. Workflow conflicts now stop instead of automatically overwriting concurrent changes.

## November 6, 2026: OSS milestone and case-study refresh

The earlier 41/50 paragraph is a historical November 3 snapshot. The current [scoreboard](../data/oss-scoreboard.json) records **50 qualifying merged PRs** across **13 company groups** and a new **75-merge goal**. A complete public external merged-PR search returned 81 unique results with `incomplete_results=false`; its URLs, authors and merge dates match the previous canonical REST audit plus [Google ADK-Go #1956](https://github.com/google/adk-go/pull/1956), merged at 09:37:27 UTC on November 6. The 50 qualifying records retain canonical owner names, immutable PR IDs and merge timestamps. Google includes `google` and `google-gemini`, without double counting. CodeSync-only landings are excluded.

The five case studies now cover Google ADK-Go #1956, Microsoft Semantic Kernel #14668, AWS VAMS #856, Netflix DGS Codegen #997 and Meta Lexical #9707. Selection favors substantive behavior changes, test evidence and complementary engineering skills. All five were checked against their merged patches, tests and relevant review discussions. README test links are pinned to merge commits.

Validation boundaries:

- Google: request construction and history preservation, not live-provider execution or execution of the preserved code.
- Semantic Kernel: the tested allowlist/path-normalization cases, not a claim to eliminate every network security risk.
- AWS VAMS: the project review reports 78 passing tests and 20 successful live smoke-test cycles. The timing failure was reproduced by the regression test, not by live smoke tests. The review was AI-assisted; its reported results were not rerun during this profile refresh. The PR merged to `development`; no release claim is made.
- Netflix: the original parameter-collision contribution is distinguished from the maintainer's name-allocation, serializer-shadowing and expanded runtime-test follow-up. The stale release forecast has been removed.
- Lexical: attached and removed DOM-slot boundary cases, not a claim about all editor selection behavior.

The refresh changes only the OSS README section, scoreboard and this dated addendum, plus local consistency tests. Project descriptions, benchmarks, contact links, design and generated banner statistics are unchanged. The new tests check unique authored merges, owner/group totals, README progress, and exactly five merged cases with immutable test links. Existing profile-sync regressions are also run. Upstream project test suites are source evidence here and were not rerun for this documentation change.

## November 8, 2026: OSS count refresh

The current [scoreboard](../data/oss-scoreboard.json) records **52 qualifying merged PRs** across **13 company groups**, **83 public external merged PRs overall**, and **23 remaining** toward the 75-merge goal. A fresh complete public external merged-PR search returned 83 unique results with `incomplete_results=false`. All 51 previous qualifying URLs, authors and merge dates still match that search.

The additional qualifying merge is [Microsoft physical-ai-toolchain #2074](https://github.com/microsoft/physical-ai-toolchain/pull/2074), authored by `mangeshraut712` and merged on November 8 at 06:44:26 UTC. Its canonical pull record confirms `merged=true`; Microsoft now has nine qualifying merges. The fix adds policy deltas to current joint positions in ACT delta mode and leaves absolute-mode policy positions unchanged. This profile refresh does not claim hardware validation or rerun the upstream test suite.

The five selected case studies and the profile's design, projects, benchmarks and generated assets remain unchanged. Self-owned PRs and CodeSync-only landings remain excluded from the merged-PR counts. The README, evidence snapshot and dated audit were refreshed together; local consistency checks also cover the external total, progress percentage and case-study count reference.

## November 9, 2026: Stickler merge refresh

The current [scoreboard](../data/oss-scoreboard.json) records **53 qualifying merged PRs** across **13 company groups**, **84 public external merged PRs overall**, and **22 remaining** toward the 75-merge goal. A fresh complete public external merged-PR search returned 84 unique results with `incomplete_results=false`. All 52 previous qualifying URLs, authors and merge dates still match that search.

The additional qualifying merge is [Amazon/AWS Stickler #455](https://github.com/awslabs/stickler/pull/455), authored by `mangeshraut712` and merged by `digalaviz` on November 8 at 21:50:14 UTC. Its canonical pull record confirms `merged=true`; Amazon/AWS now has 16 qualifying merges. The merged patch converts document keys and paths to strings before HTML escaping in both image and PDF galleries, with regression coverage for integer and NumPy keys, `pathlib.Path` values and preservation of entries whose string keys collide. The upstream test suite was inspected as evidence, not rerun for this documentation refresh.

The five case studies, all unrelated README content and generated assets remain unchanged. Self-owned PRs and CodeSync-only landings remain excluded. The README and evidence snapshot were refreshed together and checked with the existing profile consistency tests.

## November 9, 2026: AWS MCP merge refresh

The current [scoreboard](../data/oss-scoreboard.json) records **54 qualifying merged PRs** across **13 company groups**, **85 public external merged PRs overall**, and **21 remaining** toward the 75-merge goal. A fresh complete public external merged-PR search returned 85 unique results with `incomplete_results=false`. All 53 previous qualifying URLs, authors and merge dates still match that search.

The additional qualifying merge is [Amazon/AWS MCP #4846](https://github.com/awslabs/mcp/pull/4846), authored by `mangeshraut712` and merged by `kennthhz` on November 9 at 18:55:26 UTC. Its canonical pull record confirms `merged=true` and merge commit [730add86](https://github.com/awslabs/mcp/commit/730add86aba3bec19f820ae501462059d25af33a); Amazon/AWS now has 17 qualifying merges. The merged patch moves PostgreSQL PG-wire startup validation onto the MCP serving event loop and closes cached connections on that loop during shutdown. Regression coverage exercises startup through the registered lifespan, the first query, cleanup and deliberate startup refusal. The merged patch and test changes were inspected as source evidence; the upstream test suite and live PostgreSQL behavior were not rerun for this documentation refresh.

Only the OSS section of the existing README, the scoreboard and this dated addendum are updated. The five case studies, all unrelated README content and generated assets remain unchanged. Self-owned PRs and CodeSync-only landings remain excluded. Existing profile consistency and synchronization tests pass.
