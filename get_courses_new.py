import re
import copy
from Class import Class
from ClassList import ClassList
from Session import Session
from EquivalenceClassList import EquivalenceClassList
import csv

pattern1_str = "\s*(?P<crn>\d{5})\s+(?P<dept>[A-Z]{4})\s+(?P<course_number>\d{4}[A-Z]*)\s+(?P<section>\d+[A-Z]*)"
pattern1 = re.compile(pattern1_str)

pattern2_str = "\s+(?P<start_date>\d{2}\-[A-Z]{3})-\d{4}\s+(?P<end_date>\d{2}-[A-Z]{3}-\d{4})\s+(?P<days>[MTWRF]+)\s+(?P<start_time>\d{2}:\d{2}[ap]m)-(?P<end_time>\d{2}:\d{2}[ap]m)\D+\d{4}[A-z]*"
pattern2 = re.compile(pattern2_str)

class_list = ClassList()

current_class = None

#with open('banner_course_schedule.py') as f:
with open('html_classes_content2.txt') as f:
    
    for line in f:

        results1 = pattern1.match(line)
        results2 = pattern2.match(line)
        
        if results1 != None:
            if current_class != None:
                class_list.add_class(current_class)
            current_crn = results1.group('crn')
            current_dept = results1.group('dept')
            current_course_number = results1.group('course_number')
            current_section = results1.group('section')
            current_class = Class(current_crn, current_dept, current_course_number, current_section)
    
        elif results2 != None:
            
            new_session = Session(results2.group('days'), results2.group('start_time'), results2.group('end_time'), results2.group('start_date'), results2.group('end_date'))    
            current_class.add_session(new_session) 

# Don't forget to add the last class
class_list.add_class(current_class)
class_list.remove_no_sessions()
class_list.remove_specialized()
class_list.remove_a_session()

print(class_list)
print(len(class_list.classes))
#print(class_list.get_multiple_sessions())
print(class_list.session_dict)
#equiv_class_list = EquivalenceClassList()
#for a_class in class_list.classes:
#    copied_class = copy.deepcopy(a_class)
#    equiv_class_list.add_class(copied_class)
#print(equiv_class_list)
#print(len(equiv_class_list.classes))
#print(equiv_class_list.compressed_str())
#
#x=0
#for cl in class_list.classes:
#    print(cl.sessions[0])
#    x+=1
#    print(' ')
#print(x)
#len(cl_list)
#
#x=0
#new_cl_str_lei
#for cl in cl_str_list:
#    if cl.split()[0]=='M':
#        x+=1 
#x
#cl_str_list

#Read in the dictionary that represents the key (CRN) and the value (student ID)
#The purpose is to see students are taking two classes at the same exam time.
#Or we could build the exam schedule with this. 
reader = csv.reader(open('students_to_classes.csv', 'r'))
di = {}
for row in reader:
    print(row)
    if row!=[]:
        k, v = row
        di[k] = v


import networkx as nx

i = 0
cl_list = []
cl_str_list = []
for cl in class_list.classes:
    if str(cl.sessions[0]) not in cl_str_list:
        cl_list.append(cl.sessions[0])
        cl_str_list.append(str(cl.sessions[0]))
#print('Length of CL List:  ' + str(len(cl_list)))

my_graph = nx.Graph()
my_graph.add_nodes_from(cl_list)
for n1 in my_graph.nodes:
    for n2 in my_graph.nodes:
        if n1.does_session_overlap(n2):
            my_graph.add_edge(n1, n2)

print(len(my_graph.nodes))
print(len(my_graph.edges))

while len(my_graph.nodes) > 0:
    print('\nClique ' + str(i))
    max_num_sections = 0
    max_node = None
    
#    for node in my_graph.nodes:
#        if class_list.session_dict[str(node)] > max_num_sections:
#            max_num_sections = class_list.session_dict[str(node)]
#            max_node = node
            
    #print('Max Node:  ' + str(max_node))        
    #print('Max_Num_Sections:  ' + str(max_num_sections))
    
    cliques = nx.enumerate_all_cliques(my_graph)
    clique_number = nx.graph_clique_number(my_graph)
            
#    cliques = nx.cliques_containing_node(my_graph, max_node)
#    clique_number = nx.node_clique_number(my_graph, max_node)
#    print('Clique Number:  ' + str(clique_number))
    
    #print(len(clique.nodes))
    #print(len(clique.nodes[0]))
    #print(len(clique.edges))
    
#    for clique in cliques:
#        if len(clique) == clique_number:
#            num_sections = class_list.get_number_of_sections([str(x) for x in clique])
#            break
#    my_graph.remove_nodes_from(clique)
#    print(''.join([str(x)+' ' for x in clique]))
#    print('Number of Sections in Clique:  ' + str(class_list.get_number_of_sections([str(x) for x in clique])))  
##    print(len(my_graph.nodes))
#    i = i + 1

#Maximize # of sections in schedule. 
    max_num_sections = 0
    for clique in cliques:
        section_num = 0 
        for node in clique:
            section_num += class_list.session_dict[str(node)]
        if section_num > max_num_sections:
            max_num_sections = section_num
            max_clique = clique
    my_graph.remove_nodes_from(max_clique)
    print(''.join([str(x)+' ' for x in max_clique]))    
    print('Number of Sections in Clique:  ' + str(max_num_sections))  
    print('Clique Size:  ' + str(len(max_clique)))
    i = i + 1

#print(i)

'''
    max_clique = []
    max_sections = 0
    for clique in cliques:
        if len(clique) == clique_number:
            num_sections = class_list.get_number_of_sections([str(x) for x in clique])
            if num_sections > max_sections:
                max_clique = clique
                max_sections = num_sections
    my_graph.remove_nodes_from(max_clique)
    print(''.join([str(x)+' ' for x in max_clique]))
    print('Max Sections:  ' + str(max_sections))
'''

#print(class_list.session_dict['TR 12:15PM 01:30PM']) #get_number_of_sections(r"M 07:35PM 08:50PM"))
#print(class_list.session_dict['T 04:45PM 06:00PM']) #get_number_of_sections(r"M 07:35PM 08:50PM"))


#print(class_list.session_dict['T 03:45PM 04:35PM']) #get_number_of_sections(r"M 07:35PM 08:50PM"))
#for j in class_list.classes:
#    if str(j.sessions[0]) == 'T 03:45PM 04:35PM' or str(j.sessions[0]) == 'T 04:45PM 06:00PM':
#        print(j)
'''        
#first attempt with DiGraphs
my_graph = nx.DiGraph()
my_graph.add_nodes_from(class_list.classes)
for n1 in my_graph.nodes:
    for n2 in my_graph.nodes:
        if n1.does_intersect(n2):
            my_graph.add_edge(n1, n2)
print(len(my_graph.nodes))
print(len(my_graph.edges))
print(nx.number_connected_components(my_graph))
tc_graph = nx.transitive_closure(my_graph)
print(len(tc_graph.nodes))
print(nx.number_connected_components(tc_graph))
print(len(tc_graph.edges))
'''

#code for checking individual classes.
#print(class_list.session_dict['MW 09:00AM 10:15AM']) #get_number_of_sections(r"M 07:35PM 08:50PM"))
'''
Clique 2
MW 09:25AM 10:40AM W 08:00AM 10:30AM W 09:25AM 10:40AM MW 08:00AM 09:50AM MW 09:00AM 10:15AM 
Number of Sections in Clique:  54
Clique Size:  5
'''

