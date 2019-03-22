import nltk

hypothesis = ['This', 'is', 'cat']
reference = ['This', 'is', 'a', 'cat']
references = [reference] # list of references for 1 sentences.
list_of_references = [references] # list of references for all sentences in corpus.
list_of_hypotheses = [hypothesis] # list of hypotheses that corresponds to list of references.
cb = nltk.translate.bleu_score.corpus_bleu(list_of_references, list_of_hypotheses)
print("corpus_bleu(list_of_references, list_of_hypotheses) : {}".format(cb))

# 0.6025~

sb = nltk.translate.bleu_score.sentence_bleu(references, hypothesis)
print("sentence_bleu(references, hypothesis) : {}".format(sb))

# 0.6025~
