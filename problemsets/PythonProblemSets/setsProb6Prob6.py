#! usr/bin/env

StemCellGenes =[]
with open("alpaca_stemcellproliferation_genes.tsv", "r") as stemcell:
	for rawline in stemcell:
		line = rawline.rstrip()
		StemCellGenes = line.split()[0]

print(len(StemCellGenes))

AllGenes = []
with open("alpaca_all_genes.tsv", "r") as allgene:
	for rawline in allgene:
		line = rawline.rstrip()
		AllGenes = line.split()[0]
print(len(AllGenes))

PigmentGenes = []
with open("alpaca_pigmentation_genes.tsv", "r") as pigment:
		for rawline in pigment:
 			line = rawline.rstrip()
		 	PigmentGenes = line.split()[0]
print(len(PigmentGenes))
