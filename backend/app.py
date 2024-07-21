from flask import Flask, request, jsonify
from flask_cors import CORS
from audio_to_text import record_audio, convert_audio_to_text

app = Flask(__name__)
CORS(app)

@app.route('/record', methods=['POST'])
def record_audio_api():
  try:
    record_seconds = int(request.json.get('record_seconds', 3))
    audio_path = "audio_files/sample_audio.wav"

    record_audio(audio_path, record_seconds)
    text = convert_audio_to_text(audio_path)

    return jsonify({"Transcription": text}), 200
  
  except Exception as e:
    print(f"Error: {e}")
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
  app.run(debug=True)