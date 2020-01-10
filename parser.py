import nltk


def test(sentence):
    print('\n')
    print(sentence)

    parser = nltk.parse.BottomUpChartParser(grammar)

    for t in parser.parse_all(sentence):
        print(t)


if __name__ == '__main__':

    grammar = nltk.grammar.CFG.fromstring("""

S -> NP VP
NP -> NsubjP

# subject noun phrase
NsubjP -> Np | NproperP | Nsubjpron

# object noun phrase
NobjP -> Np | NproperP | Nobjpron

# regular noun phrase
Np -> N | Det N | Det AdjP N | AdjP N | Np PP

# proper noun phrase
NproperP -> Nproper | Det AdjP Nproper | AdjP Nproper

PP -> P NobjP

AdjP -> Adj | Adj AdjP
AdvP -> Adv | PP AdvP


VP -> VtrP | AuxP | VintrP

# VP of intransitive verb
VintrP -> Vintr | Vintr AdvP | Adv Vintr | VintrP PP


# =====================
# VP of auxiliary verb
AuxP -> PerfectV | BeV | MdV | MdPerfectV

# progressive passive VP
VprogpassP -> Vprogpass | Vprogpass AdvP | Adv Vprogpass | VprogpassP PP
Vprogpass -> BEprestp VpastpPassive | BEprestp Adv VpastpPassive

# passive VP
VpassP -> Vpass | Vpass AdvP | Adv Vpass | VpassP PP

# past participle verb for subject-predicate VP
VpastpSubjP -> VpastpSubj | VpastpSubj AdvP | Adv VpastpSubj | VpastpSubjP  PP

# past participle verb for passive-voice VP
VpastpPassiveP -> VpastpPassive | VpastpPassive AdvP | Adv VpastpPassive | VpastpPassiveP PP

# progressive VP
VprogP -> Vprog | Vprog AdvP | Adv Vprog | VprogP PP

# present VP
VprestP -> Vprest | Vprest AdvP | Adv Vprest | VprestP PP

AuxPrefect -> SingularPerfect | PluralPerfect | PastPrefect

PerfectV -> AuxPrefect VpastpSubjP | AuxPrefect BEpastp VpastpPassiveP | AuxPrefect BEpastp VprogP | AuxPrefect BEpastp VprogpassP
# add possible position for Adv
PerfectV -> Adv AuxPrefect VpastpSubjP | Adv AuxPrefect BEpastp VpastpPassiveP | AuxPrefect Adv BEpastp VpastpPassiveP  | Adv AuxPrefect BEpastp VprogP | AuxPrefect Adv BEpastp VprogP| Adv AuxPrefect BEpastp VprogpassP | AuxPrefect Adv BEpastp VprogpassP


BeV -> BEpass VprogP | BEpass VpastpPassiveP | BEpass VprogpassP

MdV -> AuxMd VprestP | AuxMd BE VpastpPassiveP | AuxMd BE VprogP | AuxMd BE VprogpassP
# add possible position for Adv
MdV -> Adv AuxMd VprestP | Adv AuxMd BE VpastpPassiveP | AuxMd Adv BE VpastpPassiveP | Adv AuxMd BE VprogP | AuxMd Adv BE VprogP | Adv AuxMd BE VprogpassP | AuxMd Adv BE VprogpassP

MdPerfectV -> AuxMd PluralPerfect VpastpSubjP | AuxMd PluralPerfect BEpastp VpastpPassiveP | AuxMd PluralPerfect BEpastp VprogP | AuxMd PluralPerfect BEpastp VprogpassP
# add possible position for Adv
MdPerfectV -> Adv AuxMd PluralPerfect VpastpSubjP | AuxMd Adv PluralPerfect VpastpSubjP
MdPerfectV -> Adv AuxMd PluralPerfect BEpastp VpastpPassiveP | AuxMd Adv PluralPerfect BEpastp VpastpPassiveP | AuxMd PluralPerfect Adv BEpastp VpastpPassiveP
MdPerfectV -> Adv AuxMd PluralPerfect BEpastp VprogP | AuxMd Adv PluralPerfect BEpastp VprogP | AuxMd PluralPerfect Adv BEpastp VprogP
MdPerfectV -> Adv AuxMd PluralPerfect BEpastp VprogpassP | AuxMd Adv PluralPerfect BEpastp VprogpassP | AuxMd PluralPerfect Adv BEpastp VprogpassP


# =====================
# VP of transitive verb
VtrP -> V_with_NP_Phrase | V_with_NP_NP_Phrase | V_with_PP_Phrase | V_with_NP_PP_Phrase | V_with_S_Phrase | V_with_toVP_Phrase | V_with_NPtoVP_Phrase

# original VP for sentence like want to do
VdoP -> Vprest | Vprest AdvP | Adv Vprest | VdoP PP

# to be NP
VbeNP -> BE NobjP

# VP for verb followed by NP
V_with_NP_Phrase -> Vpast_with_NP NobjP | Adv Vpast_with_NP NobjP | Vpast_with_NP NobjP AdvP | V_with_NP_Phrase PP
Vprest_with_NP_Phrase -> Vprest_with_NP NobjP | Adv Vprest_with_NP NobjP | Vprest_with_NP NobjP AdvP | Vprest_with_NP_Phrase PP

# VP for verb followed by NP NP
V_with_NP_NP_Phrase -> Vpast_with_NP_NP NobjP NobjP | Adv Vpast_with_NP_NP NobjP NobjP | Vpast_with_NP_NP NobjP NobjP AdvP | V_with_NP_NP_Phrase PP
Vprest_with_NP_NP_Phrase -> Vprest_with_NP_NP NobjP NobjP | Adv Vprest_with_NP_NP NobjP NobjP | Vprest_with_NP_NP NobjP NobjP AdvP | Vprest_with_NP_NP_Phrase PP

# VP for verb followed by PP
V_with_PP_Phrase -> Vpast_with_PP PP | Vpast_with_PP Adv PP | Adv Vpast_with_PP PP | Vpast_with_PP PP AdvP | V_with_PP_Phrase PP
Vprest_with_PP_Phrase -> Vprest_with_PP PP | Vprest_with_PP Adv PP | Adv Vprest_with_PP PP | Vprest_with_PP PP AdvP | Vprest_with_PP_Phrase PP

# VP for verb followed by PP  i.e. the elepant reminded Nadia of Ross
V_with_NP_PP_Phrase -> Vpast_with_NP_PP NobjP PP | Vpast_with_NP_PP NobjP Adv PP | Adv Vpast_with_NP_PP NobjP PP | Vpast_with_NP_PP NobjP PP AdvP | V_with_NP_PP_Phrase PP
Vprest_with_NP_PP_Phrase -> Vprest_with_NP_PP NobjP PP | Vprest_with_NP_PP Adv NobjP PP | Adv Vprest_with_NP_PP NobjP PP | Vprest_with_NP_PP NobjP PP AdvP | Vprest_with_NP_PP_Phrase PP

# VP for verb followed by a sentence
V_with_S_Phrase -> Vpast_with_S S | Adv Vpast_with_S S | Vpast_with_S AdvP S | Vpast_with_S Conj S | Adv Vpast_with_S Conj S | Vpast_with_S AdvP Conj S | V_with_S_Phrase PP
Vprest_with_S_Phrase -> Vprest_with_S S | Adv Vprest_with_S S | Vprest_with_S AdvP S | Vprest_with_S Conj S | Adv Vprest_with_S Conj S | Vprest_with_S AdvP Conj S | Vprest_with_S_Phrase PP

# VP for verb followed by [to do]
V_with_toVP_Phrase -> Vpast_with_toVP Pto VdoP | Adv Vpast_with_toVP Pto VdoP | Vpast_with_toVP Pto VdoP AdvP | V_with_toVP_Phrase PP
V_with_toVP_Phrase -> Vpast_with_toVP Pto Vprest_with_NP_Phrase | Adv Vpast_with_toVP Pto Vprest_with_NP_Phrase| Vpast_with_toVP Pto Vprest_with_NP_Phrase AdvP | V_with_toVP_Phrase PP
V_with_toVP_Phrase -> Vpast_with_toVP Pto Vprest_with_NP_NP_Phrase | Adv Vpast_with_toVP Pto Vprest_with_NP_NP_Phrase | Vpast_with_toVP Pto Vprest_with_NP_NP_Phrase AdvP | V_with_toVP_Phrase PP
V_with_toVP_Phrase -> Vpast_with_toVP Pto Vprest_with_PP_Phrase | Adv Vpast_with_toVP Pto Vprest_with_PP_Phrase | Vpast_with_toVP Pto Vprest_with_PP_Phrase AdvP | V_with_toVP_Phrase PP
V_with_toVP_Phrase -> Vpast_with_toVP Pto Vprest_with_NP_PP_Phrase | Adv Vpast_with_toVP Pto Vprest_with_NP_PP_Phrase | Vpast_with_toVP Pto Vprest_with_NP_PP_Phrase AdvP | V_with_toVP_Phrase PP
V_with_toVP_Phrase -> Vpast_with_toVP Pto Vprest_with_S_Phrase | Adv Vpast_with_toVP Pto Vprest_with_S_Phrase | Vpast_with_toVP Pto Vprest_with_S_Phrase AdvP | V_with_toVP_Phrase PP
V_with_toVP_Phrase -> Vpast_with_toVP Pto VbeNP | Adv Vpast_with_toVP Pto VbeNP | Vpast_with_toVP Pto VbeNP AdvP | V_with_toVP_Phrase PP
V_with_toVP_Phrase -> Vpast_with_toVP Pto BE VpassP | Adv Vpast_with_toVP Pto BE VpassP | Vpast_with_toVP Pto BE VpassP AdvP | V_with_toVP_Phrase PP



Vprest_with_toVP_Phrase -> Vprest_with_toVP Pto VdoP | Adv Vprest_with_toVP Pto VdoP | Vprest_with_toVP Pto VdoP AdvP | Vprest_with_toVP_Phrase PP
Vprest_with_toVP_Phrase -> Vprest_with_toVP Pto Vprest_with_NP_Phrase | Adv Vprest_with_toVP Pto Vprest_with_NP_Phrase| Vprest_with_toVP Pto Vprest_with_NP_Phrase AdvP | Vprest_with_toVP_Phrase PP
Vprest_with_toVP_Phrase -> Vprest_with_toVP Pto Vprest_with_NP_NP_Phrase | Adv Vprest_with_toVP Pto Vprest_with_NP_NP_Phrase | Vprest_with_toVP Pto Vprest_with_NP_NP_Phrase AdvP | Vprest_with_toVP_Phrase PP
Vprest_with_toVP_Phrase -> Vprest_with_toVP Pto Vprest_with_PP_Phrase | Adv Vprest_with_toVP Pto Vprest_with_PP_Phrase | Vprest_with_toVP Pto Vprest_with_PP_Phrase AdvP | Vprest_with_toVP_Phrase PP
Vprest_with_toVP_Phrase -> Vprest_with_toVP Pto Vprest_with_NP_PP_Phrase | Adv Vprest_with_toVP Pto Vprest_with_NP_PP_Phrase | Vprest_with_toVP Pto Vprest_with_NP_PP_Phrase AdvP | Vprest_with_toVP_Phrase PP
Vprest_with_toVP_Phrase -> Vprest_with_toVP Pto Vprest_with_S_Phrase | Adv Vprest_with_toVP Pto Vprest_with_S_Phrase | Vprest_with_toVP Pto Vprest_with_S_Phrase AdvP | Vprest_with_toVP_Phrase PP
Vprest_with_toVP_Phrase -> Vprest_with_toVP Pto VbeNP | Adv Vprest_with_toVP Pto VbeNP | Vprest_with_toVP Pto VbeNP AdvP | Vprest_with_toVP_Phrase PP
Vprest_with_toVP_Phrase -> Vprest_with_toVP Pto BE VpassP | Adv Vprest_with_toVP Pto BE VpassP | Vprest_with_toVP Pto BE VpassP AdvP | Vprest_with_toVP_Phrase PP

Vprest_with_toVP_Phrase -> Vprest_with_toVP Pto Vprest_with_NPtoVP_Phrase | Adv Vprest_with_toVP Pto Vprest_with_NPtoVP_Phrase | Vprest_with_toVP Pto Vprest_with_NPtoVP_Phrase AdvP | Vprest_with_toVP_Phrase PP


# verb for VP followed by NP to do  i.e. Nadia wanted Ross to jump
V_with_NPtoVP_Phrase -> Vpast_with_NPtoVP NobjP Pto VdoP | Adv Vpast_with_NPtoVP NobjP Pto VdoP | Vpast_with_NPtoVP NobjP Pto VdoP AdvP | V_with_NPtoVP_Phrase PP
V_with_NPtoVP_Phrase -> Vpast_with_NPtoVP NobjP Pto Vprest_with_NP_Phrase | Adv Vpast_with_NPtoVP NobjP Pto Vprest_with_NP_Phrase| Vpast_with_NPtoVP NobjP Pto Vprest_with_NP_Phrase AdvP | V_with_NPtoVP_Phrase PP
V_with_NPtoVP_Phrase -> Vpast_with_NPtoVP NobjP Pto Vprest_with_NP_NP_Phrase | Adv Vpast_with_NPtoVP NobjP Pto Vprest_with_NP_NP_Phrase | Vpast_with_NPtoVP NobjP Pto Vprest_with_NP_NP_Phrase AdvP | V_with_NPtoVP_Phrase PP
V_with_NPtoVP_Phrase -> Vpast_with_NPtoVP NobjP Pto Vprest_with_PP_Phrase | Adv Vpast_with_NPtoVP NobjP Pto Vprest_with_PP_Phrase | Vpast_with_NPtoVP NobjP Pto Vprest_with_PP_Phrase AdvP | V_with_NPtoVP_Phrase PP
V_with_NPtoVP_Phrase -> Vpast_with_NPtoVP NobjP Pto Vprest_with_NP_PP_Phrase | Adv Vpast_with_NPtoVP NobjP Pto Vprest_with_NP_PP_Phrase | Vpast_with_NPtoVP NobjP Pto Vprest_with_NP_PP_Phrase AdvP | V_with_NPtoVP_Phrase PP
V_with_NPtoVP_Phrase -> Vpast_with_NPtoVP NobjP Pto Vprest_with_toVP_Phrase | Adv Vpast_with_NPtoVP NobjP Pto Vprest_with_toVP_Phrase | Vpast_with_NPtoVP NobjP Pto Vprest_with_toVP_Phrase AdvP | V_with_NPtoVP_Phrase PP
V_with_NPtoVP_Phrase -> Vpast_with_NPtoVP NobjP Pto Vprest_with_S_Phrase | Adv Vpast_with_NPtoVP NobjP Pto Vprest_with_S_Phrase | Vpast_with_NPtoVP NobjP Pto Vprest_with_S_Phrase AdvP | V_with_NPtoVP_Phrase PP
V_with_NPtoVP_Phrase -> Vpast_with_NPtoVP NobjP Pto VbeNP | Adv Vpast_with_NPtoVP NobjP Pto VbeNP | Vpast_with_NPtoVP NobjP Pto VbeNP AdvP | V_with_NPtoVP_Phrase PP
V_with_NPtoVP_Phrase -> Vpast_with_NPtoVP NobjP Pto BE VpassP | Adv Vpast_with_NPtoVP NobjP Pto BE VpassP | Vpast_with_NPtoVP NobjP Pto BE VpassP AdvP | V_with_NPtoVP_Phrase PP
V_with_NPtoVP_Phrase -> Vpast_with_NPtoVP NobjP Pto Vprest_with_NPtoVP_Phrase | Adv Vpast_with_NPtoVP NobjP Pto Vprest_with_NPtoVP_Phrase | Vpast_with_NPtoVP NobjP Pto Vprest_with_NPtoVP_Phrase AdvP | V_with_NPtoVP_Phrase PP


Vprest_with_NPtoVP_Phrase -> Vprest_with_NPtoVP NobjP Pto VdoP | Adv Vprest_with_NPtoVP NobjP Pto VdoP | Vprest_with_NPtoVP NobjP Pto VdoP AdvP | Vprest_with_NPtoVP_Phrase PP
Vprest_with_NPtoVP_Phrase -> Vprest_with_NPtoVP NobjP Pto Vprest_with_NP_Phrase | Adv Vprest_with_NPtoVP NobjP Pto Vprest_with_NP_Phrase| Vprest_with_NPtoVP NobjP Pto Vprest_with_NP_Phrase AdvP | Vprest_with_NPtoVP_Phrase PP
Vprest_with_NPtoVP_Phrase -> Vprest_with_NPtoVP NobjP Pto Vprest_with_NP_NP_Phrase | Adv Vprest_with_NPtoVP NobjP Pto Vprest_with_NP_NP_Phrase | Vprest_with_NPtoVP NobjP Pto Vprest_with_NP_NP_Phrase AdvP | Vprest_with_NPtoVP_Phrase PP
Vprest_with_NPtoVP_Phrase -> Vprest_with_NPtoVP NobjP Pto Vprest_with_PP_Phrase | Adv Vprest_with_NPtoVP NobjP Pto Vprest_with_PP_Phrase | Vprest_with_NPtoVP NobjP Pto Vprest_with_PP_Phrase AdvP | Vprest_with_NPtoVP_Phrase PP
Vprest_with_NPtoVP_Phrase -> Vprest_with_NPtoVP NobjP Pto Vprest_with_NP_PP_Phrase | Adv Vprest_with_NPtoVP NobjP Pto Vprest_with_NP_PP_Phrase | Vprest_with_NPtoVP NobjP Pto Vprest_with_NP_PP_Phrase AdvP | Vprest_with_NPtoVP_Phrase PP
Vprest_with_NPtoVP_Phrase -> Vprest_with_NPtoVP NobjP Pto Vprest_with_toVP_Phrase | Adv Vprest_with_NPtoVP NobjP Pto Vprest_with_toVP_Phrase | Vprest_with_NPtoVP NobjP Pto Vprest_with_toVP_Phrase AdvP | Vprest_with_NPtoVP_Phrase PP
Vprest_with_NPtoVP_Phrase -> Vprest_with_NPtoVP NobjP Pto Vprest_with_S_Phrase | Adv Vprest_with_NPtoVP NobjP Pto Vprest_with_S_Phrase | Vprest_with_NPtoVP NobjP Pto Vprest_with_S_Phrase AdvP | Vprest_with_NPtoVP_Phrase PP
Vprest_with_NPtoVP_Phrase -> Vprest_with_NPtoVP NobjP Pto VbeNP | Adv Vprest_with_NPtoVP NobjP Pto VbeNP | Vprest_with_NPtoVP NobjP Pto VbeNP AdvP | Vprest_with_NPtoVP_Phrase PP
Vprest_with_NPtoVP_Phrase -> Vprest_with_NPtoVP NobjP Pto BE VpassP | Adv Vprest_with_NPtoVP NobjP Pto BE VpassP | Vprest_with_NPtoVP NobjP Pto BE VpassP AdvP | Vprest_with_NPtoVP_Phrase PP

Vprest_with_NPtoVP_Phrase -> Vprest_with_NPtoVP NobjP Pto Vprest_with_NPtoVP_Phrase | Adv Vprest_with_NPtoVP NobjP Pto Vprest_with_NPtoVP_Phrase | Vprest_with_NPtoVP NobjP Pto Vprest_with_NPtoVP_Phrase AdvP | Vprest_with_NPtoVP_Phrase PP
Vprest_with_NPtoVP_Phrase -> Vprest_with_NPtoVP NobjP Pto Vprest_with_toVP | Adv Vprest_with_NPtoVP NobjP Pto Vprest_with_toVP_Phrase | Vprest_with_NPtoVP NobjP Pto Vprest_with_toVP_Phrase AdvP | Vprest_with_NPtoVP_Phrase PP

V_with_NPtoVP_Phrase -> Vpast_with_NPtoVP NobjP Pto Vprest_with_toVP_Phrase | Adv Vpast_with_NPtoVP NobjP Pto Vprest_with_toVP_Phrase | Vprest_with_toVP_Phrase NobjP Pto Vprest_with_toVP_Phrase AdvP | V_with_NPtoVP_Phrase PP
V_with_NPtoVP_Phrase -> Vpast_with_NPtoVP NobjP Pto Vprest_with_NPtoVP_Phrase | Adv Vpast_with_NPtoVP NobjP Pto Vprest_with_NPtoVP_Phrase | Vprest_with_toVP_Phrase NobjP Pto Vprest_with_NPtoVP_Phrase AdvP | V_with_NPtoVP_Phrase PP


    # Lexicon starts from here
    

   
Nproper -> 'Nadia' | 'Ross' | 'Marseilles' | 'Google'
Nsubjpron -> 'I' | 'you' | 'he' | 'she' | 'they' | 'it' | 'we' | 'that'
Nobjpron -> 'me' | 'you' | 'him' | 'her' | 'them' | 'it' | 'us' | 'that'


N -> 'fur' | 'cat' | 'notebook' | 'park' | 'dog' | 'man' | 'statue' | 'school' | 'rutabaga' | 'boat' | 'eggplant' | 'elephant' | 'poodle' | 'cloth' | 'cheese' | 'help' | 'autoclave' | 'autopoiesis' | 'hovercraft' | 'menu'
P -> 'before' | 'after' | 'in' | 'with' | 'from' | 'to' | 'for' | 'onto' | 'on' |'of'
Adj -> 'tall' | 'long' | 'soft' | 'black' | 'big' | 'handsome'
Adv -> 'quickly' | 'slowly' | 'carefully' | 'suddenly' | 'immediately' | 'really' | 'always' | 'already' | 'before' | 'after' | 'here'
Det -> 'that' | 'a' | 'the' | 'my' | 'his' | 'her' | 'their' | 'its' | 'a' | 'an'

# model auxiliary verb
AuxMd -> 'will' | 'would' | 'shall' | 'should' | 'can' | 'could' | 'may' | 'might' | 'must'

SingularPerfect -> 'has'
PluralPerfect -> 'have'

PastPrefect -> 'had'

BE -> 'be'
BEpastp -> 'been'
BEprestp -> 'being'
BEpass -> 'am' | 'is' | 'was' | 'are' | 'were'


Vprest -> 'give' | 'find' | 'demand' | 'reward' | 'remind' | 'help' | 'want' | 'see' | 'win' | 'believe' | 'tell' | 'run' | 'arrive' | 'aspire' | 'leave' | 'shoot' | 'eat' | 'jump' | 'fondle' | 'bring' | 'be'
Vsingular -> 'gives' | 'finds' | 'demands' | 'rewards' | 'reminds' | 'helps' | 'wants' | 'sees' | 'wins' | 'believes' | 'tells' | 'runs' | 'arrives' | 'aspires' | 'leaves' | 'shoots' | 'eats' | 'jumps' | 'fondles' | 'brings' | 'comes'

Vprog -> 'giving' | 'finding' | 'demanding' | 'rewarding' | 'reminding' | 'helping' | 'wanting' | 'seeing' | 'winning' | 'believing' | 'telling' | 'running' | 'arriving' | 'leaving' | 'shooting' | 'eating' | 'jumping' | 'fondling' | 'bringing' | 'aspiring'
Vpass -> 'given' | 'found' | 'demanded' | 'rewarded ' | 'reminded' | 'helped' | 'wanted' | 'arrived' | 'seen' | 'won' | 'believed' | 'told' | 'kicked' | 'left' | 'aspired' | 'shot' | 'eaten' | 'fondled' | 'brought' | 'jumped'

VpastpSubj ->  'given' | 'won' | 'believed' | 'kicked' | 'left' | 'jumped' | 'shot' | 'run' | 'arrived' | 'eaten' | 'helped' | 'seen' | 'aspired' | 'fondled'
VpastpPassive -> 'given' | 'found' | 'demanded' | 'rewarded ' | 'reminded' | 'helped' | 'wanted' | 'seen'| 'won' | 'believed' | 'told' | 'kicked' | 'left' | 'aspired' | 'shot' | 'eaten' | 'fondled' | 'brought'

Vintr -> 'win' | 'won' | 'believe' | 'believed' | 'come' | 'leave' | 'left' | 'eat' | 'ate' | 'see' | 'saw' | 'arrive' | 'arrived' | 'shoot' | 'shot' | 'jump' | 'jumped' | 'run' | 'ran' | 'play' | 'played'

Pto -> 'to'

Vpast_with_NP -> 'demanded' | 'rewarded' | 'reminded' | 'won' | 'believed' | 'brought' | 'gave' | 'saw' | 'left' | 'told' | 'fondled' | 'wanted' | 'played' | 'found' | 'helped' | 'shot' | 'ate'
Vprest_with_NP -> 'demand' | 'reward' | 'remind' | 'win' | 'believe' | 'bring' | 'give' | 'see' | 'leave' | 'tell' | 'fondle' | 'want' | 'play' | 'find' | 'help' | 'shoot' | 'eat'

Vpast_with_NP_NP -> 'brought' | 'gave' | 'told' | 'found'
Vprest_with_NP_NP -> 'bring' | 'give' | 'tell' | 'find'

Vpast_with_PP -> 'was' | 'were' | 'jumped'
Vprest_with_PP -> 'be' | 'jump'

Vpast_with_NP_PP -> 'gave' | 'told' | 'rewarded' | 'brought' | 'reminded' | 'helped' | 'shot'
Vprest_with_NP_PP -> 'give' | 'tell' | 'reward' | 'bring' | 'remind' | 'help' | 'shoot'

Vpast_with_S -> 'reminded' | 'said' | 'believed' | 'found' | 'demanded'
Vprest_with_S -> 'remind' | 'say' | 'believe' | 'find' | 'demand'

Vpast_with_toVP -> 'wanted' | 'aspired' | 'demanded'
Vprest_with_toVP -> 'want' | 'aspire' | 'demand'

Vpast_with_NPtoVP -> 'wanted' | 'told'
Vprest_with_NPtoVP -> 'want' | 'tell'

Conj -> 'that'

    """)

    # test sentences stars
     sentences3_1 = [
        'Nadia left quickly',
        'the cat with the long soft black fur slowly ate',
        'black Nadia come with a notebook',

        'he played with her in the park',

        'the cat with the long soft black fur slowly ate in the school',
        'black big Nadia quickly come with a big black notebook from school',
        'my dog come with a statue from the park',
        'cat come with Nadia from school'
    ]

    bad_sentence3_1 = ['Nadia with the long soft fur slowly ate',
                     'Nadia suddenly left quickly',
                     'Nadia suddenly left quickly immediately',
                     ]
                     
     sentence3_2_adv = [
        'Nadia really had quickly run',
        'Nadia has really been kicked',
        'Nadia had really been quickly running',
        'Nadia really had been quickly being kicked',

        'Nadia is running quickly',
        'Nadia was being kicked quickly',
        'Nadia was quickly kicked',

        'Nadia really may run quickly',
        'Nadia may be quickly kicked',
        'Nadia will really be running quickly',
        'Nadia really may be quickly being kicked',

        'Nadia may really have quickly run',
        'Nadia may have been kicked quickly',
        'Nadia should really have been running quickly',
        'Nadia really may have been quickly being kicked',

    ]


    sentence3_2 = [
        'Nadia had run',
        'Nadia had been kicked',
        'Nadia had been running',
        'Nadia had been being kicked',

        'Nadia is running',
        'Nadia was being kicked',
        'Nadia was kicked',

        'Nadia may run',
        'Nadia may be kicked',
        'Nadia may be running',
        'Nadia may be being kicked',

        'Nadia may have run',
        'Nadia may have been kicked',
        'Nadia may have been running',
        'Nadia may have been being kicked',
    ]

    sentences3_2_pp = ['Nadia is running in the park quickly']

                     
    sentences3_3 = [
        'Nadia fondled the eggplant',
        'the handsome poodle brought Ross to the autoclave',
        'Nadia brought a cloth for the cheese',

        'they told Ross to jump onto the elephant',
        'she believed that Ross was already on the hovercraft',
        'she really wanted help',
        'she really aspired to help',
        'cheese was always on the menu',
        'the eggplant reminded Nadia of Ross'

    ]

    complex_sentence3_3 = [

        'he wanted tall Nadia to reward the cat with the soft eggplant in school',
        'Nadia said that he left',
        'Nadia said he left',
        'Nadia quickly wanted to run',
        'Nadia quickly wanted to run in the park',
        'Nadia jumped from the park to the park',
    ]

    bad_sentence3_3 = ['Nadia found',
                       'Ross brought to Nadia',
                       'Nadia told to jump onto the elephant',
                       'Nadia wanted to jumped',
                       'Nadia wanted slowly to run',
                       'Nadia wanted in the school to jump',
                        'it said',
                     ]
                     
    # want to be NP
    toBeNP = ['Nadia wanted to be a cat',
              'Nadia wanted him to want her to aspire to be a soft black cat',
              'Nadia wanted him to want her to aspire to be kicked in school',
              'Nadia wanted him to want to tell him to be shot in school',
              'Nadia wanted him to want her to want him to shoot the cat in school'
    ]
   
   # some general examples
    example = [
    'Nadia left immediately',
    'the cat with the long soft fur slowly ate',
    'she arrived',


    'Nadia will leave',
    'Nadia has left',
    'Nadia may have been leaving',

    'Nadia fondled the eggplant',
    'the handsome poodle brought Ross to the autoclave',
    'Nadia brought a cloth for the cheese',
    'they told her to jump onto the elephant',
    'she believed that Ross was already on the hovercraft',
    'she really wanted help',
    'she really aspired to help',
    'cheese was always on the menu',
    'the eggplant reminded Nadia of Ross',


    'Nadia rewarded the man with the eggplant',
    'Nadia won an elephant',
    'a rutabaga could have been demanded',
    'autopoiesis always reminded her of Marseilles',
    'I saw Nadia on a boat with my elephant',
    'Nadia was reminded',
    'an elephant had been being won',]

    example_bad = [
        'Nadia with the long soft fur slowly ate',
        'the cat with the tall her arrived',
        'they told to jump onto the elephant',
        'Nadia found',
        'Ross brought to him',
        'Nadia will left',
        'Nadia has could leave',
        'Nadia has had left',

    ]

    # UNgrammatical sentences but parsed successfully
    overgen = [
        'they has arrived',
        'he have been kicked',
        'they has been jumping',
        'he have left',
        'Nadia before saw him',
        'she come with a black black cat',

    ]

    # grammatical sentences but didn't parsed
    undergen = [

        'the cat has been jump onto the boat',
        'she could be a cat',
        'Nadia has been given a notebook',

        'a cat that is soft come slowly',
        'he could have bring that cat to her',
        'my cat Nadia slowly come',
        'I give you help to run quickly',
        'here I eat',
    ]


    for sent in example:
        sent = sent.split(" ")
        test(sent)