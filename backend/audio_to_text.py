import speech_recognition as sr
import pyaudio
import wave

def record_audio(filename, record_seconds=3, sample_rate=16000, chunk_size=1024):
  # Setup
  format = pyaudio.paInt16
  channels = 1

  audio = pyaudio.PyAudio()

  # Start Recording
  stream = audio.open(format=format, channels=channels,
                      rate=sample_rate, input=True,
                      frames_per_buffer=chunk_size)

  print("Recording...")

  frames = []

  for _ in range(0, int(sample_rate / chunk_size * record_seconds)):
    data = stream.read(chunk_size)
    frames.append(data)

  print("Finished recording.")

  # Stop Recoding
  stream.stop_stream()
  stream.close()
  audio.terminate()

  # Save the recorded data as a WAV file
  with wave.open(filename, 'wb') as wf:
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(format))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))

def convert_audio_to_text(audio_path):
  recognizer = sr.Recognizer()

  with sr.AudioFile(audio_path) as source:
    recognizer.adjust_for_ambient_noise(source)
    audio_data = recognizer.record(source)

    try:
      text = recognizer.recognize_google(audio_data, language="ja-jp")
      print("Transcription: " + text)
      return text
    except sr.UnknownValueError:
      print("Google speech Recognition could no understand the audio")
    except sr.RequestError as e:
      print(f"Could not request results from Google Speech Recognition service; {e}")


if __name__ == "__main__":
  audio_path = "audio_files/sample_audio.wa"
  record_seconds = 3

  record_audio(audio_path, record_seconds)
  
  convert_audio_to_text(audio_path)