from service import Service

class SpeechController:
    def __init__(self):
        self.api = Service()

    def set_rate(self, rate):
        self.api.set_parameter("rate", rate)

    def set_volume(self, volume):
        self.api.set_parameter("volume", volume)

    def speak_to_file(self, text, filename):
        self.api.send_text(text, filename)

    def speak_and_play(self, text):
        self.api.send_and_play(text)
