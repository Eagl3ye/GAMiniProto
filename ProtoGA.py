'''
 For the context of this code, our goal is to make
 a simple Genetic Algorithm that can brute-force
 its way in to getting the CORRECT answer. 
'''
																		# This variable is the expected value of a gene.
CORRECT = "241680"														# Used to compare and compute fitness values 
																		# We can change this to any 6-digit number as we wish
'''
 The fittest Gene can be determined by comparing a
 Gene candidate to the CORRECT variable above.  
'''
##############################################################################################
'''
 Add all imports needed here
'''
import random	

##############################################################################################
'''
 Insert any Classes we wanted to add here
'''
class Gene:
	expression = ""														# The content of a Gene
	def __init__(self):
		self.expression = self.createExpression()						# Initialization of the content of the Gene
		self.fitness = self.getFitness()								# The calculated fitness of the Gene

	def __str__(self):													# For debugging, it can display the content of a Gene
		return self.getExpression()										#	by doing: print(Gene)

	def __eq__(self, other):											# It enables comparing two Objects directly
		return self.expression == other.expression 						#	Ex:	Gene_A = Gene_B

	def __hash__(self):													# It enables comparing two Objects directly too
		return hash(('expression',self.expression))						# Also needed to identify unique Objects and duplicates 

	def createExpression(self):											#-----------------------------------------------------
		expression = ""													#
		for i in range(len(CORRECT)):									# << Produces 6-digit number (length of CORRECT)
			expression += str(random.randint(0,9))						# << For every digit... create random number (0-9)
		return expression 												#

	def getExpression(self):											#-----------------------------------------------------
		return self.expression 											# << Call this to get the content of the Gene

	def mutate(self, m_chance):											#-----------------------------------------------------
		m_expression = "" 												# 'm_chance' - chance of mutation to happen on every digit of a Gene
		for data in list(self.expression):								# << Converts a string to an array of letters (to be iterable)
			if(m_chance == 0): 											# << If 0% chance of mutation then it will not mutate at all
				m_expression += data 									# << Passes the original digit to another variable
			else:														#
				if(random.random() <= m_chance):						# random.random() - returns a float between 0 to 1 (inclusive)
					isItself = True										# For ex:	If random = 0.12  and  'm_chance' = 0.01  
					m_data = data 										# 				then the mutation will not happen
					while isItself: 									# 'isItself' - a variable used to trigger if the condition is met
						m_data = str(random.randint(0,9))				# << Gets a random value from 0 to 9
						isItself = (m_data == data)						# << If it still gets its original value then the loop repeats...
					m_expression += m_data								# << ...Otherwise the new value is added to the string variable that 
				else:													#       will be returned
					m_expression += data 								# << "REDUNDANT LINE OF CODE / FOR REDUNDANCY"
		self.expression = m_expression									# << The Gene will have its new value or the post-mutation value 
		self.fitness = self.getFitness() 								# << Calls a function to get the fitness value of the new content of the Gene

	def getFitness(self):												#-----------------------------------------------------
		fitness = 0														#
		compare = CORRECT												#
		for locA, locB in zip(list(compare),list(self.expression)): 	# << Iterates the two iterable arrays of letters simultaneously
			'''
				For ex:
					If...
					  compare 			= "112412"
					  self.expression 	= "927234"
					Then at 1st iteration...
					  locA = "1"
					  locB = "9"
					Then at 2nd iteration...
					  locA = "1"
					  locB = "2"
					And so on
			'''
			points = abs(int(locA) - int(locB)) 						# << It calculates the distance of the number from the number of the expected value 
			'''
				Let's say:
					compare 		= "112412"
					self.expression = "927234"
					At 1st iteration:
						v
					   [1] 1 2 4 1 2 
						v
					   [9] 2 7 2 3 4

					   Distance is 8
					At 2nd iteration:
						   v
					    1 [1] 2 4 1 2 
						   v
					    9 [2] 7 2 3 4
					   Distance is 1
					And so on
			'''
			fitness += points											# << All points will be added							
		return fitness                                                  #

class GenePool:															#-----------------------------------------------------
	genepool = []														# << Creation of an array
	def __init__(self,parent_pop):										# 
		self.genepool = self.init_GP(parent_pop)						# << Initialization of the Genepool by calling a method

	def __str__(self):													# For debugging, it can display the content of the Genepool
		return self.get_GP()											#	by doing: print(Genepool)

	def init_GP(self,parent_pop):										#-----------------------------------------------------
		i_genepool = []													# << Call this method to initialize the population of the Genepool
		for i in range(parent_pop):										# << Creates [n] number of Gene...   
			i_genepool.append(Gene())									# << ...and each is appended to the Genepool
		return i_genepool												#

	def get_GP(self):													#-----------------------------------------------------
		out_genepool = ""												#
		newline_ctr = 1													#
		for gene in self.genepool:										#
			out_genepool += str(gene) + ":" + str(gene.fitness) + " "	#
			if(newline_ctr == 5):										# Just some text formatting code / For debugging
				newline_ctr = 0											#
				out_genepool += "\n\n"									#
			newline_ctr += 1											#
		return out_genepool												#

	def mutate_GP(self):												#-----------------------------------------------------
		for gene in self.genepool:										# << For every Gene in the Genepool
			gene.mutate(1)												# << Calls the 'mutate()' method of the 'Gene' class with the 100% mutation chance 
																		# [!] - mutation chance can be changed here

	def sort_GP(self):													#-----------------------------------------------------
		self.genepool.sort(key=lambda gene: gene.getFitness())			# << Some pythonic way to sort an array of Objects by their fitness value

	def rem_dupes_GP(self):												#-----------------------------------------------------
		self.genepool = list(set(self.genepool))						# << Removes duplicate Genes by converting it using Set() and back using List()

##############################################################################################
'''
 Insert any implementations here
'''

x = GenePool(10000)
x.rem_dupes_GP()
x.sort_GP()


