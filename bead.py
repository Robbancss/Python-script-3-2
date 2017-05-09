import os

class Ford:
    "Translater class."
    def __init__(self, vocab):
        self.Vocab = vocab
    def fordit(self, fromFile, toFile):
        if os.path.isfile(fromFile):
            with open(fromFile, mode='r') as fromTranslate:
                with open(toFile,mode='w') as toTranslate:
                    for line in fromTranslate:
                        for key, element in self.Vocab.items():
                            line = line.replace(key, element)
                        toTranslate.write(line)
        else:
            print("Nincs input file!")

    def visszafordit(self, fromFile, toFile):
        if os.path.isfile(fromFile):
            with open(fromFile, mode='r') as fromTranslate:
                with open(toFile, mode='w') as toTranslate:
                    for line in fromTranslate:
                        for key, element in self.Vocab.items():
                            line = line.replace(element, key)
                        toTranslate.write(line)
        else:
            print("Nincs input file!")