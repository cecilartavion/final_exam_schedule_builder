# Final Exam Schedule Builder
The purpose of this program is to assist in building a final exam schedule. In particular, this program will group class times together so there are no conflicts in assigning rooms. 

To accomplish this, the program builds a graph with unique class times as vertices and an edge between two vertices if the vertices overlap in some amount of class time and in the day of the week as well. For example, a class that meets at 9:25am-10:50am on Monday and Wednesday and a class that meets at 9:30am-11:30am on Wednesday only will be joined by an edge in our graph. On the other hand, a class that meets at 9:25am-10:50am on Monday and Wednesday and a class that meets 9:25am-10:50am Tuesday and Thursday will NOT be joined by an edge in our graph. 

Then the program finds maximal cliques and chooses the clique with the largest number of classes that meet at the times represented by the clique. After all of the cliques are chosen, the program will associate each clique with one of the main class times for Dalton State College and identify which cliques do not match any of the main times. For Dalton State College, the main times classes are held during the school year are 8-9:15am, 9:25-10:40am, 10:50am-12:05pm, 12:15-1:30pm, 1:40pm-2:55pm, 3:05-4:20pm, 4:45-6:00pm, 6:10-7:25-pm, and 7:35-8:50pm. Those times are grouped by Monday/Wednesday and Tuesday/Thursday. 

Placing cliques into final exam slots can be considerably variable. So much so, this is left as a manual process. For this reason, after associating the cliques with the normal operating times of classes, the user must manually put class times into exam slots. As an example of the variability, at Dalton State College, there were 32 cliques during the Spring 2019 semester, yet we were only allowed 24 final exam time slots to place these cliques. Clearly, there will be some overlap. So we put the cliques into the time slots that would cause the least amount of conflicts. 

Some of the restrictions that Dalton State College abides by are listed below:
* If a clique contains a class that only meets on Monday, then the entire clique must have a final exam on Monday.
* The normal class time that is associated with a clique (e.g. 9:25am-10:50am Monday) needs to be close to the final exam time schedule to that clique (e.g. 8:00am-10:00am on Monday, 8:00am-10:00am Wednesday, 10:15am-12:15pm Monday, or 10:15am-12:15pm Wednesday). This restriction is not required but is highly desired. 
* There needs to be as few room conflicts as possible. Preferably, there should be no room conflicts, but in our example, that was not possible.
* Since the Final Exam week starts on Tuesday and ends on Monday for Dalton State College and we need to report the final grades for graduating students by Friday, there needs to be as few final exams as possible on Monday so that instructors do not have to reschedule many of their exams. 

To run the code, download all of the files into one directory. Then execute the code in get_courses.py. All other files do not need to be edited unless your restrictions are vastly different than the ones explained above. 

Note: If a course is listed as TBA, it is skipped. If a class is designated as an online class, it is skipped. Since we are building cliques, all classes in a clique will overlap at exactly the same time, so there is no way they can meet in the same room. This property allows all of the classes contained in a clique to hold their final exams at the same time.
