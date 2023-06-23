#demo
from token_module import Token 


test_token=Token()
test_token.calculate_and_save_sum_of_smallest_jaccard_distances("tensors.txt")
test_token.calculate_and_print_mean_vector("tensors.txt")

print("quality score: "+str(test_token.quality_of_data))
print(test_token.catastrofic_loss)
