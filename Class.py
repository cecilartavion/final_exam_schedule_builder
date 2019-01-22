class Class:
    
    def __init__(self, crn, dept, course_number, section):
        self.crn = crn
        self.dept = dept
        self.course_number = course_number
        self.section = section
        self.sessions = []
        
    def add_session(self, session):
        self.sessions.append(session)
        self.sessions.sort()
        
    def __str__(self):
        first_line = self.crn + ' ' + self.dept + ' ' + self.course_number + ' ' + self.section + '\n'
        return first_line + str(self.sessions[0])
    
    def does_intersect(self, other):
        return self.sessions[0].does_session_overlap(other.sessions[0])
            
            
        