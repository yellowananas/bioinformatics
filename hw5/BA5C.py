import mlpy

table = {}
table['A'] = 0
table['C'] = 1
table['G'] = 2
table['T'] = 3

x = 'GGAACTAGGTGTCCGCATAAAATAGCCCTCATGAGGTAGACTGCAGGGAGGTAAATGTTACCACTGGACGTCCATTTACTGCTTGCGGTAAGTCAGCTGTTTGTGCGTCTTGTCAAAGCACCCGTTCGGTTGTGGAGTGGTTGTGAACAATTAACGTTATGTAAAGATCGTGAGGCAGGGGGTTGCACACGGCTGGCGGTATGGGTCTCCGCGTCACAGTATGTGGCGTATTTCTTAGGGTGTGCACTGCGCCCCGTGAGATGGACTGATTCCTCCAGGTAAACACCCATATAGGTTGTTCTGTCGGGAAGAACCCGCGTTGTGGCTAGGTTCGGATTCGCCGCTACAAGCTACCAACGGAAGCAAGACCGGAAACTGCCCAAAGCGCGGACTTCAATATAAGGTTGGTCACCAGGTGAGCATAGACGGGCCAGCCGTTCCCGCCATTATTGGTGTATCGAATCTCATGTATTGATCCATTTGCGCCTTCCAGGTACGACCGCCTAGTACCAATCTGCAGCGGCCCCCGACACGCCCAAACCATTGGCGGAATAACCGAGACACTTGACAATTTACAGGACGGTGGATTACGGCATCATATCGTGGAACGCAGGCTATACTCCTAACCGCGAGAAATCATTTAATTGGTTACGGATACAACAAATTCGGCTGAGTCCGTTGCCTTCCCAAAGCGGGACTATCCACCTTGTGCTAAATGGAAAACCTACTCATTGGTACGCACACGAGCCTTTGCATAATCGCATTTGGATCTCTGCTGCAGGACCCCGTGACTTTTCGTAGGATCCTATAATGTTGGGATAAACTC'
y = 'TCAAGCCCGTGTATTTGGGGCCCGGTCCCTCCCAAATCAGGAGACGGTCTTGAACGACAGGCTGGGTCCCGGCAGGTATGACGTGTTGATCTATTTATTATCGTACCAGACGTGCCTGTATCCCACACAACGGTATGAGTGTAGCCGGCGTGGCTCTTAAGTGAGCTTGTTGCTGCTCCTTTCGCGACTCGGTGGTCTTAGTCCTACTTATCATGTAGGAGGTCCTGAGATGGATTTCCAGCTGCCGGCGATCCTTGAAGGGGCGGCCGAGTGCTAGGGGAGGTCTGACGATTAATGCGGGGTGAAGGCTGATGAAGTTGTCCAGGACTGTCGTCCTTGCAATCCAGACCGGGAGTGGGCGAGGGCGAAGTCTGGCCTCCCCGCGCATGGTGTGACGCGTTCGAACGTCGATGTCCAAAAGTTACAATGACTAGATAGGAATATGGGGGACAGTGGTACTATAGTTCAAGCGGCCGTTGGAGTTAGCTAGTACCGCGTGAGCTCTTATCCGTATTATTCGGTTTGTAAATCATCACCCATAATAAGGGGGTGAAAAATTATGCCCCTACTAACTATTCGTAGATCCAAGTATGGAAACAATTGCCCGTAAGCGGATAGCATTCACAACTTAGCTAATCACACTCAGCATTCGCCGCCCATATCTTAAGGGTGCCGCATGTAGTGAGCAAATCTCAGTGTCAACGGGCTAGGGATTTAGAACGTGCAGTTCAAAAACGGGCGACGACCGCCTATACGGAGGATACGGTACACCCATTACTTCAATCACATGTACTGCTAACCGACCACTAGTAACTTAGTTCGAGCTTCTTATGGCTTACA'

def commonSubseq(x, y, table):
	str1 = []
	str2 = []
	res = []
	for l in x:
		str1.append(table[l])
	for l in y:
		str2.append(table[l])
	length, path = mlpy.lcs_std(str1, str2)
	for i in path[0]:
		h = str1[i]
		for k, v in table.items():
			if v == h:
				res.append(k)
	return ''.join(res)

print commonSubseq(x, y, table)