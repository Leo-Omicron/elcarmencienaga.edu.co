#!/usr/bin/env node
/**
 * Automated deployment script for demos.elcarmencienaga.edu.co
 * Invokes @hostinger/mcp (hostinger-hosting-mcp) over stdio using HOSTINGER_API_TOKEN
 * (or local OAuth credentials) to deploy ./demos and clear the website cache.
 */

import { spawn } from "node:child_process";
import path from "node:path";
import process from "node:process";

const DOMAIN = "demos.elcarmencienaga.edu.co";
const USERNAME = "u985679183";
const DEMOS_PATH = path.resolve(process.cwd(), "demos");

function createMcpClient() {
  const isWin = process.platform === "win32";
  const cmd = isWin ? "cmd.exe" : "npx";
  const args = isWin
    ? ["/d", "/s", "/c", "npx --yes --package=@hostinger/mcp@latest hostinger-hosting-mcp"]
    : ["--yes", "--package=@hostinger/mcp@latest", "hostinger-hosting-mcp"];
  const child = spawn(cmd, args, {
    stdio: ["pipe", "pipe", "inherit"],
    env: process.env,
  });

  let buffer = "";
  let nextId = 1;
  const pending = new Map();

  child.stdout.on("data", (chunk) => {
    buffer += chunk.toString("utf8");
    const lines = buffer.split("\n");
    buffer = lines.pop() ?? "";
    for (const line of lines) {
      const trimmed = line.trim();
      if (!trimmed) continue;
      try {
        const msg = JSON.parse(trimmed);
        if (msg.id && pending.has(msg.id)) {
          const { resolve, reject } = pending.get(msg.id);
          pending.delete(msg.id);
          if (msg.error) {
            reject(new Error(JSON.stringify(msg.error)));
          } else {
            resolve(msg.result);
          }
        }
      } catch {
        // Ignore non-JSON stdout lines
      }
    }
  });

  function request(method, params = {}) {
    const id = nextId++;
    const payload = JSON.stringify({ jsonrpc: "2.0", id, method, params }) + "\n";
    return new Promise((resolve, reject) => {
      pending.set(id, { resolve, reject });
      child.stdin.write(payload);
    });
  }

  function close() {
    child.stdin.end();
    child.kill();
  }

  return { request, close };
}

async function main() {
  const client = createMcpClient();
  try {
    await client.request("initialize", {
      protocolVersion: "2024-11-05",
      capabilities: {},
      clientInfo: { name: "ieec-demos-deployer", version: "1.0.0" },
    });

    console.log(`Deploying ${DEMOS_PATH} to ${DOMAIN}...`);
    const deployRes = await client.request("tools/call", {
      name: "execute",
      arguments: {
        operation: "hosting_deploy",
        params: {
          domain: DOMAIN,
          path: DEMOS_PATH,
          type: "static",
        },
      },
    });
    console.log("Deploy result:", JSON.stringify(deployRes));

    console.log(`Clearing cache for ${DOMAIN}...`);
    const cacheRes = await client.request("tools/call", {
      name: "execute",
      arguments: {
        operation: "hosting_cache_clear-website",
        params: {
          domain: DOMAIN,
          username: USERNAME,
        },
      },
    });
    console.log("Cache clear result:", JSON.stringify(cacheRes));
  } finally {
    client.close();
  }
}

main().catch((err) => {
  console.error("Deployment failed:", err);
  process.exit(1);
});
