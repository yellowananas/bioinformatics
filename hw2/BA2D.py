k = 12
t = 25

dna = ['ACAGTGGCCATCAGCCCTTAAAACGTTGATACGTTATCTGTTTCATTATACGAGCCATTGTTTCCGGACGCGCGCGGACCTTTATCGAGGGGGTTGGCGCTATCTGAGTAACCGTCCCACTGATAAAAACTCTAGGCCCACATAGCGTAAAGTTCA',
'TCGTGAAGTTCATTTTGAGAGGATTATAGTACCTAGTATATCTAAATCAGCTATTAATTTCGTAATCAGCCGACTAGACGATAATTAATATAGGTCGCCTTATCATACCCGGTCATTGCATGGCCCGCAGCAGCTGTTTTAAGACAAGCTAGGGGC',
'CCATAAAGTTGACGCTGTCTGAGCCACCCATAGATGCAGATATGTCCTAGGGCATACAACAGTGAATTACAAGCACTCCTTGCGTTGAAAAATCAACTTAGGCGGCGTCGCGCTCTTATTCAAGCTAAGCCTGGCGGTTAAGCCGTGTCTCCCCGT',
'ACCGTTCGGAAAACTCCTCTTATATAGAGGGATGCGCGAATTGATACGCTATCCTAAGTTGCTCAAATTTAACAATAATAGGGCGTGAACAACGACTCATAAAGTTTATCGGCATGTCATTAAAACTGACCAGCGTGCCAGCAGATCTGCAACGAG',
'AAGTGGCAATCCTGTCTCACTGCAAGTTTCGCCACGGCTCACCTTACCTTCTTACGTATATCGATGGCAGTAGCTTAAAGTTGATGGTACCAGCGATGCCACTACTCGCCTCGGACATATTCCACCCAGACATATTAGTCCGGCGACCTGCTCTCG',
'CAGGTTGACGTTTCAGGGAAGTGAAATCCATTGAGACAATTGGGATCTCACTGTGATCTATGGAGAAAGCAAGGCCCGGGTGAGGCGAAGGAGTGATAACGTCCTCCGCCTCCACTCAGTCAAAGCAGTAGTGCCTAAAGTTGAATCTACGGTGCT',
'AGCGAAACCCTGTGAGATACTGCGCCTTGAAGTTAACGTCTCTGCAACGCTGTAAAGCTCTCCCTTGGGCAAGTCCCATCGGTGACGGCATGCTATAACTATTTGGTCGATCCGCAGAGGCTGACGGAGGGTGTAATCACCGCCATGTGAGAGGTT',
'ACTATATGTTCGGCTCCGCCACCGAGACGTTGAGTTGGCGTGGCGCCGTATCCATTTATATTTGCCAAGCGACCAGCAGCACGGACGTCATGCGGTTCGTGAAGTTGATCCGACCTGAACACTGACAATCATCGAAGTATGACTCCCCAGCTCTCT',
'TCGCCGATTCGCAGGTCACTCCTATGGGGTCTAGTTACCTTAAGTTCAAAGCATAACCCGATCGGTAGATCACCACAAATCGTGGTATCTTCACACGACTTCTACAGCAAGAAGCGGTGAGGGACCGCGCTTTCACCGTCTTTGAGCCCAACACGA',
'CCCACGGTTCTAACCAATGCCGCCCAGGGGTACATCCTACATCCAGCCTCCCATAGTGACAAACAATACGAGTTTAGCTCTGCCCTATGACTGAATGAAATAAAAAAGTGACGCTTGGCGCGTTATAAGACTCCGTGAAGTTGAACAAGGCAGACT',
'TTTCTTAGAAAGATGGCTAGTCGGAAGGGACCACCAAGCGGCGCGTCAACAAGTAAAGACACCGTGGCTGCGGGGCTCTCCAGTACATGAAGTTAAGATGCACTTTACTCTGACCCTCGTCAAACTACAGTTCGCTCATCCTAGCAGAACCCCAGA',
'CCATTAAGTTGATGCGCTGGAGTGTTGGATATTAACGAATATGATCGATTACAGTGGCATGAGACTATTACTAGAGGTCGGGGGAAATAGCGCGCTGGAGAACGAGAGTATTGAGGGACTGTTGGCTTGTCACTGCGACACCAAAACGGCCACAGC',
'GTCCAGTGTCCACGAAGTACTCCTCTCTGCTGTGCGTGGATTTAACCTTGACATAAGTATTGGAAATTTCGTGCTGTCACGCCTAGTTGAAACCGCTGGGTAGATTGCTACGTGCTCGTACGACTCTCTTTACTTGGGAAGAGCACTTTAAGTTCA',
'ACAAAGACTTCCGCCCTGTCCGCTTACACAATTAGGGTAGTTCTGATGAGCACGGCCAGTTACAATCTTGTTAACGCGTCAGTTTCCTAAAGTTCAGTCAAGACCCAATTTTCGCAGTGGCAGCTGACATCAGAAGGCGATGTCCAGGCCAAGTCT',
'GTGCAGTGCTCCGTTCATACTGGCCGCGTGTTGCGCTTCGGGGTCAGCGAGATAAACTCGGACTAAGTGAGCTGCAACTTGCGTACTTTAAGTTTACCACCAGATAGCTTAGTCGTTTCCTTCTACATTTTTCATTACTCCACGTGGGTCCCGTAA',
'ATCTGAGCGTTGTCTACACTCCCTTCGTAAAGTTAATTGGTTACGTCACGCGCTCTGGTACAGACAGGACTAAGATAGAAGTGAGATGTAATCCTCATACGAGACAGGTGCGGAGCATTGGTAACATTGTGCACCTAGAAAGTCCCTCGCCACTGC',
'TCGCACTCGAAATGGATAGCACCGTCCTGCATTAGCCGCCTTTTGAACGGGCAACGGTTATAGACAAATCGTGGCAGAAGGCCGACGACACGTCTCGCCGTCCAAGTACCTTTAAGTTGATATGGCAAAATATGCACCGGACCTCAATACTATAAG',
'TACCCACTCTCACCTTCAAGTTAATCATTACAAGTACGCTCAAGCTGGAATATAGCCGACCGCACGGGCCACAGGGGAGGGCGCGTATGCGGGCCGTCGGTACGTTGCAAGGGGCAGTCCAGGACGACGTGCTCGCATCTCGCCTGTGTGCCTATC',
'CCCGCGACTAAATGGTCTGATACGGATCCAATAGTTAGCCATTGATATAATCCCGACTACTTTCGCTAGCCGACTTAAAGTTTAACGAAAACGACAGTAGTCTAGACCGCCCTAGGTTGTATTATCATCGGGTCCCGCAGAGCGTGGGTACGAGAG',
'TGAATTCGCGACGATAGGGCCTGTTATAGACATGGGGCGTTAGACTAGAACCCAAATCAAGACCCGAGCGTAATAATTATATTACCGAGATCCTCCTGTTGCCTGCACGAGGTGCTCCACCCATGAAGTTTAAAACCACTATGGTGAGTACGGGTG',
'GGGCTGGGACGATCCATGTGACGGGTTTTCCTAAATGGTTGTGCTGCTGCATTAAGTTTATATTGGTGTAAATCCATTTGTAAGCTAGACAATACGGTCCGCCGGCAATCCCTAGGCATTAGGGCCGCAAGGACCTTGCCGCTATATATTTTCGGC',
'CATGTCGCCATGGAAACTGGGCCCCACGTCACACAGTCGGACGTGATTTTCACGGTGGCCGCTTTCTAAGAGCACTAAGGAACCTATACTAACCCCGTGCTTGAATCCGTCTCACTGCCGCCATCAAGTTAATATTAAAGGAATTCACGGGATCCA',
'TGTAAGAGCGATAGGCTTGGTACTCGTAATCAGCCTCTTGGCCTTCCTTCGCATGGCATTCTAGCGCGGTCACCTACTAACTAAGGGCCCGTTATAGCCTGAAGTTCACGCAGTGACTTGTATCACTGCAAAAGTGATCCTAAAGCGCATGCTCAA',
'CCACAAGATGGATTCAAAGGTATCAAAGACGGCAGCGATAGGTCCCTGATAGCTACGATTAACGTAGAGGTCCATACAATAGAACTTGGAACTCGCGCAAGAGCCCCTAGTAGTCAGTACGCTATATTCGACCCATTAAGTTAACGTTGAACGCCC',
'AATTACTTCCAGCGATGGGTTTTACGAACTACATCTATCATGTGAGTGTGCAAATAGCGAACCTCAAGTTCACCTGAGAGCACGTACTACGAGGGCTTCCGTATAGGCCTTAGTTAATCCCGTGCTGTCATATCGCGGAGCCATGTATCTCTATCA']

def formProfile(word, k):
	alpha = ['A', 'C', 'G', 'T']
	profile = [[0] * k for _ in range(4)]
	for w in word:
		for i in range(0, len(w) - k +1):
			string = w[i:i+k]
			for l in range(0, len(string)):
				index = alpha.index(string[l])
				profile[index][l] += 1.0/((len(w) - k + 1) * len(word))
	return profile

def mostProb(string, k, profile):
	alpha = ['A', 'C', 'G', 'T']
	max_prob = 0
	res = string[0:k]
	for i in range(0, len(string) - k + 1):
		prob = 0
		word = string[i:i+k]
		prob = 1
		for l in range(0, len(word)):
			index = alpha.index(word[l])
			prob = prob * profile[index][l]
		if prob > max_prob:
			max_prob = prob
			res = word
	return res

def score(array):
	alpha = ['A', 'C', 'G', 'T']
	res = 0
	for i in range(0, len(array[0])):
		let = {'A':0, 'C':0, 'G':0, 'T':0}
		for word in array:
			let[word[i]] += 1
		maxval = max(let, key=let.get)
		for word in array:
			if word[i] != maxval:
				res += 1
	return res


def greedyMotifSearch(dna, k, t):
	bestMotifs = []
	for string in dna:
		bestMotifs.append(string[0:k])
	for i in range(0, len(dna[0]) - k + 1):
		motifs = []
		motifs.append(dna[0][i:i+k])
		for e in range(1, t):
			profile = formProfile(motifs, k)
			motifs.append(mostProb(dna[e], k, profile))
		if score(bestMotifs) > score(motifs):
			bestMotifs = list(motifs)
	res = '\n'.join(bestMotifs)
	return res

print greedyMotifSearch(dna, k, t)


