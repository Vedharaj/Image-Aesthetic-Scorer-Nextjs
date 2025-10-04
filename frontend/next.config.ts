/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    serverActions: true,
    serverActionsBodySizeLimit: 10 * 1024 * 1024, // 10 MB
  },
};

module.exports = nextConfig;
