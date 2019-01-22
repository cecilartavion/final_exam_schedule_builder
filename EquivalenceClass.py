class EquivalenceClass:
    
    def __init__(self):
        self.eq_class = []
        
    def add_class(self, a_class):
        self.eq_class.append(a_class)
        
    def __str__(self):
        out = ''
        for i in self.eq_class:
            out = out + str(i) + '\n'
        return out
    
    def compressed_str(self):
        out = ''
        for a_class in self.eq_class:
            if str(a_class.sessions[0]) not in out: 
                out = out + str(a_class.sessions[0]) + '\n'
        return out