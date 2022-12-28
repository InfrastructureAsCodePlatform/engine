import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

import dns from 'dns'

dns.setDefaultResultOrder('verbatim')

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  server: {
    proxy: {
      '^/auth': {
        target: `http://${process.env.API_BASE || 'localhost'}:${process.env.API_PORT || '8000'}/api/v1/`,
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/auth/, ''),
      }
    },
    host: process.env.FRONTEND_HOST || 'localhost',
    port: parseInt(process.env.FRONTEND_PORT || '3001')
  }
});
