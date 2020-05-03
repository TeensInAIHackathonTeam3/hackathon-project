def studentmatchteacher(stu_subject, stu_lang, stu_otherlang, stu_year, stu_timezone):
    year_req=int(stu_year[2:len(year_req)])
    timezone_req=time_zone_to_int(stu_timezone)
    teacherlist=[]
    #filtering by most requirements
    for teacher in TeacherInfo.query.filter(db.and_(TeacherInfo.teacher_subject==stu_subject,
                                     db.or_(TeacherInfo.teacher_first_language==stu_lang,
                                            TeacherInfo.teacher_first_language==stu_otherlang))).all():
        teacherlist.append([0,teacher])
    #filtering by year
    for teacher in teacherlist:
        if not year_req in year_range(teacher[1].teacher_min_year,teacher[1].teacher_max_year):
            teacherlist.remove(teacher)
    #ranking by score
    for teacher in teacherlist:
        teacher_timezone = time_zone_to_int(teacher[1].teacher_timezone)
        # -n squared points for each hour offset
        teacher[0] -= (timezone_req - teacher_timezone) **2
        # lessons in a language a student is fluent in but is not their main language
        if teacher[1].teacher_first_language == stu_otherlang:
            teacher[0]-= 15
    teacherlist.sort()
    teacherlist.reverse()
    data_out=[]
    for teacher in teacherlist:
        data_out.append(
            {
                'name': "{} {}".format(teacher[1].teacher_first_name,teacher[1].teacher_last_name) ,
                'subject' : abbreviation_to_name(teacher[1].teacher_subject),
                'timezone': teacher[1].teacher_timezone.upper(),
                'language': abbreviation_to_name(teacher[1].teacher_first_language)
                })   
    return data_out

def time_zone_to_int(timezone):
    index=["utc","bst","cdt"].index(timezone)
    return (0,1,-5)[index]

def abbreviation_to_name():
    index=("mat","eng","phy","che","bio","fre","spa")
    return("Maths","English","Physics","Chemistry","Biology","French","Spanish")[index]

def year_range(lower,upper):
    lower=int(lower[2:len(lower)])
    upper=int(upper[2:len(upper)])
    if upper<lower:
        upper,lower=lower,upper
    return range(lower,upper+1)
def hardcoded_student_match_teacher():
    student=StudentInfo.query.filter(StudentInfo.id==3).first()
    
    return studentmatchteacher(student.student_subject, student.student_first_language,
                               student.student_other_language, student.student_year_group,
                               student.student_timezone)

#student_match_teacher("eng","eng","na","yr10","utc")
