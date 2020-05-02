def studentmatchteacher(stu_subject, stu_lang, stu_otherlang, stu_year, stu_timezone):
    teacherlist=[]
    for teacher in TeacherInfo.query.filter(db.and_(TeacherInfo.teacher_subject==stu_subject,
                                     db.or_(TeacherInfo.teacher_first_language==stu_lang,
                                            TeacherInfo.teacher_first_language==stu_otherlang))).all():
        teacherlist.append([0,teacher, teacher.id])
        return teacherlist

def time_zone_to_int(timezone):
    index=["utc","bst","cdt"].index(timezone)
    return [0,1,-5][index]
    
studentmatchteacher("eng","eng","na","yr10","utc")
