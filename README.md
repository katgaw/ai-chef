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

## Support

For issues or questions, please check the OpenAI API documentation or FastAPI documentation.

---

**Happy Cooking! 👨‍🍳**

