DNASeq = "ACGT"
input = ("Enter a DNA sequence: ")
DNASeq = DNASeq.upper()
DNASeq = DNASeq.replace(" ","")
print("Sequence:" , DNASeq)
SeqLength = float(len(DNASeq))

print("Sequence Length:" , SeqLength)
BaseList = "ACGT"
for Base in Baselists:
  Percent = 100 * DNASeq.count(Base) / SeqLength
  print("%s: %4.1f" % (Base,Percent))
