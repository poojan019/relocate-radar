import { describe, expect, it } from "vitest";

import { parseHealthResponse } from "@/lib/health";

describe("parseHealthResponse", () => {
  it("accepts a healthy payload", () => {
    expect(parseHealthResponse({ status: "ok" })).toEqual({ status: "ok" });
  });

  it("rejects an unexpected payload", () => {
    expect(() => parseHealthResponse({ status: "down" })).toThrow();
  });
});
