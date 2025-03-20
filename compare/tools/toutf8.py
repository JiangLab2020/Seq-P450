import codecs

import chardet


def convert_to_utf8(input_file, output_file):
    with open(input_file, "rb") as f:
        raw_content = f.read()
        detected_encoding = chardet.detect(raw_content)["encoding"]

    with codecs.open(
        input_file, "r", encoding=detected_encoding, errors="replace"
    ) as f:
        content = f.read()
        content = content.replace("*", "")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)

    return output_file
