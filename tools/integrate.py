''' Approximates integral of a curve between two bounds '''
def integrate (lower_bound, upper_bound, func, accuracy = 500):
        
    ''' Gets subdomain size and initialises total variable '''
    subdomain_size = (upper_bound - lower_bound) / accuracy 
    total = 0  
    
    ''' Loops over each subdomain '''
    for i in range(1, accuracy):
        
        ''' Calculates current subdomain start and end points '''
        current_subdomain_end = lower_bound + (subdomain_size * i) 
        current_subdomain_start = current_subdomain_end - subdomain_size     
        
        ''' Sums each rectangle and triangle each iteration of the loop, and adds to the total area '''      
        total += ((current_subdomain_end - current_subdomain_start) * func(current_subdomain_end)) + \
            (0.5 * (current_subdomain_end - current_subdomain_start) * \
            (func(current_subdomain_start) - func(current_subdomain_end)))
            
    return total # Returns total 