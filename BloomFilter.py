import math
import mmh3 #hash function
from bitarray import bitarray 
import BitVector


class BloomFilter(object):

    def __init__(self, bit_count , number_of_hashes):
        print "BloomFilter"
        if bit_count<= 0 or number_of_hashes<=0 :
            raise ValueError('Error: Bit count and Number of hashes should be greater than zero.')

        self.bit_count = bit_count
        self.number_of_hashes =number_of_hashes

        #Initally there are no elements in the set
        self.n = 0

        #Craete a BitVector to store the bit values
        self.bit_vector = BitVector.BitVector(size = self.bit_count)

        #Set all the bits to zero
        self._setAllBitsToZero()


    def _setAllBitsToZero(self):
        for i in self.bit_vector:
            self.bit_vector[i] = 0

    def GetBitIndicesFromInput(self,inp):
        list_of_bits = []

        for i in range(1, self.number_of_hashes+1):
            list_of_bits.append((hash(inp) + i*mmh3.hash(inp)) % self.bit_count)
        print inp ,":",str(list_of_bits)

        return list_of_bits

    def CheckIfInputIsPresent(self,inp):
        for i in self.GetBitIndicesFromInput(inp):
            if self.bit_vector[i] != 1:
                return False

        return True

    def ProbabilityOfFalsePositives(self):
        p_fp = math.pow((1.0 - math.exp(-(self.number_of_hashes*self.n)/ self.bit_count)), self.number_of_hashes)
        print self.n,p_fp
        return p_fp

    def AddtoBitVector(self, inp):
        for i in self.GetBitIndicesFromInput(inp):
            self.bit_vector[i]=1

        self.n = self.n + 1
        #self.ProbabilityOfFalsePositives()

    def GetLength(self):
        return self.n



    def clear(self):
        self.n=0
        self.bit_vector = BitVector.BitVector(size=self.bit_count)
