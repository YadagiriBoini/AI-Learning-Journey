#  Bayes Theorem
# P(A|B) = P(B|A) * P(A) / P(B)

p_B_given_A = 0.7
p_A = 0.3
p_B = 0.5

bayes_probability = p_B_given_A*p_A / p_B

print("P(A|B):",bayes_probability)