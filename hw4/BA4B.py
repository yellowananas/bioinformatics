table = {}
table['F'] = ['UUU', 'UUC']
table['L'] = ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG']
table['I'] = ['AUU', 'AUA', 'AUC']
table['V'] = ['GUU', 'GUA', 'GUC', 'GUG']
table['S'] = ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC']
table['P'] = ['CCU', 'CCC', 'CCA', 'CCG']
table['T'] = ['ACU', 'ACC', 'ACA', 'ACG']
table['A'] = ['GCU', 'GCC', 'GCA', 'GCG']
table['Y'] = ['UAU', 'UAC']
table['H'] = ['CAU', 'CAC']
table['Q'] = ['CAA', 'CAG']
table['N'] = ['AAU', 'AAC']
table['K'] = ['AAA', 'AAG']
table['D'] = ['GAU', 'GAC']
table['E'] = ['GAA', 'GAG']
table['C'] = ['UGU', 'UGC']
table['W'] = ['UGG']
table['R'] = ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']
table['G'] = ['GGU', 'GGC', 'GGA', 'GGG']
table['M'] = ['AUG']

def toRNA(dna):
	res = ''
	for letter in dna:
		if letter == 'T':
			letter = 'U'
		res = res + letter
	return res

def toDNA(rna):
	res = ''
	for letter in rna:
		if letter == 'U':
			letter = 'T'
		res = res + letter
	return res

rna = toRNA('GGATTCGCCCGATGATCGACGGTTTAAGGTTACATGGAATCCCACATCGTTTGTGCGCTCGGTTCCTGGACGCTACAGATCTCTAGTAATGAATTCCCGAAGATACTACGGAGCTCCCTTCATGTGAAGGACGCAGGTAGGTACGGCATAGTTTGCTACATATACTGTCCTAGTACGAAAGCCCTGACGCCTAGCTCATCTGTTGAGCAGCGACTACGAGCCCTGCTGTAACATCTTAGTCTGCCGACTATCAGCGGCCCCGCTCGTAATGTATCTTATTACCATGTTCGTTTAAGCTAATTGGCGGGTCGACGCGCCGGACGCATAGGTCAGTCAAACATACATTCACATCGACACAGACTCACGTATTTAACTAGTGATACACTCTGTCCAGTCAAGGGCGACCAAGAATGCAATCGAGGTACCGGTCACTCTTATTTCTGCGGGCACAAGAAAAACACACGTGCGTCGGGCTCTTCGATTTGCTTGCCTTGTTACCCGAGTGCGACGATTAACAGAAGCGTAGGGAACTACAGCTATTTCGCAGTTTTTCGTGGAATGTATGTCCCAGAGGCAAGAATGGATCCCACTTCACAGCTATAGTCGTCACGAGCTTGATCAACTGCTAATCATATTGGCGCATGCCTGATTTTTCTTGTGGTCAGGGCTATGGCCTCATCACCTAAAATTGTTACGGAGGTTTCTGGACGGCACCTTTCGGTGCGCATTGCTTTCTCACTTCGTTAACCGATACTTTTCAGTGCATTCCTGGTATGGCGACATGAGGTCAGGGCATTAGGCTAAAGGATTTGTTTATTGCACTTTTGGCACCTGCTCACTTGTTATACCGGGCGCGGCAGGACCCGTCCCACCTCATAAAGTCCTTGAGTCCAAATAACAGAGGAATATCAGTTATTCGCTCCTGGGGTTCTAACTTTTCGTGGTCCCGCATATGATATGTTACCCGGGGGTTGTGCCGTCACACTCGGGGCAAGAGGGATTACATTTGTACAACTTCTAGACGACAAGGCGATAACGCTCCGCGACTGGGTCGGTATGGCCCTTCCCTGTTCTTCCCTGAGCAACCGTCGACCGCGAGCGTACTGTGCCTCCCGACTACGCACTTCGCGATAGGCTTACCCGTCGCTGCTGGTAAAGCAGTCCAATCGTTGCCGCGTAGGGTATTTAACTTGGCAGGTCTGTCCTATGTGAAAACGAGAGCTCGTTCTGAGTTCGTATTAACACATCTTCTCTTGAATAGCGTGGGTAACCGTACTTCGCTGTGGAGTAGGATTGCTAGGACTGCCTATCCTCATGCCTTGTTATTACTTACACGAGAGAAATCCATACCATAACTCTTGTGCCGATCTCATGCTCGCTTAATCAGGGATTCAATCTAGCGAAAAGGATTAGTATGATAAAACGCACTACAGATGATTCGATTGCCGTTGCGCTAGATCAACTCTATTGGCGAATTCGTATCGTTAGCCCCTAGCAGCCGACCATAATTGGTGTATCCAGGCCCTGGTTAGCTCGTAAGCGTTAATCGGTTAGGAACTACTTGATCTTAATTATATGGTCCTAATGTGGAGGTCAACCGCACCAGACCACCTGGAGCCTGTGCGTCGTTAGCTTGGCCTGAGGGAAGGAAAGGAATCTGTCCATGACGCATATTCCTGTACTGAGCTCGCTCGCAATAACCGAGGAGTCTGTGAAGCACAGAACTGATAAGATTGTCTACGTATCGGCCACGGCCCAGAGCGATATACTTGATTTCTCGCTGGCGTCTCTGAACCGAACAACAGGGTTGCGGTGACTAACGACTGTCACCGATCATAACGTCCCTGTGTGGATTGCATATGCCTGGGGCTCTCCCTCTGAACCTCTTGGGGATCTTGTACGAGAGAAACTCTGAGTTGTAAGTTGACGCTTGTCTTGCCTTTACTTATCCGGTACGGACAGTCAACCCATGTAGCCTAGGACTTCGGGGGCACTCTGAAAGGGTTGTACATTGATGCGTGACCTAGCCCGCCCGGGGTTACCTTTGGAGAGGTTGACTCCGGGTCCGAAGGGAGATAACGAGGCGTGTGGCTGCAGAGTCTTTTTAGGTTATATCTCCTCAAGTACGACGACTCGAGGGTCTGGATACACCGGGTGCTGAGGCCCCAAACTACCGGTTCAACGAAGCTCTGGCCCACTTGTCCAGGAATGGTTAATCACAGCACAATGAATCGACTCATACGGAATGCGGATTATCTAGCGTAAACACTAAGCCAGGAACGTCACTATGTATAACAGATGTCTAAAATCCCGTATTGCGTAACGGATTATAGGCGACAACTCTTGATTGTGTACCATCGGGCAAAGTGAGAGTCACCCAAATAGTGTTAAATCTGTTGTCTTTGTGACATGCATTCAACGAACCGGACAGCGAACGCCGTCCTTCATACAACACCGAACATTTACCTGGGAACACTGACGCACCTCCCACGATCTGCATTTCTTTGTGTTTACTACTTAGAAGGTACTGAATCGCATTCAGACAGTCAGCGTGGGCAAACCGACATCTGCGCCGCTATGACGGCAGACTGTGTGCCGCTGACAGTTTTATGACAGGGCTATGCGCTGAGCCGATTTCTATCCAACCATTCTATACCCTACTTTCAGGTCCGACTAGTGGTTTCGGGCACACTGCCTACAGGATCTACGTGAATTACTTTGAAAGAGTTGCCCGGCGTGATCTATGGTGAGAAAATGCTCGAATATCAGCATCCAAACTCGTACCCGCTGGTATCTGTGGCGCAAATAGACTGCTCCAGACTGCTTCTTCCCGCAAATAGCGAGTGTAGCGCGAATCCGAACATAAAGGCAAGACGAGTGCTGCGCTCCATTGACTGGGCCTCTCCTACGAGTTTGCCCTCATTTCGTGAGCTTATTCACAGAGCGTACCCTGAGACAGCGAGTATTGTGCTGCTATGCATCGAACACGATCCGCTCCAGCTTCATCAATTCCTAATTACGGTTTGATCACGTACTCTAGCCGGCGGACACCAGTCCCTCATAACAGAGCGGATATTGCATGGCCATCAAGTACCCGCGTACGTCCAACTAGACTACGGCTGGCGCATAAGTTATGCGTAAACTCCCATATCGTAACTGCTGTGGCGCTTAAGTCAGGGGCACGTGCTTCCTTCGAAGACTGCAACGGGTGACCTGGACTGGCGTGTCTGTTGGACTCAGACTAGGATCTTAGACGCGCATTTAATTACCTCGGTCTTCAGTGCTCGGGGTCGCCCAGAGCTGGTCACACCACGGTGGACTCTCTGTCACATTTTAGCTACTTGATAGACAACATAGCGCCTGTGTACTAACTGTGCCATAAGGGGGAGACGCTCCGATCCAAGTCCAAAGGGTCGGAGCACTCTCTAGGCGCGAGCATCGGGTCAAGCGTATCGTTCCTAGGTGACCCGGTCGACGTTCGCCTCTCCCCGGACACTTCGTACGGCCACTCCGCTGCGAAGATGGCGAGCCAGGCTCTGTATCCAAACCCCCAGCTTATGGCTGGTGTTCGTAGAGACTGATCGATGACATCTGGCCTAGAAATTATACAGCTAAATGCTTGTGTGAACAAGCAGTGGTCACGGTCGGAACACAAGAGAAATCAGCCCGTAAAGAACTCTTAACCAAACCCCCGAGCCTTTATCTATCGTAAAGGGCAGGGCGAGCTGTTGCTGCAGGTAGCAACCCGTATGAGAGATTGTTTTCAGGTGGGTCCGTTGTAGTCTCCATTCGGGTGACATTCGTATCTACGAGTGAGGAGACGACAGAAAGTGTCACGGCGGTATGGCTGCAGCCGGATTTGTAGAGTGCATGTCCCAAAGACAGCATTGTCGATCGACTTACAACCATCCACTTGGACATGAGTTGCAGGAGAACAGAAATCGATTGTTATCTGAGCGCTCTGACAGCCCAGGGGACGTATTAATAGGCGGTAAGAGTGCCTATGAATCGTTGGTACACGGCCATCTCACATCAGTGATCACTCGGTTCAGTGTAGGCCCGTGAAGACCGGCCAGGGCAAGCGAAACCCTTGTTAGCGGAATAGCCAGTGACTCACTCTCAGCTGGCGCTGGCTCATACACTCGACGAACTGACGCTGGGACATACACTCGACAAATCGCGCATTCGTGGAGTGTATGAGTCAGCGGCAAAGGTTTAGTTCTCGACTGGCGTTGACTCATACATTCCACAAACCATAGTACTATCAAAGTCGTCGCCTTAATGGAGTTTGTAACGTCTTTACGGGGTAATCTGACATATTAAGGGGTACTGTCTGGCGAAGGCTTGGCAAAAGCATGACTCCCTTTATTTCCAATTCGATAATCCGCCCCCGCTATAGTCGGTATATATATTCGGGGTTAAGATCACGAGTGAGACCGGCCCCGATCATTTTTCCAGTTGGATCAGGAGCTCATGTATGGCGTCCGAGCTTTCTCCAGAGCTCTAGAGAAGCGATCACCACGGTCCAGGATTTCCACACTACTTTGCAGAGTATTATTCGCACAGCAATCGGCTCGGTCCTCACTCTTCACGGTTTCTACTCGAGGCGTTCCCTGGGAACCACATCACGGGAACAGTAGTCTTTAACTCTGCGTTCAGGAGTTGTATTGGCGTGCACCTCTCACCTGCGCGTGCAGTCAATCACCTTGAGTAAGTGGATGGGTTTCTTTCCAATGTGTCCCCGTACATGGGAATCCGAAGCTAAATAACACCACCGCAGCGGTTCGTGGAATGTATGAGCCAAAGACAGCTACATACGACACAGTGTCAAGTCTAACCCAACTGACGTTATGCGAACCGGGAAATCCCCCATGGTGACTCTGTTTTCCGTTCGTGGACAGCTTTCGAGAGTGTAAGCCGTCGTTTCGGTCTACGAGGGGTCAGCGTCCTCATACAATTAGGAATCATTTCTATCTTATTAACTCCTCAGTTAGCAATCAAATCACCTCTTCAAGTTATCATACTAGCAAAGGTCAAGGGACACTTCAGATTATTCTGATAGATCGCACTATAAGACTAATGTTGGCTCTAGTTTATCTATTCTGATCCAACAGTAATAATACCGTAGATTATATTAAAAATCACGTTAATGTTAAGTAACACATTAACGTGTATCCTGGCGCCGCATCTCTCCTTGCTGCTTGTAGAAACAAAAATCGTGTCCATAGGGAATCGAGTTATTTATGCTACGCGCGAGTCTCAGTCTGAAAGGGGGGTTTAGCTTTTTGGGTCCTTCGTAGAGTGTATGAGTCAGCGGCAGACTCATGTCTAGGATCCTTATTAAACAATAACGCGTGCAGGTCACCGCGTAGTCTGTCGCCGCACCTGAAGCTCTGAAGTTTTGCGAGCGGGTCGGCAGGATTGCACGGCGGAACGGAGAGTCGTGGTCGCATTGGAATGCAAATTACACTATGATGATGCGGAGAACTAAGGGGACGGACTCACCGGGCCCCATCATGATTTAGTCCTGATATTGTGATACCCCGCTATCTTCGTCCGCTGTTAGCACGCTCATCACAGGTGTCAACGGCGCCCAGTAGTGCTCGCAGAGAGTAAGTGTGTTTGTGACGGCGCTTGCTCCCGCGCATACACTATATGCCGCGTTGATGCTTTCGAACTCCATTTTTGCCGCTGAGACATGCATTCAACAAACTGAGTTAACGCCGGTGGCAAGGCTTAGATGGGTCTACATTACAGTGAAAGAAGAATCGGGCCGATACTTAACGGGGGGACAGTAGCGGGCTTGTCAAACCTGAAGGATTCTCACTGATGGCATTACAAAACACATGCTCGCCACGTACCGAGTCTTAAGCGTCATCCGTTAAGAGGAAATTGTGGTTCAGCAATAAGAGATAGGGACGGCTAGTTCGCCAATATTCCAGGAGCCAGGGGTTACGTCATTCCGTTGGTTCAGCTGAGGGTACTCCTAGTTTAGCCATACCCTACGCCCGGAACTTGTCTTTCGTCGAGTGTATGAGTCAGCGGCAATGCTGTGACGCTTACCGATACTTTTCTTGGCCGTGCGTTAGATAATGCGTTTTAATTATTGTCCCAGGCACATCGGAGGGTTTGCGATTAGATCGCAAATACTGGAGTCGTTGCGGTTCGCATCATACTAGCCTGTCAAAGAAATGCTACTGTGCATTAGCTGGATCTTGCGGGGGGGTTCTTGATGTATGACAGTATGGATCGTCTAAGATCAGTCGTGTGCCCCTCCAGCATTACCGGACAAGCTCATGACTGCGGGAGGAAACATATTCTGTCAATGATATCCCGTCGGGCAAAAGAGGAGCTGTACAAATCCCTGATCAGGATTAGCACCCGCCCCATCTTTGCCACGTTTCGACCGGGTCAAACGGTAAAGAGGTAAGACGACGACTATGACGCTGGCATTGATACCTAAAGTACCGCCTCCGTCTTATTGTCGCTGTGACATGCACTCTACGAAAAGCCCTATAATACTACACTTCGTGGACGGACAATGGAGCAGCGCACCATTGCTAAGACAGCCTTACATAGTATCCTTTAGAATGCGCCAACTATATCACTATTGGGAACTGACCTGTACTGCTTATTACACGAACACTACTGATTGTTTCATTCTGTCGCTGTGACATGCATTCAACAAATGGGTTGTATGGTTAATCTGAGCTACTCATACTATACGCTACGACTGCGCAGTATACTGGATAGGTAGTTAACACATTCAGCATCATCCAGGTTTCGTGGACCGTGTTAAATATGTAATGCGGAATCGAATTGTGTATTGTTACCGGGTCTATGTTTCCTCGGAATCGCTAGCGTACAATGAAGAAAGGGTCTATTCATGTTTGAGCTACCGATGCAGGGTTGCATAGTTATGAGAGTGAAGATATTTGTCTACGGTTATGACGTTGGGGACGCAAATCAAGAGCACGAAGAAGCATTAGCCTCTTGTAGGTTGTCAGTCCAAGTATATGGAACGACTACTAAGCAAACTCGACGAACCTAATACAGACGGCTCGTCCGTGGCGCCACAACGGTCTTTCGATGGCATAAGTAATGGACTCATCAAGCCGTAAGCGTCTGTGCCAGTTCGTCGAATGTATGTCTCAAAGACAGCGACTCCCGCGACCTCCTGTCACCTTCTGGCGCGACACCTTGAATCGGCTAGCGAATAGTACGACGCTTACCTCTTACAATACGGTGGACCTGCCGTCAATACTTCGACATTGGTTTACCCTGTGATCCCTAAAATGGGTGCCAAAGAATCCCGTTGTCCCGAGGTCTCGTATTTGTCGCCACCGTCCGATATATTTTTGAACCCATTACTTAAGCTGTTGGGAGAGGTCGTAATGCCTATCTCGTAACCTTAGTCCACCAATCTGCCACCCGCCTGGAACCTTGCCTGACAAAGGCCTGTTTGATTTGAAACATACGTTTTTAGGCCCCGATTCGCTTAGTTCAGCTCTCGCACCCCGGACACCCACCAGTTCGTACAGGGGATCAGAGAAACTTTTACTAGCGCAATCGAGCATATCTGGACGAGGAGTCGAAACTGATCGATAACACCTTCGGCCGTGTACTTCCACTATTGTAGGGGATGAACGAGGTCCTCCTACTCCTGAAATTCGCCGGTTCTGGAATATCGGACACGCTTCGCACGTTCCCATAGAAGGTGACCCGGAGGCCCCCGGAGTTCTCGTGAACAACCACAGTGTTAGGAATGTCCGCCACGCCCAACAGTTGTTGTTAAACGTCCCACTATAGATACCCACATCAGGGTGGTGGTTATTTAAATCTCGACTCAGAGATGGGAAACACAGCGCACCGGAGTAGGCCTAGTAAACCCAGATAAGTAGGGCACACAACATACAAGATAGCATTGTCCCGACTGATCCTGACCGCTACGAGAAATCAAGCCCTCACCTCCTAGGCAGTACGTAATACGAATTCTGGAATGGCACATCTAGTCAAGCAATTCCCTTATGACATGGATCTCCTATGCAGAATCTGGAATACGAAGAAAGTGTTATCATCGGGGGGGATGAACCAATATTAAGTGGTGGGCTTGTCCGGATACCGTCATGTGGGCCGGACCTAGGGCCGAGCTAAGTGCCGCCTACAGTTGACACGTTATAAGTGCGTTGCCCACTTTTTCTCTGGTCGGGGAGATGGTGTCTGAAACATTTGGAAGAATCGTCTGCTGTTTAAGATTTCGTAGAGTGTATGTCCCAGAGGCAATTACATTGGCCGATGCCTGGTTATAATTGACCTCAACCTCAAGTCAACAAAACCTGAGTCCTTATGTGAGCATATGGTTCCATAACTTACCCAGCAATCGTGTTCAGTCGGCGCCTTACGTTCATGTTTTTTGTGGAGTGCATGTCTCAAAGGCAGTAAATACGTGCCTTTCCAATCGGCCGCCCTCGTGTATAGGCGTAGATGAGCTACGTATTGGAAACACGTCACATGCAGAATTGGGAATCAACCTTCAAAGCCGGCAGCAAGATCAAACTTTGTGGAATGTATGAGCCAACGACAGTATCCGCCATGGTTTAAGACAGATAAATTCCCCCCTACCGGCCCGCTGGACGTTATGTCAAAAGGGCTCCACATTCCAGTCAAGATCTCATCTATTGGTCACTCGAGGATCGATTCATTTATGCGCCAAGGCCAAGGTTTCCATCCAGCTTCTCAGCCAAGGCACCATGGCGATCTCCACGCCTACTGTAGAGACCGCAGGAGAGTCTAGTTACTCTCTGTCGTTGTGACATGCACTCCACAAACGATCTACGGATCCAGTTGACTGTGGATATACTCAGAGTGCATCCTTAAGGCACTGTACTGATACGTTGGCGAAGCTTTTCGGGCTGCAATCTGGCACAGCAGGTCTACCGTCCGCGGTGCCTTTAACTCCCTAGAGCCA')
protein = 'FVECMSQRQ'

def complement(string):
	res = []
	comp_table = {'A': 'U', 'C': 'G', 'U': 'A', 'G': 'C'}
	string = list(string)
	for el in string:
		res.append(comp_table[el])
	res.reverse()
	res = "".join(res)
	return res



def toProtein(rna, table):
	res = ''
	for i in range(0, len(rna) - 2, 3):
		for k, v in table.items():
		    if rna[i:i+3] in v:
		        res = res + k
	return res

def peptide(rna, protein, table):
	res = []
	prot_len = len(protein) * 3
	for i in range(0, len(rna) - prot_len - 1):
		prot = toProtein(rna[i:i+prot_len], table)
		comp_prot = toProtein(complement(rna[i:i+prot_len]), table)
		if (prot == protein) | (comp_prot == protein):
			res.append(toDNA(rna[i:i+prot_len]))
	res = '\n'.join(res)
	return res

print peptide(rna, protein, table)