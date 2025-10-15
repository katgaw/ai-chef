# 🍳 AI Chef - Diet Recipe Generator

A beautiful and simple FastAPI application that generates personalized dinner recipes using GPT-4, tailored to your dietary preferences (vegetarian or vegan).

## Features

- 🎨 Modern, responsive UI with smooth animations
- 🌱 Support for vegetarian and vegan diets
- 🤖 Powered by OpenAI's GPT-4
- 🔒 Secure - API key is never stored, only used for requests
- ⚡ Fast and lightweight

## Requirements

- Python 3.13
- OpenAI API Key ([Get one here](https://platform.openai.com/api-keys))

## Installation

1. Clone or download this repository

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the FastAPI server:
```bash
python main.py
```

Or alternatively:
```bash
uvicorn main:app --reload
```

2. Open your browser and navigate to:
```
http://localhost:8000
```

3. Enter your OpenAI API key and select your diet preference to generate a recipe!

## Usage

1. **Enter API Key**: Paste your OpenAI API key in the password field
2. **Select Diet**: Choose between Vegetarian or Vegan
3. **Generate**: Click the "Generate Recipe" button
4. **Enjoy**: Get a personalized, simple dinner recipe!

## API Endpoints

- `GET /` - Serves the main web interface
- `POST /generate-recipe` - Generates a recipe based on diet preferences
- `GET /health` - Health check endpoint

## Technologies Used

- **FastAPI** - Modern Python web framework
- **OpenAI API** - GPT-4 for recipe generation
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation

## Security Note

Your OpenAI API key is only used for generating recipes and is never stored on the server. Each request uses the key you provide and discards it after use.

## Python 3.13 Compatibility

All dependencies have been tested and are compatible with Python 3.13:
- fastapi==0.115.4
- uvicorn==0.32.0
- openai==1.51.0
- pydantic==2.9.2

## License

MIT License - Feel free to use and modify as needed!

## 🚀 Deploying to Vercel

This app is ready to deploy to Vercel with just a few commands!

### Option 1: Using the Deploy Script (Easiest)

```bash
./deploy.sh
```

This script will:
- Install Vercel CLI if needed
- Log you in to Vercel
- Deploy your app to production

### Option 2: Using NPM Scripts

```bash
# Deploy to production
npm run deploy

# Deploy a preview (for testing)
npm run deploy:preview
```

### Option 3: Manual Deployment

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Login to Vercel:
```bash
vercel login
```

3. Deploy:
```bash
vercel --prod
```

### First Time Deployment

On your first deployment, Vercel will ask you a few questions:
- **Set up and deploy?** → Yes
- **Which scope?** → Choose your account
- **Link to existing project?** → No
- **What's your project's name?** → ai-chef (or your preferred name)
- **In which directory is your code located?** → ./

After deployment, you'll get a URL like: `https://ai-chef-xxxx.vercel.app`

### Important Notes

- ⚠️ **Python Version**: Vercel uses Python 3.9 by default (configured in `vercel.json`)
- 🔒 **Security**: Never commit your OpenAI API key. Users will provide their own keys.
- 🌐 **Custom Domain**: You can add a custom domain in your Vercel dashboard

## Files for Vercel Deployment

- `vercel.json` - Vercel configuration
- `.vercelignore` - Files to exclude from deployment
- `deploy.sh` - Automated deployment script
- `package.json` - NPM scripts for easy deployment

## Support

For issues or questions, please check the OpenAI API documentation or FastAPI documentation.

---

**Happy Cooking! 👨‍🍳**

