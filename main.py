import argparse
from speech import SpeechController

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text", nargs="?", help="Tekst do wypowiedzenia")
    parser.add_argument("-o", "--output", help="Zapisz jako plik")
    parser.add_argument("-s", "--source", help="Plik tekstowy jako źródło")
    parser.add_argument("-r", "--rate", help="Szybkość")
    parser.add_argument("-v", "--volume", help="Głośność")

    args = parser.parse_args()
    ctrl = SpeechController()

    if args.rate:
        ctrl.set_rate(args.rate)
    if args.volume:
        ctrl.set_volume(args.volume)

    if args.source and args.output:
        with open(args.source, "r", encoding="utf-8") as f:
            text = f.read()
        ctrl.speak_to_file(text, args.output)
    elif args.text and args.output:
        ctrl.speak_to_file(args.text, args.output)
    elif args.text:
        ctrl.speak_and_play(args.text)
    else:
        print("Podaj tekst")

if __name__ == "__main__":
    main()
