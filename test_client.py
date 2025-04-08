import pytest
from speech import SpeechController


@pytest.fixture
def controller():
    return SpeechController()


def test_set_rate(controller):
    controller.set_rate("140")


def test_set_volume(controller):
    controller.set_volume("0.7")


def test_speak_to_file(controller, tmp_path):
    test_file = tmp_path / "test_output.wav"
    controller.speak_to_file("TEST", str(test_file))
    assert test_file.exists()
