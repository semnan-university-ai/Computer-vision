
# Amir Shokri [ 9811920009 ] - Farshad Asgharzade [ 9811920004  ] - Alireza Gholamnia [ 9811920011 ]
# Dr.Fadaei
# amirsh.nll@gmail.com - Farshad_asgharzade@hotmail.com - gholamniareza@gmail.com
# python exercise 2 - Question 6

import operator
import heapq

def main():
    
	inputString = open("input.txt", "r")
	inputString = str(inputString.read())

	inputString = inputString.replace(" ", "")
	inputString = inputString.replace(".", "")

	arr = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
	arrAlpha = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]

	for ch in inputString:
		charCode = ord(ch)
		if charCode > 96:
			if charCode < 123:
				arr[charCode - 97] += 1
				continue
		if charCode > 64:
			if charCode < 91:
				arr[charCode - 65] += 1
				continue

	inputDic = {}


	for x in range(0, 25):
		inputDic[arrAlpha[x]] = arr[x]

	#inputDic = sorted(inputDic.items(), key=operator.itemgetter(1))

	char_to_code = huffman(inputDic)
	char_to_code, encoded = huffman_encode(char_to_code)
	print(char_to_code)
	decoded = huffman_decode(invert_dictionary(char_to_code), encoded)

def huffman(freqmap):
    class Node:
        def __init__(self, freq, char, left = None, right = None):
            self.__left = left
            self.__right = right
            self.__freq = freq
            self.__char = char

        def addLeft(self, left):
            self.__left = left

        def addRight(self, right):
            self.__right = right

        def freq(self):
            return self.__freq

        def char(self):
            return self.__char
        
        def hasLeft(self):
            return self.__left != None

        def hasRight(self):
            return self.__right != None

        def isTerminal(self):
            return not(self.hasLeft()) and not(self.hasRight())

        def left(self):
            return self.__left

        def right(self):
            return self.__right

        def __lt__(self, other):
            return self.freq() < other.freq()

    queue = [Node(freq, key) for key, freq in freqmap.items()]
    heapq.heapify(queue)
    for i in range(len(freqmap) - 1):
        left_node = heapq.heappop(queue)
        right_node = heapq.heappop(queue)
        heapq.heappush(queue, Node(left_node.freq() + right_node.freq(), None, left_node, right_node))
    root = heapq.heappop(queue)
    if root.isTerminal():
        return {root.char(): '0'}
    stack = [(root, "")]
    char_to_code = {}
    while len(stack) > 0:
        node, code = stack.pop()
        if node.hasLeft():
            stack.append((node.left(), code + '0'))
        if node.hasRight():
            stack.append((node.right(), code + '1'))
        if node.isTerminal():
            char_to_code[node.char()] = code
    return dict(sorted(char_to_code.items()))

def huffman_encode(text):
    def build_freqmap(text):
        length = len(text)
        freqmap = {}
        for i in text:
            freqmap[i] = freqmap.get(i, 0) + 1
        for key in freqmap.keys():
            freqmap[key] = (freqmap[key] / length) * 100
        return freqmap
    char_to_code = huffman(build_freqmap(text))
    encoded_symbols = []
    for x in text:
        encoded_symbols.append(char_to_code[x]) 
    return char_to_code, ''.join(encoded_symbols)

def huffman_decode(code_to_char, encoded):
    decoded_symbols = []
    symbol_start = 0
    symbol_end = 1
    length = len(encoded)
    while symbol_end <= length:
        key = encoded[symbol_start:symbol_end]
        if key in code_to_char:
            decoded_symbols.append(code_to_char[key])
            symbol_start = symbol_end
        else:
            symbol_end = symbol_end + 1

    if symbol_start < length:
        raise ValueError("The encoded string cannot be recognized")

    return ''.join(decoded_symbols)

def invert_dictionary(dictionary):
    return dict(map(reversed, dictionary.items()))

if __name__ == "__main__":
    main()