from deep_translator import GoogleTranslator

def translate_text(text, src, dest):
    translated = GoogleTranslator(
        source=src,
        target=dest
    ).translate(text)

    return translated