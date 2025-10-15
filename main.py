from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI(title="AI Chef - Diet Recipe Generator")

class RecipeRequest(BaseModel):
    api_key: str
    diet_type: str

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve the main HTML page"""
    with open("static/index.html", "r") as f:
        return f.read()

@app.post("/generate-recipe")
async def generate_recipe(request: RecipeRequest):
    """Generate a recipe based on diet preference using GPT-4"""
    try:
        # Initialize OpenAI client with user's API key
        client = OpenAI(api_key=request.api_key)
        
        # Create the prompt based on diet type
        prompt = f"""Create a simple, delicious {request.diet_type} dinner recipe. 
        
Please provide:
1. Recipe name
2. Prep time
3. List of ingredients (with quantities)
4. Step-by-step cooking instructions
5. Nutritional highlights

Keep it simple, healthy, and suitable for one person. Make it appetizing and easy to follow."""

        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional chef specializing in healthy, simple recipes. You provide clear, concise recipes that are easy to follow."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=800
        )
        
        recipe = response.choices[0].message.content
        
        return {
            "success": True,
            "recipe": recipe,
            "diet_type": request.diet_type
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recipe: {str(e)}")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

