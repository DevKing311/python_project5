import random 
import datetime
import time
import mysql.connector

mycon = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='CBT_EXAM'
)
mycursor = mycon.cursor()

# mycursor.execute('CREATE DATABASE CBT_EXAM')
# mycursor.execute('''
#  CREATE TABLE student(
#                 sn INT PRIMARY KEY AUTO_INCREMENT,
#                 user_id VARCHAR(50) UNIQUE  NOT NULL,
#                 username VARCHAR(50) UNIQUE KEY NOT NULL,
#                 password VARCHAR(50) NOT NULL
#                   )
#  ''');
# mycursor.execute('''
# CREATE TABLE admin(
#                 sn INT PRIMARY KEY AUTO_INCREMENT,
#                 user_id VARCHAR(50) UNIQUE  NOT NULL,
#                 username VARCHAR(50) UNIQUE KEY NOT NULL,
#                 password VARCHAR(50) NOT NULL
#                  )
# ''')
# mycursor.execute('''
# CREATE TABLE exam(
#                  exam_id INT PRIMARY KEY AUTO_INCREMENT,
#                  exam_name VARCHAR(250) UNIQUE KEY NOT NULL)
# ''');
# mycursor.execute('''
# CREATE TABLE questions(
#                   question_id INT PRIMARY KEY AUTO_INCREMENT,
#                  exam_id INT NOT NULL,
#                  question_text VARCHAR (500) NOT NULL,
#                  option_a VARCHAR(300) NOT NULL,
#                  option_b VARCHAR(300) NOT NULL,
#                  option_c VARCHAR(300) NOT NULL,
#                  option_d VARCHAR(300) NOT NULL,
#                  correct_option CHAR(1),
#                  FOREIGN KEY (exam_id) REFERENCES exam(exam_id)
#                  )
# ''')
# myquery = 'INSERT INTO exam (exam_name) VALUES(%s)'
# val = [('General health awareness',), ('Physical fitness and exercise science',), ('Mental and public health',)]
# mycursor.executemany(myquery,val)
# mycon.commit()
# myquery = 'INSERT INTO questions (exam_id, question_text, option_a, option_b, option_c, option_d, correct_option) VALUES(%s,%s,%s,%s,%s,%s,%s)'
# questions1 = [
#     (1,'Which factor is essential for maintaining good health?',' Sleep only','Exercise only','Balanced lifestyle','. Medication','c'),
#     (1,'What is the body main source of energy?','Protein','fat',' Carbohydrate','vitamin','c'),
#     (1,'How much water is recommended daily for adults (average)?','1–2 glasses',' 2–3 glasses',' 6–8 glasses',' 12–15 glasses','c'),
#     (1,'Poor hygiene can lead to:','Strong immunity','Infections','Weight loss',' Better digestion','b'),
#     (1,'Which organ pumps blood around the body?','Lungs','Brain','Liver','Heart','d'),
#     (1,'Lack of sleep may cause','Better focus',' Increased productivity','Fatigue','Faster recovery','c'),
#     (1,'Which habit helps prevent disease?','Hand washing','Skipping meals','Smoking','Alcohol abuse','a'),
#     (1,'A balanced diet includes:','One food group','Two food groups','All food groups in right proportion','Only vegetables','c'),
#     (1,'Excess sugar intake can cause:','Diabetes','Strong bones','Better memory','Improved vision','a'),
#     (1,'Exercise benefits mental health by:','Increasing stress','Improving mood','Causing anxiety','Reducing sleep','b')
# ]
# mycursor.executemany(myquery,questions1)
# mycon.commit()


# myquery = 'INSERT INTO questions (exam_id, question_text, option_a, option_b, option_c, option_d, correct_option) VALUES(%s,%s,%s,%s,%s,%s,%s)'
# question2 = [
#  (2,'Cardiorespiratory fitness improves the function of the:','Muscles only','Heart and lungs','Bones','Joints','b'),
#  (2,'Which exercise improves flexibility?','Sprinting','Stretching','Deadlift','Push-ups','b'),
#  (2,'BMI is used to assess','Strength level','Weight status','Endurance','Agility','b'),
#  (2,'Warm-up before exercise helps to:','Cause fatigue','Prevent injury','Prevent injury','Increase stiffness','b'),
#  (2,'Which is a compound exercise?',' Bicep curl','Leg extension','Squat','Calf raise','c'),
#  (2,'Overtraining may cause:','Faster recovery','Injury and fatigue','Muscle growth',' Better sleep','b'),
#  (2,'Rest days are important for:','Muscle recovery','Fat gain','Loss of strength','Dehydration','a'),
#  (2,'Which training improves muscle endurance?','Heavy weights low reps','Light weights high reps','No resistance','Random training','b'),
#  (2,'Breathing correctly during exercise helps to:','Reduce oxygen supply','Improve performance','Cause dizziness',' Increase fatigue','b'),
#  (2,'Cool-down after exercise helps to:','Increase heart rate','Prevent stiffness','Cause injury','Stop blood flow','b')
# ]
# mycursor.executemany(myquery,question2)
# mycon.commit()

# myquery = 'INSERT INTO questions (exam_id, question_text, option_a, option_b, option_c, option_d, correct_option) VALUES(%s,%s,%s,%s,%s,%s,%s)'
# question3=[
#  (3,'Mental health refers to:','Absence of disease','Emotional and psychological well-being','Physical strength only',' Intelligence level','b'),
#  (3,'Chronic stress may lead to:','Better focus','Anxiety and depression','Improved immunity','Faster healing','b'),
#  (3,'Which habit supports good mental health?','Social interaction','Isolation','Lack of sleep','Poor diet','a'),
#  (3,'Public health focuses mainly on:','Individual treatment','Community health prevention','Surgery','Gym training','b'),
#  (3,'Vaccination helps to:','Cure all diseases','Prevent infectious diseases',' Increase weight','improve strength','b'),
#  (3,'Which is a sign of good mental health?','Persistent sadness','Emotional balance','Constant worry',' Social withdrawal','b'),
#  (3,'Substance abuse can result in:','Better judgment','Health problems','Increased focus','Strong immunity','b'),
#  (3,'Clean environment helps to:','Spread diseases','Promote public health','Increase pollution','Cause infections','b'),
#  (3,'Sleep deprivation affects:','Memory and concentration','Height growth','Eye color','Blood group','a'),
#  (3,'Seeking professional help for mental health issues is:','Weakness','Unnecessary','Responsible','Dangerous','c')
# ]
# mycursor.executemany(myquery,question3)
# mycon.commit()
# mycursor.execute('''
# CREATE TABLE results(
#                   result_id INT PRIMARY KEY AUTO_INCREMENT,
#                   user_id VARCHAR(50) NOT NULL,
#                   exam_id INT NOT NULL,
#                   score INT ,
#                   date_taken DATETIME DEFAULT CURRENT_TIMESTAMP,
#                   FOREIGN KEY (user_id) REFERENCES student(user_id),
#                   FOREIGN KEY (exam_id) REFERENCES exam(exam_id)
# #                   )
# #                   ''')

class cbt:
    def __init__(self):
        self.mainpage()

    def mainpage(self):
        print(' Welcome to Health Science Computer-Based Test (HS-CBT)')
        ask = input('1. Login\n2. Sign-up\nChoose: ')
        if ask=="1":
            print('loading....')
            time.sleep(2)
            S_A= input("Select user\n1.Student\n2. Admin\nChoose: ")
            if S_A=="1":
                print('loading....')
                time.sleep(2)
                self.student_login()
            elif S_A=="2":
                print('loading....')
                time.sleep(2)
                self.admin_login()
        elif ask=="2":
            print('loading....')
            time.sleep(2)
            S_A= input("Select user\n1.Student\n2. Admin\nChoose: ")
            if S_A=="1":
                print('loading....')
                time.sleep(2)
                self.student_signup()
            elif S_A=="2":
                print('loading....')
                time.sleep(2)
                self.admin_signup()
 
    def student_signup(self):
        U_name= input('Enter name: ') 
        P_word= input('Enter password: ')
        id=random.randint(100,200)
        U_id = f"CBT25-{id}"
        myquery='INSERT INTO student (user_id, username, password) VALUES (%s,%s,%s)'
        val= (U_id,U_name,P_word)
        mycursor.execute(myquery,val)
        mycon.commit()
        if mycon:
            print('Registration Succesful, User_ID:',U_id)
            oper= input('Do you want to login?: ').upper()
            if oper=="YES":
                self.student_login()
            else:
                print('GoodBye....')
        else:
            print('Fail')
    def student_login(self):
         print('\n====LOGIN====')
         self.u_id= input("Enter your user id: ")   
         p_word= input('Enter your password: ')
         myquery= 'SELECT * FROM student WHERE user_id=%s AND password=%s'
         val=(self.u_id,p_word)
         mycursor.execute(myquery,val)
         result= mycursor.fetchone()
         if result:
            print('\n====WELCOME===')
            self.student_menu()
         else:
            print('Wrong Username or Password')
    def admin_signup(self):
        U_name= input('Enter name: ') 
        P_word= input('Enter password: ')
        id=random.randint(201,300)
        U_id = f"ADMN25-{id}"
        myquery='INSERT INTO admin (user_id, username, password) VALUES (%s,%s,%s)'
        val= (U_id,U_name,P_word)
        mycursor.execute(myquery,val)
        mycon.commit()
        if mycon:
            print('Registration Succesful, User_ID:',U_id)
            oper= input('Do you want to login?: ').upper()
            if oper=="YES":
                self.admin_login()
            else:
                print('GoodBye....')
        else:
            print('Fail')
    def admin_login(self):
          print('\n====LOGIN====')
          u_id= input("Enter your user id: ")
          p_word= input('Enter your password: ')
          myquery= 'SELECT * FROM admin WHERE user_id=%s AND password=%s'
          val=(u_id,p_word)
          mycursor.execute(myquery,val)
          result= mycursor.fetchone()
          if result:
            print('\n====WELCOME===')
            self.admin_menu()
          else:
             print('Wrong Username or Password')
    def student_menu(self):
        E_V= input('Select \n1.Take Exam\n2. View Result\n3. Quit\nChoose: ')
        if E_V=='1':
           self.take_exam()
        elif E_V=='2':
           self.view_result()
        elif E_V=='3':        
            print('Good Bye!!')
            return
        else:
            print('Invalid Choice')
            return
    def admin_menu(self):
        admn=input('Select:\n1.Add Questions\n2. Edit Questions\n3. Delete Exam\n4. View Results\n5. Quit \nChoose: ')
        if admn=='1':
            self.add_q()
        elif admn=='2':
            self.edit_q()
        elif admn=='3':
            self.delete_e()
        elif admn=='4':
            self.view_AR()
        elif admn=='5':
            return
        else:
            print('Invalid choice')
            return
        
    def exam_menu(self):
         mycursor.execute("SELECT exam_id, exam_name FROM exam")
         result = mycursor.fetchall()
         print("\nAvailable Exams:")
         for exam in result:
          print(f"{exam[0]}. {exam[1]}")
    def take_exam(self):
         self.exam_menu()
         exam = int(input("\nEnter exam number to start: "))  
         check_query = "SELECT * FROM results WHERE user_id = %s AND exam_id = %s"   
         mycursor.execute(check_query, (self.u_id,exam))
         already_taken = mycursor.fetchone()
         if already_taken:
             print("\n You have already taken an exam.")
             return
         myquery= 'SELECT question_text, option_a, option_b, option_c, option_d, correct_option FROM questions WHERE exam_id = %s'  
         mycursor.execute(myquery, (exam,))  
         questions = mycursor.fetchall()
         if not questions:
            print("No questions found for this exam.")
            self.exam_menu()
         print("\n--- Exam Started ---")
         score = 0
         for i, q in enumerate(questions, start=1):
          print(f"\nQuestion {i}: {q[0]}")
          print("A.", q[1])
          print("B.", q[2])
          print("C.", q[3])
          print("D.", q[4])
          answer = input("Your answer (A/B/C/D): ").lower()
          if answer == q[5]:
             score += 1
         myquery = 'INSERT INTO results (user_id, exam_id, score) VALUES (%s, %s, %s)'
         mycursor.execute(myquery,(self.u_id, exam, score))
         mycon.commit()
         print("\nExam submitted successfully.")
         self.student_menu()
    def view_result(self):
      myquery='SELECT exam.exam_name, results.score, results.date_taken FROM results  JOIN exam ON results.exam_id = exam.exam_id WHERE user_id = %s'
      mycursor.execute(myquery, (self.u_id,))
      records = mycursor.fetchall()
      print("\n--- Your Results ---")
      for exam_name, score, date_taken in records:  
        mycursor.execute("SELECT COUNT(*) FROM questions WHERE exam_id = %s", (self.u_id,))
        num_questions = mycursor.fetchone()[0]
        print(f"Exam ID : {exam_name}")  
        print(f"Score   : {score}/{num_questions}")
        print(f"Date    : {date_taken}")
        print("-" * 30)
    def add_q(self):
         mycursor.execute("SELECT exam_id, exam_name FROM exam")
         result = mycursor.fetchall()
         print("\nAvailable Exams:")
         for exam in result:
          print(f"{exam[0]}. {exam[1]}")
         exam = int(input("\nEnter Exam ID to add question: "))  
         question_text = input("Enter the question: ")
         option_a = input("Option A: ")
         option_b = input("Option B: ")
         option_c = input("Option C: ")
         option_d = input("Option D: ")
         correct_option = input("Correct option (A/B/C/D): ").lower()
         myquery= 'INSERT INTO questions (exam_id, question_text, option_a, option_b, option_c, option_d, correct_option) VALUES(%s,%s,%s,%s,%s,%s,%s)'  
         mycursor.execute(myquery, (exam, question_text, option_a, option_b, option_c, option_d, correct_option))
         mycon.commit()
         print("\nQuestion added successfully!")

         print()
    def edit_q(self):
          mycursor.execute("SELECT exam_id, exam_name FROM exam")
          exams = mycursor.fetchall()
          print("\n--- Available Exams ---")
          for e_id, e_name in exams:
           print(f"{e_id}. {e_name}")
          exam_id = int(input("Enter exam ID: "))
          mycursor.execute(
         "SELECT question_id, question_text FROM questions WHERE exam_id = %s",
         (exam_id,) )
          questions = mycursor.fetchall()
          print("\n--- Available Exams ---")
          for e_id, e_name in exams:
             print(f"{e_id}. {e_name}")
          exam_id = int(input("\nEnter exam ID: "))
          mycursor.execute( "SELECT question_id, question_text FROM questions WHERE exam_id = %s", (exam_id,)   )
          questions = mycursor.fetchall()
          print("\n--- Questions ---")
          for q_id, q_text in questions:
           print(f"{q_id}. {q_text}")
          q_id = int(input("\nEnter question ID to edit: "))
          new_question = input("New question text: ")
          new_a = input("New option A: ")
          new_b = input("New option B: ")
          new_c = input("New option C: ")
          new_d = input("New option D: ")
          correct = input("Correct option (a/b/c/d): ").lower()
          myquery ='UPDATE questions SET question_text=%s,option_a=%s, option_b=%s,option_c=%s,option_d=%s, correct_option=%s WHERE question_id=%s AND exam_id=%s'
          mycursor.execute(myquery, ( new_question, new_a, new_b, new_c, new_d, correct, q_id, exam_id))
          mycon.commit()
          print(" Question updated successfully.")

    def delete_e(self):
     exam_id = int(input("Enter exam ID: "))
     mycursor.execute( "SELECT question_id, question_text FROM questions WHERE exam_id = %s",(exam_id,))
     records = mycursor.fetchall()
     if not records:
        print("No questions found.")
        return
     print("\n--- Questions ---")
     for q_id, q_text in records:
        print(f"{q_id}. {q_text}")
     q_id = int(input("\nEnter Question ID to delete: "))
     confirm = input("Are you sure? (yes/no): ").lower()
     if confirm != "yes":
        print("Deletion cancelled.")
        return
     mycursor.execute("DELETE FROM questions WHERE question_id = %s", (q_id,))
     mycon.commit()
     print(" Question deleted successfully.")

    def view_AR(self):
      myquery='''
          SELECT student.username, exam.exam_name, results.score, results.exam_id, results.date_taken
          FROM results
          JOIN exam ON results.exam_id = exam.exam_id
          JOIN student ON results.user_id = student.user_id
       '''
      mycursor.execute(myquery, )
      records = mycursor.fetchall()
      print("\n--- Students Final Results ---")
      for username,exam_name, score,exam_id, date_taken in records:  
        mycursor.execute("SELECT COUNT(*) FROM questions WHERE exam_id = %s", (exam_id,))
        num_questions = mycursor.fetchone()[0]
        print(f'Username: {username}')
        print(f"Exam ID : {exam_name}")  
        print(f"Score   : {score}/{num_questions}")
        print(f"Date    : {date_taken}")
        print("-" * 30)
            
cbt()       





