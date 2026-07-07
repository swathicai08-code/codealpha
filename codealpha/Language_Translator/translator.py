from deep_translator import GoogleTranslator

def translate_text(text, src, dest):
    try:
        return GoogleTranslator(source=src, target=dest).translate(text)
    except Exception as e:
        return str(e)