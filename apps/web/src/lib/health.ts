import { z } from "zod";

/** Runtime schema for the API's `GET /health` response. */
export const healthResponseSchema = z.object({
  status: z.literal("ok"),
});

export type HealthResponse = z.infer<typeof healthResponseSchema>;

export function parseHealthResponse(payload: unknown): HealthResponse {
  return healthResponseSchema.parse(payload);
}
