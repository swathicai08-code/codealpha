from deep_translator import GoogleTranslator

def translate_text(text, src, dest):
    try:
        translated = GoogleTranslator(
            source=src,
            target=dest
        ).translate(text)

        return translated

    except Exception as e:
        return str(e)