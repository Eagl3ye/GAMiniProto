import random

correct = "241680"

class Gene:
	expression = ""
	def __init__(self):
		self.expression = self.createExpression()
		self.fitness = self.getFitness()

	def __str__(self):
		return self.getExpression()

	def __eq__(self, other):
		return self.expression == other.expression

	def __hash__(self):
		return hash(('expression',self.expression))

	def createExpression(self):
		expression = ""
		for i in range(len(correct)):
			expression += str(random.randint(0,9))
		return expression

	def getExpression(self):
		return self.expression

	def mutate(self, m_chance):
		m_expression = "" 
		for data in list(self.expression):
			if(m_chance == 0): 
				m_expression += data
			else:
				if(random.random() <= m_chance):			# Replace it with another number
					isItself = True							# other than itself
					m_data = data
					while isItself:
						m_data = str(random.randint(0,9))						
						isItself = (m_data == data)
					m_expression += m_data
				else:
					m_expression += data
		self.expression = m_expression
		self.fitness = self.getFitness()

	def getFitness(self):
		fitness = 0
		compare = correct
		for locA, locB in zip(list(compare),list(self.expression)):
			points = abs(int(locA) - int(locB))
			fitness += points
		return fitness

class GenePool:
	genepool = []
	def __init__(self,parent_pop):
		self.genepool = self.init_GP(parent_pop)

	def __str__(self):
		return self.get_GP()

	def init_GP(self,parent_pop):
		i_genepool = []
		for i in range(parent_pop):
			i_genepool.append(Gene())
		return i_genepool

	def get_GP(self):
		out_genepool = ""
		newline_ctr = 1
		for gene in self.genepool:
			out_genepool += str(gene) + ":" + str(gene.fitness) + " "
			if(newline_ctr == 5):
				newline_ctr = 0
				out_genepool += "\n\n"
			newline_ctr += 1
		return out_genepool

	def mutate_GP(self):
		for gene in self.genepool:
			gene.mutate(1)

	def sort_GP(self):
		self.genepool.sort(key=lambda gene: gene.getFitness())

	def rem_dupes_GP(self):
		#print("{} Genes in the genepool [before]".format(len(self.genepool)))
		self.genepool = list(set(self.genepool))
		#print("{} Genes in the genepool [after]".format(len(self.genepool)))

	def topGP(self):
		return



##############################################################################################

x = GenePool(10000)
x.rem_dupes_GP()
x.sort_GP()