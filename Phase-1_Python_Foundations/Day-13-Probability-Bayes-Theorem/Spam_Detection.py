#  Bayes Theorem
# P(A|B) = P(B|A) * P(A) / P(B)


p_Spam = 0.2
p_offer_given_spam = 0.7

p_normal = 0.8
p_offer_given_normal = 0.1


# p(spam) = 0.2
# p(offer/spam) = 00.7
# p(normal) = 0.8
# p(offer/normal) = 0.1
# want => p(spam/offer)


# need = p(offer)
# Using total probability
p_offer = ( 
    p_offer_given_spam * p_Spam  +
    p_offer_given_normal * p_normal
)


# Now bayes probability:
p_spam_given_offer = (p_offer_given_spam * p_Spam) / p_offer

print("P(Spam | Offer):",p_spam_given_offer)