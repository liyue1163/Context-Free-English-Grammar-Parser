# Context-Free-English-Grammar-Parser
- Context-free English grammars for the chart parser in NLTK, the grammar is able to properly handle valid sequences of auxiliaries and nested complements in a sentence.
- In order to parse English sentences, modify the test sentences contained in parser.py and run it.
- It is widely acknowledged that building a perfect parser is demanding, below are some discussions about the limit of this parser.

I will combine the over and under generated sentences together to discuss the limitation of my final grammar:
Some limitation occurs in the noun phrase part, the grammar is not able to handle the noun phrase that is modified by a subordinate clause, for instance, my grammar cannot parse a valid sentence like “the cat that is black ate”, in which our rule cannot parse noun phrase ‘the cat that is black’ because I only allow Det, Adj, and PP be attached to a noun.
Under generated sentence such as ‘my cat Nadia jumped’ was also revealed, in that sentence Det ‘my’ and noun ‘cat’ together modifies Nadia and the current rule doesn’t allow a noun to modify another noun in a noun phrase
Even if we only use Det, Adj or PP to attach to a noun, there was also some limitation observed. For instance, my rule is not able to tell if duplicated Adj’s are attached to a noun, which means that the sentences like ‘the tall tall tall cat come slowly’ will be over generated. 
 
Some limitation occurs in the verb phrase part, the infinitive phrase is considered in this assignment such as ‘he wanted to run’ and it will be correctly handled. But the final grammar cannot correctly generate an infinitive phrase when it’s used to introduce a purpose. For instance, ‘I give you help to run quickly’ cannot be parsed because the grammar can only parse that sentence up to ‘I gave you help’ but doesn’t consider the following infinitive clause. 
 
As for test strategy, I intuitively conducted the test: I first tested basic and simple sentences that involve only nouns and verbs, then I increased the complexity by adding other phrases like PP and Adv, respectively. I paid attention to the positions of Adv and PP because it could have different meanings and some combinations are not grammatically correct. Then I added additional phrases together to test long sentences. Also, whenever I revised the grammar, I checked all the test sentences again. 
