<<<<<<< HEAD
import math

limits = {1000:10, 500: 10, 200:10, 100: 10, 50: 10, 20: 10, 10: 10}

def collect(amount, nominals):
    if amount == 0 :
        return  dict()
    if not nominals:
        return
    
    current_nominal = nominals[0]
    avaible_notes = limits[current_nominal]
    notes_needed = math.floor(amount / current_nominal)
    number_of_notes = min(avaible_notes, notes_needed)
   
    for i in range(number_of_notes, -1, -1):
        result = collect(amount - i * current_nominal, nominals[1:])    
    
        if result  is not None:
            if i:
                result[current_nominal] = number_of_notes
                return result
            else:
                return result
    
def i_want_to_get(amount_required, limits):
    nominals = sorted(limits.keys(), reverse=1)
    return collect(amount_required, nominals)
    
print(i_want_to_get(260, limits))
=======
import math

limits = {1000:4, 500: 1, 200:4, 100: 0, 50: 1, 20: 1, 10: 5}

def collect(amount, nominals):
    if amount == 0 :
        return  dict()
    if not nominals:
        return
    
    current_nominal = nominals[0]
    avaible_notes = limits[current_nominal]
    notes_needed = math.floor(amount / current_nominal)
    number_of_notes = min(avaible_notes, notes_needed)
   
    for i in range(number_of_notes, -1, -1):
        result = collect(amount - i * current_nominal, nominals[1:])    
    
        if result  is not None:
            if i:
                result[current_nominal] = number_of_notes
                return result
            else:
                return result
    
def i_want_to_get(amount_required, limits):
    nominals = sorted(limits.keys(), reverse=1)
    return collect(amount_required, nominals)
    
print(i_want_to_get(1170, limits))
>>>>>>> 0c2b3f761926311d764006ec2609dbd063adb930
