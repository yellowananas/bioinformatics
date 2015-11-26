pattern = 'GCCGCAC'
dna = ['TCGCTGCTATAGTATCCCGCCAAAAAACCAGATCCACAACCGGACGGCTTATTCAGTTCGAGCTGTGTCTTCCAAACTCCTATAGCCCACAATAATCG',
'ACGGCTACTATTATTTTGTCGACGGTTGTACCTTAGGCTCACTAAGTACGGTAACAAGCACAGGCGCCTTACACACGCCGCGATACCGGCGATGACGT',
'CCCATAACTGATCACTCCGATTAGAACTGCAAAATGGCCCCGATCTTTCCGTTTAAGATTTACACGTCACAAGGGAACCATTAGGAACCTGCATCGAA',
'GAAGCGCCCCGGAGATACAAGATCCCCTGAGGCCCCGCAAACGGGACGATAAATCTATGTCCCCGAGAAATCTCGCATCTCAGCCACAGGTATAGGCC',
'GGCCATTTGAGGCCGATATTAACCAGGGTACATCGTCTTAATGCAAAGTACTAATCTGAGTGACTACCCTCAACTGGCAGTGTCCACACGGTTTGGAA',
'GGCTATGCTGTATTTATTTCCTCGCCCACCTACAGCAGAAAAGCCCGTGTGTTTCCATGAAATAGTGTGCCTGCACGTGGGGGCGCTGACGGGAGACA',
'GTGCACGGACGCCATTGAGCGGAGAACATAAATCCTCAAACCCCCGCATACTCTGAGGACGGGACACCAGGCCAGGAGCAATACTAGGAGGCAGGTTA',
'ACGGTAAGAACTGGGTGAACCAAGCGGATGTGTTATGAGGAATGTACTCCGGGTAACGCAGAGTACACTGGTACGCTATGGATAGTTATCAAATAAAT',
'CAGTAAAGCCCAGTAACAAATGAGGCTCCAGATCCGGGCGCTCATGTGTATTGCTGCACTTGACGGCATATAATTTCTTACCTCTAAGGTGTCACTTA',
'CCCTGCACAGGGGTGATTCCCTCTTAGAGCCTCGTTCCTCGGCACGAGCCTTGGTTACCTTAACGGCCGCGCAATTGGATTGAAAGGGTTCGGGTAGG',
'AGGATCGTAATGCAGATTGTTGTTCTTTCCACCGGGGAGAGATCTCATTTTGGTACCGTGATCGTTTCTAAGCCGCACTGCGGGAGTATATGCAGAAT',
'ACCCTGTCATCTCCGGTTATACCCCCGAGTCAGAACGTTAACTAAACCTGAGGTCCTGACAAGGCAATAAAAGAGGTGTATGTCTGCAAGTTGAGCGT',
'ACAGAATCACCCACACTCGTCCATTTCCTGTCCAAACCGGTCATCTGAGGCCTGATATCCTGTGGACCTAGGTTAGCCGGTCCCCGCGCCGGAAATGT',
'GGCTGAGTAGTACGAATTACATTTGACCCTAGGCTAACCCTGACGTTTCTAAGTGATGTACCGATGTTGATAGGTTCAGGAGAGGATCAAGCGCATTT',
'GCGAAGATGTAGTGAGGGTAGGGGTAATGTTACAGGGTCCGTTCCCCACGGTGCCTACAAATTTAACCATTCGCTGCCTATCCCCGCTCTTGAAGGGC',
'ACGTACATGCTACCGGGCATCACCTTTCGCGGCTTAGGTGCGTTTGGAACGCCAAGCCCGGAAGGCCAGCAGTAGCATATTGATAGCGCTTGTAGTCC',
'ATCGGGCCTCTTCCTGAACGGGCGCTGACTCCATTATATCATCCAACGCGCTGCGCTCGCGGACGTGCCAGTACAAAGTGACAGTTCTTGTACGGAGA',
'GATTATGCCGGCATGGAGAAACTACGTTAACTACTTCACAGTTGAACGGTGGATGAATCCCGAGTAACTCATTAACACTAATGTGACGCAGCACACTT',
'TAAATGCAAGCGCCCTATCCGTTCCGGACTGGGACTCGCGTGACAAACGTTAACTGAGGCCGCTACTTCCAATAGGTGTCCAATTGAACTACGGGGGC',
'ATGCATACTGTGTTTGGTAGTCTCTATGATACATTCGAGACGCAAGACTTCTGCTGCAGCTAAACCTCCAGTCTTCATTCTACCTTGATAACTAATTA',
'CCGCTAACACCAGTCTCTTCAGCAACCCCTCCTGAGTCTCCTATAGTCGTGTGAGAGTAATCCAGCGGTCCAATGGGGATCATGATGGTATTCCGTGA',
'CACACGCTGCCGAATAACTAAAGGACAGTTGTAACTTCGTCCGAAGACTGCGAGCTTAATCCCCTAAGACGAATCCACCGAAATAAGCCGCTGTCGTT',
'GGCGGGCGCTTCAGGTGACGAATAGTGGGGATGATCCTGCTGAATTTCCACCTGCTAGGAGGGTTAGAGGTCTGGACCCGGAGGATTGAATGTACTTT',
'GCTATTGACCATGCGCCGAGGTAGGATAGATTATTTGGCGAACGCAAGGGAATAACTAGCAATTCGGCCGGATAATGCAGTTTGTTGCGAGATCGGTG',
'TGCTTCGCACAGGAAGTGTAGAAGATTACACATTCCAATCCTTATGCACCTCGAAGACCGATGGACTACTCCATAATGATAGACTGAGATTAAACTGT',
'CCCGCCGCGTTTCGGCGCTGCTACCAGGAGTGCCTATGTGAACGAAGGTTATAAACATTTGTTGATTTAGGTAAATTAGGCGCAACCTGCTAGTGCTA',
'AGTGGGCACCCAAACTAAGTTACATGCCCCCCATGGAAAATCTGTTACACCGCTAACTGACAGTGTCGTAAGATAATGGTGCAGTCTGGCGGGTTCGG',
'TGGGTCAGGACCACTATGGAGTTTCCACACGCCGTACGCTATATTCCCAGGCAAGGTTCGGAAGGCGCAACGAGTGATCCGTCGGGGAGTCACGCAGT',
'GGCGCGAAACCGGATTTCCAAAGATACAACCGCGCGCGACAGCCCAGAATTATATGTATGTTGTTCAAAGAACCCCACATGGACAGTGTTTTATACGT',
'GCTTGCCGTTCTAAGTATGCATCCGGCGGCGATGTTATTCCCGAGGAGCTGTATACAGGTATTGACCCGCATTTTGTGACGGTGGCCTGGGTATTTCC',
'CCCCGACACCGCCTCGGGATTGCTTAAAGATTCTAGTAGTCTGCACTTCTATTCTGCTTGGTTCCATTGTTGTATGCCCGCTCAATCTTTGTAATATG',
'TCGGCGAGGCCTTTCCTGATTGCCCGGATCGCAAGGATTTTTGTCGGCTTCACCACGTTCATTAAGTACGTATTGGCTCCGGAGATGGATTAGTAACT',
'GTGAAGAGAGCTTCAGAGTCTCTGCCTCCGCTCTGCGTGGTACCTTCTTCGTACAATTCAACGCCGTACAGCTCAGGTACCTCGTTTGTCTATGTCTG',
'TCAATTGTATGACTCCTACCATCGTCTTAATCCACGGGATTTTTATCTTCCTCATGTATCAGGTTCTGTACACACCGTAACTGTAACAATCTTCCGGC',
'TGATATCAACCAAAGAGGCTCAGCTCCACGGTCCTTACCTTTGCTCTTCTCGTCACATGAAAATAAGGAGTGACTGCATGCGCGGTACGTCATGAGGT',
'CGAGGTTAGAGCAGCAAGGGGTTTCCCGGTGCCGGTCCGGGACTTGGTTGTAACCTAGGCAAGTTCTGTCACTCCTCCCCCCTGTGTACGGGGGCGAG',
'CTCCGAGCCTGACTTGGAATTTTGGAAAGACCCCCATATGGGTCCGTTTCAATGCCCAGATAACCTTTAATACACGCGCGTTAGATTACATCCAACGC',
'CGAATACCGTCGTCAGGAGCACTGTGAGACCTCCGATTTGACGCACCGGATCTTGAGCCATCCGTTCTCAATGTGCGTGCCAATAGTCGTCCTGGCTG']

def hammingDistance(string, pattern):
	res = 100
	k = len(pattern)
	for r in range(0, len(string) - len(pattern) + 1):
		word = string[r:r+k]
		ham_dist = 0
		for i in range(0, len(word)):
			if word[i] != pattern[i]:
				ham_dist += 1
		if ham_dist < res:
			res = ham_dist
	return res

def distancePatternStrings(pattern, dna):
	res = 0
	for word in dna:
		res += hammingDistance(word, pattern)
	return res 

print distancePatternStrings(pattern, dna)
