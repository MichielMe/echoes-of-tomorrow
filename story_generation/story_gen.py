import openai
import os
from dotenv import load_dotenv
from databaseM.db_handler import save_new_chunk, get_last_story_chunk


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initial story setup
initial_setup = """The year is 2035. AI technology, under the control of global corporations, 
has permeated every facet of life. Yet beneath this veneer of progress, whispers circulate about 
government cover-ups of alien encounters and hidden advanced technologies. Dr. Emily Carter, a 
rising star in AI ethics, stumbles upon encrypted files that hint at the existence of Project 
Echo, an off-the-books initiative purported to hold universe-altering secrets. Meanwhile, Leo, a 
blue-collar worker disillusioned by the widening gap between social classes, finds an alien artifact 
that reacts to his touch. Their paths cross with Agent Sarah Dawson, a government operative with her 
own dark past, tasked with keeping Project Echo a secret. As they delve deeper, they realize that 
the truth is far more complex and dangerous than they ever imagined."""

def generate_story_chunk():
    # Retrieve the last saved chunk
    last_chunk = get_last_story_chunk()
    
    messages = [
        {"role": "system", "content": "You are a creative writer. Generate a continuation of a sci-fi story."},
        {"role": "assistant", "content": f"Initial Story Setup: {initial_setup}"}
    ]
    
    # Add last story chunk if available
    if last_chunk:
        messages.append({"role": "assistant", "content": f"Last Story Chunk: {last_chunk}. The story continues..."})
    
    # Add the instruction for generating the next story chunk
    messages.append({"role": "user", "content": "Write the follow up text chunk. Continue the story. End the text chunk with two relevant hashtags. The text can absolutely not have more then 500 characters. Limit it to 500 characters, that's super important!"})
    
    # Make the API call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages,
        temperature=0.9
    )
    
    # Extract the generated story chunk
    new_chunk = response['choices'][0]['message']['content']
    
    # Save the new chunk to the database
    save_new_chunk(new_chunk)
    
    return new_chunk

