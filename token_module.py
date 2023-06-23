#
import math
import pickle
from datetime import datetime

class Token:
    def __init__(self):
        self.quality_of_data = None
        self.keys = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.catastrofic_loss = None 
        self.comments = []
        self.weights = None
        self.tensors = None
        self.bin_name = None

    @staticmethod
    def calculate_jaccard_distance(set1, set2):
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        jaccard_distance = 1 - (intersection / union)
        return jaccard_distance

    @staticmethod
    def calculate_sum_of_smallest_jaccard_distances(file_path):
        def read_tensors_from_file(file_path):
            tensors = []
            with open(file_path, 'r') as file:
                for line in file:
                    tensor = set(map(int, line.strip().strip('[]').split(',')))
                    tensors.append(tensor)
            return tensors

        tensors = read_tensors_from_file(file_path)
        smallest_distances = []
        for i in range(len(tensors) - 1):
            smallest_distance = 1.0  # Initialize with maximum value
            for j in range(i + 1, len(tensors)):
                jaccard_distance = Token.calculate_jaccard_distance(tensors[i], tensors[j])
                smallest_distance = min(smallest_distance, jaccard_distance)
            smallest_distances.append(smallest_distance)

        sum_of_smallest_distances = sum(smallest_distances)
        return sum_of_smallest_distances

    def calculate_and_save_sum_of_smallest_jaccard_distances(self, file_path):
        result = self.calculate_sum_of_smallest_jaccard_distances(file_path)
        self.quality_of_data = result


    #add here the matrix calcualatiion to caluctale catastrofhic loss
    @staticmethod
    def read_matrix_from_file(file_path):
        matrix = []
        with open(file_path, 'r') as file:
            for line in file:
                tensor = list(map(int, line.strip().strip('[]').split(',')))
                matrix.append(tensor)
        return matrix

    @staticmethod
    def mean_vector(mat):
        rows = len(mat)  # Number of rows in the matrix
        cols = len(mat[0])  # Number of columns in the matrix

        mean_vector = []  # Initialize an empty list for the mean vector

        for i in range(cols):
            col_sum = 0  # Accumulate the sum of values in the current column

            for j in range(rows):
                col_sum += mat[j][i]

            mean = col_sum / rows  # Calculate the mean value for the current column
            mean_vector.append(mean)  # Add the mean value to the mean vector

        return mean_vector

    def calculate_and_print_mean_vector(self, file_path):
        matrix = self.read_matrix_from_file(file_path)
        result = self.mean_vector(matrix)
        self.catastrofic_loss=result
        print("used as catastrific loss check, Mean vector:", result)



    #add keys for the smart contracts (keep 10 max)
    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

    def update_keys(self, new_prime):
        if self.is_prime(new_prime):
            self.keys.append(new_prime)  # Add the new prime number to the keys list
            if len(self.keys) > 10:
                self.keys = self.keys[1:]  # Remove the oldest key if the list exceeds 10 elements
            print("Updated keys:", self.keys)
        else:
            print("The provided number is not prime. Skipping the update.")

    #add zipping
    #done in diff libs
    
    #add the comments:
    def add_comment(self, comment):
        self.comments.append(comment)
    
    def update_comments(self):
        while True:
            comment = input("Enter a comment (or 'q' to quit): ")
            if comment == 'q':
                break
            self.add_comment(comment)


    #add seriliaztion and binaries tokenizations
    def serialize(self):
        filename = f"token_{self.keys}_{datetime.now().strftime('%Y%m%d%H%M%S')}.bin"
        self.bin_name=filename
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print("Token object serialized and saved as", filename)

    @staticmethod
    def deserialize(filename):
        with open(filename, 'rb') as file:
            token = pickle.load(file)
        return token


'''
# Create an instance of the Token class
token2 = Token()

# File path of the tensors file
file_path = "tensors.txt"

# Calculate and save the sum of the smallest Jaccard distances
token2.calculate_and_save_sum_of_smallest_jaccard_distances(file_path)

# Access the quality_of_data attribute and print the result
print("Quality of data:", token2.quality_of_data)
'''