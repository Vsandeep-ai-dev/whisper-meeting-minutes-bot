from transcriber import transcribe_audio
from summarizer import summarize_text
from action_item_extractor import extract_action_items

def main():
    print("🤖 Whisper Meeting Minutes Bot")

    audio_path = input("Enter path to the meeting audio file (e.g. audio/sample_meeting.mp3): ")
    print("\n🔊 Transcribing...")
    transcript = transcribe_audio(audio_path)
    print("\n📝 Summary:")
    print(summarize_text(transcript))
    print("\n✅ Action Items:")
    print(extract_action_items(transcript))

if __name__ == "__main__":
    main()
