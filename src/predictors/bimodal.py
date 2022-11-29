class BimodalPredictor:
    
    def __init__(self, index_size):
        self.index_size = index_size
        self.table = [0] * (2 ** index_size)
        
    def predict_branch(self, actual_result, pc_addresss, taken) -> dict:
        actual_result['branches'] += 1
        is_taken = False
        index = pc_addresss & ((2 ** self.index_size) - 1)
        
        if (self.table[index] >= 2):
            is_taken = True
            
        if is_taken and taken:
            actual_result['correctly_taken'] += 1
            self.table[index] = 3
        elif is_taken and not taken:
            actual_result['incorrectly_taken'] += 1
            self.table[index] -= 1
        elif not is_taken and taken:
            actual_result['incorrectly_untaken'] += 1
            self.table[index] += 1
        else:
            actual_result['correctly_untaken'] += 1
            self.table[index] = 0

        return actual_result