# 🚀 Vercel Deployment Guide

Quick guide to deploy your AI Chef app to Vercel.

## Prerequisites

- A Vercel account (sign up at [vercel.com](https://vercel.com))
- Git installed on your machine
- Your code pushed to a Git repository (GitHub, GitLab, or Bitbucket)

## Method 1: Automated Script (Recommended)

The easiest way to deploy:

```bash
./deploy.sh
```

This script handles everything automatically:
1. Checks if Vercel CLI is installed (installs if needed)
2. Verifies you're logged in (prompts login if needed)
3. Deploys your app to production
4. Provides you with the live URL

## Method 2: NPM Scripts

If you prefer using npm:

```bash
# Production deployment
npm run deploy

# Preview deployment (for testing)
npm run deploy:preview
```

## Method 3: Vercel Dashboard (No CLI Required)

1. Go to [vercel.com/new](https://vercel.com/new)
2. Import your Git repository
3. Vercel will auto-detect settings from `vercel.json`
4. Click "Deploy"
5. Done! 🎉

## Method 4: Manual CLI Deployment

Step by step:

```bash
# 1. Install Vercel CLI globally
npm install -g vercel

# 2. Login to your Vercel account
vercel login

# 3. Deploy to production
vercel --prod
```

## First Deployment Questions

When deploying for the first time, Vercel will ask:

```
? Set up and deploy "~/ai-chef"? [Y/n]
→ Press Y

? Which scope do you want to deploy to?
→ Choose your username/organization

? Link to existing project? [y/N]
→ Press N

? What's your project's name?
→ ai-chef (or customize)

? In which directory is your code located?
→ ./ (press Enter)
```

## After Deployment

You'll receive a URL like:
```
https://ai-chef-xxxx.vercel.app
```

### Testing Your Deployment

1. Visit the URL
2. Enter your OpenAI API key
3. Select a diet type
4. Generate a recipe!

## Updating Your Deployment

Every time you want to deploy updates:

```bash
# Quick update
./deploy.sh

# Or
npm run deploy

# Or
vercel --prod
```

## Configuration Files

The following files are configured for Vercel:

- **`vercel.json`**: Main configuration
  - Sets Python runtime
  - Defines build and route settings
  
- **`.vercelignore`**: Excludes unnecessary files
  - Python cache files
  - Virtual environments
  - Development files

- **`package.json`**: NPM deployment scripts

## Troubleshooting

### Issue: "Command not found: vercel"

**Solution**: Install Vercel CLI:
```bash
npm install -g vercel
```

### Issue: Python version errors

**Solution**: The app uses Python 3.9 on Vercel (configured in `vercel.json`). All dependencies are compatible.

### Issue: Static files not loading

**Solution**: The app is configured to handle static files correctly. If issues persist, check the `main.py` file paths.

### Issue: OpenAI API errors

**Solution**: This is client-side. Users need to provide valid OpenAI API keys.

## Environment Variables (Optional)

If you want to set default environment variables in Vercel:

1. Go to your project dashboard
2. Click "Settings" → "Environment Variables"
3. Add variables (though this app doesn't require any by default)

## Custom Domain

To add a custom domain:

1. Go to your project in Vercel
2. Click "Settings" → "Domains"
3. Add your domain
4. Follow DNS configuration instructions

## Monitoring

Vercel provides:
- Real-time logs
- Analytics
- Performance metrics

Access these in your project dashboard.

## Costs

- Vercel has a generous free tier
- OpenAI API costs depend on usage (GPT-4 requests)
- Users provide their own API keys, so you have no API costs

## Security Notes

- ✅ Never commit API keys to Git
- ✅ Users provide their own keys
- ✅ Keys are never stored on the server
- ✅ CORS is configured for security

## Rollback

If something goes wrong:

```bash
# List deployments
vercel ls

# Rollback to a previous deployment via dashboard
# Go to Vercel Dashboard → Deployments → Promote to Production
```

---

## Quick Commands Reference

```bash
# Deploy to production
./deploy.sh
# OR
npm run deploy
# OR
vercel --prod

# Deploy preview
npm run deploy:preview
# OR
vercel

# Check deployment status
vercel ls

# View logs
vercel logs

# Remove deployment
vercel remove [deployment-url]
```

---

**Need Help?**
- [Vercel Documentation](https://vercel.com/docs)
- [FastAPI on Vercel](https://vercel.com/docs/functions/serverless-functions/runtimes/python)

**Happy Deploying! 🚀**

