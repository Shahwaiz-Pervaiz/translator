from translate import Translator
with open("read.txt","r") as file:
    text=file.read()
    # lang =["ur","fr","es","hi","fr","ar"]
    # for i in lang:
    translator = Translator(to_lang="ur")
    translation = translator.translate(text)
with open("write.txt","w",encoding="utf-8") as file:
     file.write(translation)

