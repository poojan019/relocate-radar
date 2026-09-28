# relocate-web

Next.js (App Router, TypeScript strict) frontend for RelocateRadar.
API responses are validated at runtime with Zod.

> Status: scaffold only. It has a landing page and a Zod schema for the API health check.

## Setup

```bash
cd apps/web
pnpm install
pnpm dev        # http://localhost:3000
```

## Checks

```bash
pnpm lint       # ESLint (next/core-web-vitals + next/typescript)
pnpm typecheck  # tsc --noEmit
pnpm test       # vitest
pnpm build      # production build
```
