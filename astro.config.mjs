import { defineConfig } from 'astro/config';

// Built output is synced to the repo root so GitHub Pages can serve it with
// no build step and no Actions dependency — deploys stay dumb and reliable.
export default defineConfig({
  site: 'https://sachdm.github.io',
  base: '/blue-sheep-site',
  outDir: './dist',
  build: { format: 'file', assets: '_assets' },
  devToolbar: { enabled: false },
});
