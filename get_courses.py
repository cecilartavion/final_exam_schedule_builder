import re
import copy
from Class import Class
from ClassList import ClassList
from Session import Session
from EquivalenceClassList import EquivalenceClassList

#Patterns to match using regex. These patterns are likely to be school specific. Dalton
# State College uses banner.
pattern1_str = "(?P<crn>\d{5})\s+(?P<dept>[A-Z]{4})\s+(?P<course_number>\d{4}[A-Z]*)\s+(?P<section>\d+[A-Z]*)"
pattern1 = re.compile(pattern1_str)

#More patterns to match using regex. These look for the start and end dates/times
# that appear for the classes. 
pattern2_str = "\s+(?P<start_date>\d{2}\-[A-Z]{3})-\d{4}\s+(?P<end_date>\d{2}-[A-Z]{3}-\d{4})\s+(?P<days>[MTWRF]+)\s+(?P<start_time>\d{2}:\d{2}[ap]m)-(?P<end_time>\d{2}:\d{2}[ap]m)\D+\d{4}[A-z]*"
pattern2 = re.compile(pattern2_str)

class_list = ClassList()

current_class = None

#banner_course_schedule is where you would copy past all of the code for the 
# courses so that this program can peek inside and grab the patterns that
# represent the classes. Be sure to copy paste all classes you want to
# build a final exam schedule into one file. 
with open('banner_course_schedule.py') as f:
    
    for line in f:
        #Grab the lines that match the pattern. They patterns come in pairs.
        results1 = pattern1.match(line)
        results2 = pattern2.match(line)
        
        #If results1 has something, continue.
        if results1 != None:
            #If current_class has something, then start building the class.
            if current_class != None:
                class_list.add_class(current_class)
            #Add the crn number to the current class.
            current_crn = results1.group('crn')
            #Add the department 4-letter code to the current class.
            current_dept = results1.group('dept')
            #Add the course number to the current class.
            current_course_number = results1.group('course_number')
            #Add the section number to the current class.
            current_section = results1.group('section')
            #Build the current class
            current_class = Class(current_crn, current_dept, current_course_number, current_section)
        #IF results1 was empty but results2 was not, build a new session.
        elif results2 != None:
            #Construct the session using the days, start time, end time, start
            # date, and end date.
            new_session = Session(results2.group('days'), results2.group('start_time'), results2.group('end_time'), results2.group('start_date'), results2.group('end_date'))    
            #Build current class.
            current_class.add_session(new_session) 

# Don't forget to add the last class
class_list.add_class(current_class)
class_list.remove_no_sessions()
class_list.remove_specialized()
class_list.remove_a_session()

'''
To see more details about the class list that was collected, use the commands.

class_list.classes

You can also pull individual classes and check out more details by using the 
following commands.

for a_class in class_list.classes:
    a_class.crn #Gives CRN for a class
    a_class.dept #Gives the department number for a class
    a_class.course_number #Gives the course number for a class
    a_class.section #Gives the section number for a class
    a_class.sessions[0] #Gives the session time for a class
'''

#print(class_list)
#print(len(class_list.classes))
#print(class_list.get_multiple_sessions())
#print(class_list.session_dict)
#equiv_class_list = EquivalenceClassList()
#for a_class in class_list.classes:
#    copied_class = copy.deepcopy(a_class)
#    equiv_class_list.add_class(copied_class)
#print(equiv_class_list)
#print(len(equiv_class_list.classes))
#print(equiv_class_list.compressed_str())

#x=0
#for cl in class_list.classes:
#    print(cl.sessions[1])
#    x+=1
#    print(' ')
#print(x)
#len(cl_list)
#



import networkx as nx

#The following code will build the vertex set of the graph we will use to 
# build the blocks of time for the final exam schedule
i = 0
cl_list = []
cl_str_list = []
for cl in class_list.classes:
    if str(cl.sessions[0]) not in cl_str_list:
        cl_list.append(cl.sessions[0])
        cl_str_list.append(str(cl.sessions[0]))
#print('Length of CL List:  ' + str(len(cl_list)))

'''
After the code above is evaluated, it is relatively easy to examine the data
in detail using commands such as the following.

x=0
for cl in cl_str_list:
    if cl.split()[0]=='F':
        #Print the class times that are on Friday.
        print(cl)
'''

#Build the graph and its edges using the following code.
my_graph = nx.Graph()
my_graph.add_nodes_from(cl_list)
for n1 in my_graph.nodes:
    for n2 in my_graph.nodes:
        if n1.does_session_overlap(n2):
            my_graph.add_edge(n1, n2)

print(len(my_graph.nodes))
print(len(my_graph.edges))
clique_collection = []
clique_course_list = []

#In the following while loop, we will find maximal cliques that fit a certain 
# criteria. In the current case, we are build the cliques by maximizing
# the number of classes in each clique. There is suppressed code to 
# maximize using the number of unique session times.
while len(my_graph.nodes) > 0:
    print('\nClique ' + str(i))
    max_num_sections = 0
    max_node = None

    #for node in my_graph.nodes:
    #    if class_list.session_dict[str(node)] > max_num_sections:
    #        max_num_sections = class_list.session_dict[str(node)]
    #        max_node = node
    
    
    #print('Max Node:  ' + str(max_node))        
    #print('Max_Num_Sections:  ' + str(max_num_sections))
    
    cliques = nx.enumerate_all_cliques(my_graph)
    clique_number = nx.graph_clique_number(my_graph)
            
    #cliques = nx.cliques_containing_node(my_graph, max_node)
    #clique_number = nx.node_clique_number(my_graph, max_node)
    #print('Clique Number:  ' + str(clique_number))
    
    #print(len(clique.nodes))
    #print(len(clique.nodes[0]))
    #print(len(clique.edges))
    
    #for clique in cliques:
    #    if len(clique) == clique_number:
    #        num_sections = class_list.get_number_of_sections([str(x) for x in clique])
    #        break
    #my_graph.remove_nodes_from(clique)
    #print(''.join([str(x)+' ' for x in clique]))
    #print(len(my_graph.nodes))
    #i = i + 1
    
    for clique in cliques:
        if int(class_list.get_number_of_sections([str(x) for x in clique])) > max_num_sections:
            max_num_sections = int(class_list.get_number_of_sections([str(x) for x in clique]))
            max_node = clique
    clique_collection = clique_collection + [[str(x)+' ' for x in max_node]]
    my_graph.remove_nodes_from(max_node)
    print(''.join([str(x)+' ' for x in max_node]))
    clique_course_list.append([str(x) for x in max_node])
#    
#    for clique in cliques:
#        if len(clique) == clique_number:
#            my_graph.remove_nodes_from(clique)
#            print(''.join([str(x)+' ' for x in clique]))    
#            break
    print('Number of Sections in Clique:  ' + str(class_list.get_number_of_sections([str(x) for x in max_node])))  
    print('Clique Size:  ' + str(len(max_node)))
    i = i + 1

print(i)

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

#print(class_list.session_dict['T 03:45PM 04:35PM']) #get_number_of_sections(r"M 07:35PM 08:50PM"))
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


#The normal_times list the typical class times on Monday/Wednesday and
# Tuesday/Thursday. That way, it would be easier to slot the cliques into
# the final exam times manually. 
normal_times = [['08:00AM','09:15AM'],['09:25AM','10:40AM'],['10:50AM','12:05PM'],
                ['12:15PM','01:30PM'],['01:40PM','02:55PM'],['03:05PM','04:20PM'],
                ['04:45PM','06:00PM'],['06:10PM','07:25PM'],['07:35PM','08:50PM']]
days = []
times = []
missed_days = []
missed_times = []
clique_collection[0][0].split()[0]
num_classes = []
i = 0
for clique in clique_collection:
    new_days = False
    new_times = False
    i += 1
    for cl in clique:
        #If the class only meets on one day and does not meet on Friday, add it
        # the list of classes.
        if len(cl.split()[0])==1 and new_days==False and cl.split()[0]!= 'F':
            days.append(cl.split()[0])
            new_days = True
        #If the class meets at one of the normal times, add it to the list of
        # classes. 
        if [cl.split()[1],cl.split()[2]] in normal_times and new_times == False:
            times.append([cl.split()[1],cl.split()[2]])
            new_times = True
    
    #If we were unable to find a place for the class, put it in the set of 
    # missing classes.
    if new_days == False:
        missed_days.append(clique)
    #If we were unable to find a place for the class, put it in the set of 
    # missing classes.
    if new_times == False:
        missed_times.append(clique)
    if new_days == True and new_times == False:
        days = days[:-1]
        missed_days.append(clique)
    if new_days == False and new_times == True:
        times = times[:-1]
        missed_times.append(clique)

#Print the days and times that were slotted into a regular time slot
print('Days/times:',[x for x in zip(days,times)])
#Print the days and times that were not slotted into a regular time slot.
print('Missed Days/:',[x for x in zip(missed_days,missed_times)])

#Build the normal time blocks
normal_time_blocks = [[a]+b for a,b in zip(days,times)]
normal_time_blocks 

#To see the list of course times in each clique, print the following line.
print(clique_course_list)

for session in normal_time_blocks:
    if session[0] == 'R':
        print(session)