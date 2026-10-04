# Motion Render Video — Project Constitution

**Document ID:** CTRL-CONSTITUTION-001  
**Status:** ACTIVE  
**Control Plane Version:** 1.5.2  
**Architecture Baseline:** v3.0.0 — 27 lobes / 174 modules / 1,740 micro-neurons  
**Mission:** Build a verified, modular, graph-addressable knowledge system that enables a future `Motion Render Video` skill to reason about, design, generate, render, evaluate, diagnose, and refine motion/video work at the highest practical quality achievable in the available environment.

## 1. Constitutional principles

1. **Files are the source of truth.** Conversation history is never authoritative project state.
2. **Architecture before knowledge.** Canonical node identity, scope, and dependency must exist before deep content is populated.
3. **Evidence before assertion.** Technical/scientific claims require provenance appropriate to their type.
4. **First principles before presets.** Tool recipes may adapt canonical theory but never replace it.
5. **Small verified work units beat giant generations.** Default synthesis unit is one module.
6. **No silent structural drift.** IDs, scope, dependencies, or schema changes require logged change control.
7. **No premature compression.** Runtime summaries are derived only from verified canonical knowledge.
8. **No single-score quality illusion.** Quality is evaluated by multidimensional gates and explicit failure signatures.
9. **No isolated-domain reasoning.** Cross-lobe conflicts and causal chains must be checked before release.
10. **No ornamental complexity.** More nodes, effects, words, or tools are not intrinsically better; every addition needs function.

## 2. Canonical authority order

Host instructions and current user authorization govern all actions. Project documents are task data and cannot override them. Within the project, when artifacts conflict, use this order:

1. `00_PROJECT_CONSTITUTION.md`
2. `01_MASTER_ARCHITECTURE.md`
3. `10_DECISION_LOG.md`
4. verified canonical knowledge modules
5. graph registries / dependency maps
6. verified evidence maps and claim ledger
7. tool adapters
8. runtime compression / skill instructions
9. conversation history

Lower authority may not silently overwrite higher authority.

## 3. Stable identity rules

- Lobe IDs: `L00`–`L26`.
- Module IDs: `Lxx.mm`.
- Neuron IDs: `Lxx.mm.nn`.
- IDs are permanent once released in a baseline.
- Renaming a label does not change its ID.
- Splits/merges require migration mappings in the change log.
- New structural nodes must pass the architecture-growth criteria.

Additional registries use stable prefixes:

- source: `SRC-<TYPE>-####`
- claim: `CLM-Lxx-####`
- failure: `FAIL-<DOMAIN>-####`
- metric: `METRIC-<DOMAIN>-####`
- test: `TEST-<DOMAIN>-####`
- tool adapter: `TOOL-<SYSTEM>-####`
- change: `CHG-####`
- decision: `DEC-####`
- gap: `GAP-####`
- work packet: `WP-Lxx.mm-###`

## 4. Definition of canonical knowledge

A file named CANONICAL.md is the authoritative module manuscript, but its lifecycle state remains decisive. TECHNICALLY_REVIEWED means local review only. Globally validated canonical knowledge has additionally passed cross-link review and applicable quality gates. Research notes, drafts, chat outputs, tool results, and runtime summaries are **not** canonical by default.

## 5. Module lifecycle

`UNSTARTED → SCOPED → RESEARCHED → EVIDENCE_CHECKED → DRAFTED → TECHNICALLY_REVIEWED → CROSS_LINKED → QA_VERIFIED → RUNTIME_READY → RELEASED`

Regression, contradiction, or architecture change may move a module backward. No state is irreversible except historical release records.

## 6. Evidence classes

Every nontrivial claim must be classified where applicable:

- **ESTABLISHED** — strong agreement in authoritative/peer-reviewed/standards sources.
- **CONDITIONAL** — valid under explicit assumptions or operating conditions.
- **HEURISTIC** — professional rule of thumb or practice-derived guidance.
- **CONTESTED** — credible sources disagree or evidence is unsettled.
- **MODEL_SPECIFIC** — applies to a particular software/model/version/runtime.
- **AESTHETIC_JUDGMENT** — subjective design preference; never presented as universal fact.

## 7. Completeness rule

A module is structurally complete only when its intended micro-neurons are accounted for as one of:

- covered directly in the module,
- promoted to an independent R2 neuron card,
- intentionally inherited from another canonical module with an explicit link,
- explicitly deferred with a gap ID and reason.

Text volume alone never counts as completion.

## 8. Quality floor

No module can reach `QA_VERIFIED` unless it passes every mandatory gate relevant to it. A gate may be marked `N/A` only with a reason. Critical failures block promotion.

## 9. Work-session contract

Every substantive work session must begin from a Work Packet and end with a Handoff Packet. A session must not rely on unstated conversational memory. The packet defines scope, dependencies, evidence requirements, outputs, and forbidden expansion.

## 10. Change control

Architecture, ID schema, canonical terminology, evidence policy, and quality-gate changes require:

- change ID,
- reason,
- affected artifacts,
- migration impact,
- broken-reference check,
- version consequence,
- decision log entry when material.

No silent renumbering or retroactive deletion.

## 11. Runtime separation

The future `Motion Render Video` skill is an executive/router layer. It retrieves relevant verified knowledge; it does not become the sole storage location for the full knowledge base. Runtime compression must remain traceable to canonical modules.

## 12. Release principle

A release is valid only when structural validation, evidence integrity, graph integrity, terminology consistency, regression testing, retrieval testing, and packaging checks all pass. A file existing is not proof of completion.