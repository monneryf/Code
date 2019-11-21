## 1. The Importance of Counting ##

n_outcomes <- 36
p_six_six <- (1/36)
p_not_five_five<- 1 - (1/36)



## 2. Extending The Rule of Product ##

total_outcomes <- (6^3) * 52
p_666_ace_diamonds <- 1 / total_outcomes
p_no_666_ace_diamonds <- 1 - p_666_ace_diamonds



## 3. A More Concrete Example ##

p_crack_4 <- 1 / (10^4)
p_crack_6 <- 1 / (10^6)



## 4. With Replacement vs Without Replacement ##

size_num_4 <- 10*9*8*7 
size_num_6 <- 10*9*8*7*6*5



## 5. Permutations ##

factorial<-function(n) {
    factor<-1
    for(i in 1:n) {
        factor<-factor*i
        }
    print(factor)
    }
    
permutations_1 <- factorial(6)
permutations_2 <- factorial(52)


## 6. More About Permutations ##

factorial <- function(n) {
    final_product <- 1
    for (i in 1:n) {
        final_product = final_product * i
    }
    return(final_product)
}


permutation <- function(n,k) {
    return(factorial(n) / factorial(n-k))
    }
    
perm_3_52 <- permutation(52,3)

perm_4_20 <- permutation(20,4)



## 7. Sometimes Order Doesn't Matter ##

factorial <- function(n) {
    final_product <- 1 
    for (i in 1:n) {
        final_product <- final_product * i
    }
    return(final_product)
}

permutation <- function(n, k) {
    return(factorial(n) / factorial(n - k))
}

combination <- function(n,k) {
    return(factorial(n) /(factorial(n-k)*factorial(k)))
           }

c <- permutation(52,5) / factorial(5)

p_aces_7 <- 1/c
           
c_lottery <- permutation(49,6) / factorial(6)

p_big_prize <- 1 / c_lottery
           
           
           

## 8. Combination Notation ##

factorial <- function(n) {
    final_product <- 1 
    for (i in 1:n) {
        final_product <- final_product * i
    }
    return(final_product)
}

combination <- function(n,k) {
    return(factorial(n) /(factorial(n-k)*factorial(k)))
           }

c_18 <- combination(34, 18)

p_Y <- 1/c_18
p_non_Y <- 1 - p_Y


