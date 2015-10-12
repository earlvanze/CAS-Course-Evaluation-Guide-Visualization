class Report:
    class InstructorRating:
        def __init__(self, instructor = []):
            self.overall = instructor[0] #0,13
            self.informativity = instructor[1] #1,15
            self.organization = instructor[2] #2,17 
            self.fairness = instructor[3] #3,19
            self.effectiveness = instructor[4] #4,24
            self.recommendation = instructor[5] #5,66

            
    class CourseRating:
        def __init__(self, course = []):
            self.overall = course[0] #0,29
            self.objectivesClarity = course[1] #1,31
            self.objectivesAchievement = course[2] #2,33
            self.interesting = course[3] #3,35
            self.expectationsMet = course[4] #4,37
            self.workload = course[5] #5,41
            self.amtOfStudy = course[6] #6,43
            self.challenging = course[7] #7,45
            self.priorSubjectInterest = course[8] #7,48
            self.increasedSubjectKnowledge = course[9] #8,50
            self.recommendation = course[10] #9,68

    class RecLabRating:
        def __init__(self, rec = []):
            self.helpfulTA = rec[0] #0,55
            self.instrTAComm = rec[1] #1,58
            self.usefulness = rec[2] #2,61


    def __init__(self, evaluation = []):
        self.url = evaluation[0] #0,0
        self.season = evaluation[1] #1,1
        self.year = evaluation[2] #2,1
        self.title = evaluation[3] #3,2
        self.cid = evaluation[4] #4,3
        self.subject = evaluation[5] #5,4
        self.instructor = evaluation[6] #6,5
        self.numResponses = evaluation[7] #7,6
        self.totalStudents = evaluation[8] #8,6
        self.percentage = evaluation[9] #9,6
        self.instructorRating = self.InstructorRating(evaluation[10])
        self.courseRating = self.CourseRating(evaluation[11])
        self.recLabRating = self.RecLabRating(evaluation[12])

    def __str__(self):
        return self.url
