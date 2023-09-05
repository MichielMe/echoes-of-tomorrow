from story_generation.story_gen import generate_story_chunk
from databaseM.db_handler import fetch_all_story_chunks_and_save_to_txt, get_story_chunk_count
from mastodon_api.mastodon_poster import post_to_mastodon

def main():
    # Get the current count of story chunks
    count = get_story_chunk_count()
    
    # Generate a new story chunk
    new_chunk = generate_story_chunk()
    
    # Increment the count for the new chunk
    count += 1

    # Add the dynamic "Part XX:" prefix
    new_chunk_with_prefix = f"Part {count:02d}: {new_chunk}"

    fetch_all_story_chunks_and_save_to_txt()
    
    # Post the new story chunk with prefix to Mastodon
    post_to_mastodon(new_chunk_with_prefix)
    
    print(new_chunk_with_prefix)

if __name__ == "__main__":
    main()


