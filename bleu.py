#https://machinelearningmastery.com/calculate-bleu-score-for-text-python/
from nltk.translate.bleu_score import sentence_bleu
"""
# Sentence BLEU score
from nltk.translate.bleu_score import sentence_bleu
reference = [['this', 'is', 'a', 'test'], ['this', 'is', 'test']]
#reference = [['this', 'is', 'test']]
candidate = ['this', 'is', 'a', 'test']
score = sentence_bleu(reference, candidate)
print(score)
"""

# Corpus BLUE score
# two references for one document
from nltk.translate.bleu_score import corpus_bleu
references = [['this', 'is', 'the', 'test']]
hypothesis = ['this', 'is', 'the', 'test']
#candidates = [['this', 'this', 'this', 'this']]
score = sentence_bleu(references, hypothesis)
print('Corpus BLEU score is ', score)

"""

# Individual N-Gram score
# 1-gram individual BLEU
reference = [['this', 'is', 'small', 'test']]
candidate = ['this', 'is', 'a', 'test']
score = sentence_bleu(reference, candidate, weights=(1, 0))
print('Individual 1-gram: %f' % score)

# n-gram individual BLEU
reference = [['this', 'is', 'small', 'test']]
candidate = ['this', 'is', 'a', 'test']
print('Individual 2-gram: %f' % sentence_bleu(reference, candidate, weights=(0, 1, 0)))
"""

"""
# 4-gram cumulative BLEU
reference = [['this', 'is', 'small', 'test']]
candidate = ['this', 'is', 'a', 'test']
score = sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25))
print("%0.4f"%score)
"""



