def studentmatchteacher(stu_subject, stu_lang, stu_otherlang, stu_year, stu_timezone):
    year_req=int(stu_year[2:len(year_req)])
    timezone_req=time_zone_to_int(stu_timezone)
    teacherlist=[]
    #filtering by most requirements
    for teacher in TeacherInfo.query.filter(db.and_(TeacherInfo.teacher_subject==stu_subject,
                                     db.or_(TeacherInfo.teacher_first_language==stu_lang,
                                            TeacherInfo.teacher_first_language==stu_otherlang))).all():
        teacherlist.append([0,teacher, teacher.id])
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
        
    return teacherlist

def time_zone_to_int(timezone):
    index=["utc","bst","cdt"].index(timezone)
    return [0,1,-5][index]

def year_range(lower,upper):
    lower=int(lower[2:len(lower)])
    upper=int(upper[2:len(upper)])
    if upper<lower:
        upper,lower=lower,upper
    return range(lower,upper+1)
    
studentmatchteacher("eng","eng","na","yr10","utc")
