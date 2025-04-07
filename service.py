import requests
import tempfile
import os
import simpleaudio


class Service:
    def __init__(self):
        self.url = "http://127.0.0.1:8000"

    def set_parameter(self, name, value):
        response = requests.patch(
            f"{self.url}/set_parameter",
            json={"name": name, "value": value}
        )
        response.raise_for_status()

    def send_text(self, text, output_file):
        response = requests.post(
            f"{self.url}/to_speech",
            json={"text": text, "output_file": output_file}
        )
        with open(output_file, "wb") as f:
            f.write(response.content)
        print(f"Zapisano do {output_file}")

    def send_and_play(self, text):
        response = requests.post(
            f"{self.url}/to_speech",
            json={"text": text}
        )
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(response.content)
            tmp.flush()

            print("Odtwarzanie...")
            wave_obj = simpleaudio.WaveObject.from_wave_file(tmp.name)
            play_obj = wave_obj.play()
            play_obj.wait_done()

            os.unlink(tmp.name)
