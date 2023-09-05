import os
from datetime import datetime
from supabase_py import create_client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

def save_new_chunk(story_chunk):
    table = "story_chunks"
    new_entry = {
        'chunks': story_chunk,
        'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    response = supabase.table(table).insert(new_entry).execute()
    if response.get('error'):
        print(f"Insert Error: {response['error']}")
        
def get_last_story_chunk():
    table = "story_chunks"
    response = supabase.table(table).select('*').order('created_at').limit(1).execute()
    data = response.get('data')
    if not data:
        print("Fetch Error: Could not retrieve data.")
        return None
    return data[0]['chunks']

def fetch_all_story_chunks_and_save_to_txt():
    # Fetch all story chunks from Supabase
    table = "story_chunks"
    response = supabase.table(table).select('*').order('created_at').execute()
    
    # Check if data is received
    if response.get('data') is None:
        print("Fetch Error: Could not retrieve data.")
        return
    
    # Sort the data by timestamp
    sorted_data = sorted(response['data'], key=lambda x: x['created_at'])
    
    # Write the sorted chunks to a .txt file
    with open("../echoes-of-tomorrow/story.txt", "w") as f:
        for chunk in sorted_data:
            f.write(chunk['chunks'])
            f.write("\n---\n")  # A separator between each story chunk
    
    print("Story saved to story.txt")
