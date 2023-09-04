from story_generation.story_gen import generate_story_chunk
from databaseM.db_handler import save_new_chunk, get_last_story_chunk
from mastodon_api.mastodon_poster import post_to_mastodon

if __name__ == "__main__":
    # Generate the first story chunk
    first_chunk = generate_story_chunk()
    print("First Chunk:")
    print(first_chunk)

    # Post the first chunk to Mastodon
    post_to_mastodon(first_chunk)

    # Generate and post more story chunks
    for i in range(2, 6):  # Generate chunks 2 to 5
        next_chunk = generate_story_chunk()
        print(f"\nChunk {i}:")
        print(next_chunk)

        # Post the next chunk to Mastodon
        post_to_mastodon(next_chunk)