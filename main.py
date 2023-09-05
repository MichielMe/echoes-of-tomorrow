from story_generation.story_gen import generate_story_chunk
from databaseM.db_handler import fetch_all_story_chunks_and_save_to_txt
from mastodon_api.mastodon_poster import post_to_mastodon

def main():
    # Generate a new story chunk
    new_chunk = generate_story_chunk()
    fetch_all_story_chunks_and_save_to_txt()
    # Post the new story chunk to Mastodon
    post_to_mastodon(new_chunk)
    print(new_chunk)

if __name__ == "__main__":
    main()


