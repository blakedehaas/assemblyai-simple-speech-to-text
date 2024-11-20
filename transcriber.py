import assemblyai as aai
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
# Check if the API key is set
if not ASSEMBLYAI_API_KEY:
    raise ValueError("API key not found. Please set ASSEMBLYAI_API_KEY in your .env file.")
# Set the API key
aai.settings.api_key = ASSEMBLYAI_API_KEY
# Get the input file name from the user or default
input_file = input("Enter the audio file name (with extension): ").strip()
if not os.path.exists(input_file):
    raise FileNotFoundError(f"The file '{input_file}' does not exist in the current directory.")
# Extract the base name (without extension) for the output file
output_file = f"{os.path.splitext(input_file)[0]}.txt"
# Initialize the transcriber and transcribe the audio file
try:
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(input_file)
    # Save the transcript to a text file
    with open(output_file, "w") as txt_file:
        txt_file.write(transcript.text)
    print(f"Transcription complete. Saved as '{output_file}'")
except Exception as e:
    print(f"An error occurred: {e}")