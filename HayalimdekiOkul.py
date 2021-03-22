class schools():
  def __init__(self,schoolName,studentName,studentClass,teacher,lessons):
    self.schoolName = schoolName
    self.studentName= studentName
    self.studentClass = studentClass
    self.teacher = teacher
    self.lessons = lessons 

school1 = schools("Anadolu Lisesi","Mehmet Yılmaz","10-C","Özgür Coşkun","Kimya, Fizik, Matematik")

school2 = schools("Bilişim Lisesi","Sude Bilgin","12-D","Hüseyin Demir","Programlama, Web tasarım, Elektronik")

school3 = schools("Sağlık Meslek Lisesi","Büşra Tekin","11-A","Sibel Gül","Anatomi, İlk yardım, Beslenme")

print("*****SCHOOL1******")
print("\nSchool: {}".format(school1.schoolName)+
      "\nName: {}".format(school1.studentName)+
      "\nClass: {}".format(school1.studentClass)+
      "\nTeacher: {}".format(school1.teacher)+
      "\nLessons: {}".format(school1.lessons))

print("\n*****SCHOOL2******")
print("\nSchool: {}".format(school2.schoolName)+
      "\nName: {}".format(school2.studentName)+
      "\nClass: {}".format(school2.studentClass)+
      "\nTeacher: {}".format(school2.teacher)+
      "\nLessons: {}".format(school2.lessons))

print("\n*****SCHOOL3******")
print("\nSchool: {}".format(school3.schoolName)+
      "\nName: {}".format(school3.studentName)+
      "\nClass: {}".format(school3.studentClass)+
      "\nTeacher: {}".format(school3.teacher)+
      "\nLessons: {}".format(school3.lessons))




  

