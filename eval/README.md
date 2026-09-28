# eval

Search-quality evaluation for RelocateRadar.

> Status: placeholder. Code lands once there is a search to evaluate.

## Plan

- A labeled query set, with relevance judgments per (query, job) pair.
- Metrics: **nDCG@10** and **recall@20**.
- Compare three retrieval modes: keyword-only (Postgres FTS), vector-only (Qdrant), and hybrid (RRF).
- Results are reproducible from a fixed snapshot of the index. No live crawling.
