class ClassList():
    
    def __init__(self):
        self.classes = []
        self.session_dict = dict() 
        
    def add_class(self, a_class):
        self.classes.append(a_class)
        if len(a_class.sessions) > 0:
            if str(a_class.sessions[0]) not in self.session_dict:
                self.session_dict[str(a_class.sessions[0])] = 1
            else:
                self.session_dict[str(a_class.sessions[0])] = self.session_dict[str(a_class.sessions[0])] + 1
    
    def remove_a_session(self):
        self.classes = [x for x in self.classes if 'MAR' not in str(x.sessions[0])]
        
    def remove_no_sessions(self):
        self.classes = [x for x in self.classes if len(x.sessions) > 0]
        
    def remove_specialized(self):    
        self.classes = [x for x in self.classes if x not in ['PHED']]
    
    def get_number_of_sections(self, s_list):
        new_dict = {key:self.session_dict[key] for key in s_list}
        return sum(new_dict.values())
    
    def get_multiple_sessions(self):
        dups = ClassList()
        for cl in self.classes:
            if len(cl.sessions) > 1:
                dups.add_class(cl)
        return dups
    
    def __str__(self):
        out = ''
        for i in self.classes:
            out = out + str(i) + '\n'
        return out