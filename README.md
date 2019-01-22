# Final Exam Schedule Builder
The purpose of this program is to assist in building a final exam schedule. In particular, this program will group class times together that have a time conflict so that the rooms are guaranteed to overlap. 

To accomplish this, the program builds a graph with class times as vertices and there is an edge between two vertices if they share a class time. Then the program finds maximal cliques based on the number of courses. The program will then associate each clique with one of the main times and identify which cliques do not match one of the main times. For Dalton State College, the main times classes are held during the school year are 8-9:15am, 9:25-10:40am, 10:50am-12:05pm, 12:15-1:30pm, 1:40pm-2:55pm, 3:05-4:20pm, 4:45-6:00pm, 6:10-7:25-pm, and 7:35-8:50pm. Those times are grouped by Monday/Wednesday and Tuesday/Thursday. 

After making this association, the user must manually put class times into exam slots. Placing cliques into exam slots can be considerably variable. So much so, this is left as a manual process. For example, at Dalton State College, there were 32 cliques, yet there were only 24 times slots for those cliques. We put the cliques into the time slots that would cause the least conflicts. 

Some of the restrictions that Dalton State College abided by are listed below:
* If a clique contained a class that only met on Monday, then the entire clique met on Monday for their final exam.
* A clique can only be held on the days contained in that clique.
* The main time represented by a clique needs to be close to the final exam time schedule to that clique.
* There needs to be as few conflicts as possible.
* Since Final Exam week starts on Tuesday and ends on Monday, there needs to be as few as possible final exams on Monday. 

To run the code, download all of the files to one directory. Then execute the code in get_courses.py. All other files do not need editing unless you have more restrictions than the ones listed above. 

Note: If a course is listed as TBA, it is skipped. If a class is designated as an online class, it is skipped. 
