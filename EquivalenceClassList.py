from EquivalenceClass import EquivalenceClass

class EquivalenceClassList:
    
    def __init__(self):
        self.classes = []
        
    def add_class(self, a_class):
        intersects = False
        for bucket in self.classes:
            if all([a_class.does_intersect(stuff) for stuff in bucket.eq_class]):
                bucket.add_class(a_class)
                return
        new_class = EquivalenceClass()
        new_class.add_class(a_class)
        self.classes.append(new_class)
        
    def __str__(self):
        out = ''
        i = 0
        for bucket in self.classes:
            out = out + 'Class ' + str(i) + '\n'
            out = out + str(bucket) + '\n'
            i = i + 1
        return out
    
    def compressed_str(self):
        out = ''
        i = 0
        for bucket in self.classes:
            out = out + 'Class ' + str(i) + '\n'
            out = out + bucket.compressed_str() + '\n'
            i = i + 1
        return out        
        
                
        