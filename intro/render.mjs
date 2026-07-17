/**
 * Code -> MP4 -> GIF renderer for the Apple-inspired GitHub intro.
 * Usage: node intro/render.mjs
 */
import { chromium } from "playwright";
import { spawn } from "node:child_process";
import { mkdirSync, existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, "..");
const framesDir = path.join(__dirname, ".frames");
const mp4Path = path.join(root, "header.mp4");
const gifPath = path.join(root, "header.gif");
const htmlPath = path.join(__dirname, "index.html");

function run(cmd, args) {
  return new Promise((resolve, reject) => {
    const child = spawn(cmd, args, { stdio: "inherit" });
    child.on("exit", (code) =>
      code === 0 ? resolve() : reject(new Error(`${cmd} exited ${code}`))
    );
  });
}

mkdirSync(framesDir, { recursive: true });

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({
  viewport: { width: 1100, height: 480 },
  deviceScaleFactor: 2,
});

await page.goto(`file://${htmlPath}`, { waitUntil: "networkidle" });
await page.waitForTimeout(1200);

const fps = 12;
const seconds = 6;
const total = fps * seconds;

for (let i = 0; i < total; i++) {
  const frame = String(i).padStart(4, "0");
  await page.locator("#stage").screenshot({
    path: path.join(framesDir, `frame-${frame}.png`),
    type: "png",
  });
  await page.waitForTimeout(Math.round(1000 / fps));
  if ((i + 1) % 12 === 0) console.log(`captured ${i + 1}/${total}`);
}

await browser.close();

console.log("encoding MP4...");
await run("ffmpeg", [
  "-y",
  "-framerate",
  String(fps),
  "-i",
  path.join(framesDir, "frame-%04d.png"),
  "-c:v",
  "libx264",
  "-pix_fmt",
  "yuv420p",
  "-vf",
  "scale=960:-2",
  mp4Path,
]);

console.log("encoding GIF...");
await run("ffmpeg", [
  "-y",
  "-i",
  mp4Path,
  "-vf",
  "fps=10,scale=960:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=64[p];[s1][p]paletteuse",
  "-loop",
  "0",
  gifPath,
]);

console.log("done:", {
  mp4: existsSync(mp4Path),
  gif: existsSync(gifPath),
  mp4Path,
  gifPath,
});
