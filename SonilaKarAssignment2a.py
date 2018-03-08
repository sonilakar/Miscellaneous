import math

# definie class similarity
class similarity:
    
    # Class instantiation 
    def __init__ (self, ratingP, ratingQ):
        self.ratings1 = ratingP
        self.ratings2 = ratingQ

    # Minkowski Distance between two vectors
    def minkowski(self, r):
    
        distance = 0  
        match_counter = 0 
        for item in self.ratings1.keys():
            if item in self.ratings2.keys():
                x = self.ratings1[item]
                y = self.ratings2[item]
                distance += pow(abs(x - y), r)
                match_counter = match_counter + 1
        if match_counter > 0:
            return round(pow(distance,1/r),4)
        else:
                return -1
    # Pearson Correlation between two vectors
    def pearson(self):
            
            pq_sum = 0
            p_sum = 0
            q_sum = 0
            p2_sum = 0
            q2_sum = 0
            match_counter = 0 
    
            for item in self.ratings1.keys():
                if item in self.ratings2.keys():
                    pq_sum = (self.ratings1[item]*self.ratings2[item]) + pq_sum
                    p_sum = self.ratings1[item] + p_sum
                    q_sum = self.ratings2[item] + q_sum
                    p2_sum = math.pow(self.ratings1[item],2) + p2_sum
                    q2_sum = math.pow(self.ratings2[item],2) + q2_sum
        
                    match_counter = match_counter + 1
        
            if match_counter > 0:
                numerator = pq_sum - (p_sum*q_sum)/match_counter
    
                denom_p = (p2_sum - (math.pow(p_sum,2))/match_counter)
                denom_p_sqrt = math.sqrt(denom_p)
                denom_q = (q2_sum - (math.pow(q_sum,2))/match_counter)
                denom_q_sqrt = math.sqrt(denom_q)
        
                denominator = denom_p_sqrt*denom_q_sqrt
        
                pearson_corr = round(numerator/denominator, 4)
        
                return pearson_corr
            else:
                return -2

# user ratings
UserPRatings = {'Motorola':8, 'LG':5, 'Sony':1, 'Apple':1, 'Samsung':5, 'Nokia':7}
UserQRatings = {'Apple':7, 'Samsung':1, 'Nokia':4, 'LG':4, 'Sony':6, 'Blackberry':3}

#To test negative scenario when no match found use these as inputs instead of above.                
#UserPRatings = {'A':8, 'B':5, 'C':1, 'D':1, 'E':5, 'F':7}
#UserQRatings = {'G':7, 'H':1, 'I':4, 'J':4, 'K':6, 'L':3}

# creating an instance of class and calling the class methods

myobj = similarity(UserPRatings, UserQRatings)
man_dist = myobj.minkowski(1) #calculate manhattan distance
euc_dist = myobj.minkowski(2) #calculate euclidean distance
min_dist = myobj.minkowski(3) #calculate minkowski distance
p_corr = myobj.pearson()      #calculate pearson correlation 

# print output

print()
print("For the following two sets of phone user ratings:")
print()
print(UserPRatings)
print()
print(UserQRatings)
print()
if man_dist == -1:
    print("No matching keys found. Cannot calculate Manhattan Distance.")
else:
    print("The Manhattan Distance is:", man_dist)
print()
if euc_dist == -1:
    print("No matching keys found. Cannot calculate Euclidean Distance.")
else:
    print("The Euclidean Distance is:", euc_dist)
print()
if min_dist == -1:
    print("No matching keys found. Cannot calculate Minkowski Distance.")
else:
    print("The Minkowski Distance is:", min_dist)
print()
if p_corr == -2:
    print("No matching keys found. Cannot calculate Pearson Correlation.")
else:
    print("The Pearson Correlation is:", p_corr)