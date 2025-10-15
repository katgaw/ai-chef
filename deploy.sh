#!/bin/bash

# AI Chef - Vercel Deployment Script
# This script helps you deploy your FastAPI app to Vercel

echo "🚀 AI Chef - Vercel Deployment"
echo "================================"
echo ""

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null
then
    echo "⚠️  Vercel CLI is not installed."
    echo ""
    echo "Installing Vercel CLI..."
    npm install -g vercel
    echo ""
fi

# Check if user is logged in
echo "📝 Checking Vercel authentication..."
if ! vercel whoami &> /dev/null
then
    echo "🔐 Please log in to Vercel:"
    vercel login
    echo ""
fi

# Deploy to Vercel
echo "🎯 Deploying to Vercel..."
echo ""
vercel --prod

echo ""
echo "✅ Deployment complete!"
echo ""
echo "📌 Your app should now be live on Vercel"
echo "💡 Don't forget to add your OpenAI API key when using the app"

