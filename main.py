from study_reminders.students import Students
from study_reminders.students_manager import StudentsManager
from study_reminders.logger import log_reminder
from study_reminders.reminder_generator import generate_reminder
from study_reminders.reminder_sender import send_reminder
from study_reminders.scheduler import schedule_reminders

def send_reminders_now(students_manager):
    """
    Manually trigger reminders for all students - used for testing
    """
    students = students_manager.get_students()
    if not students:
        print("No students found.")
        return
    
    print("Sending Reminder Manually")
    for student in students:
     reminder = generate_reminder(student["name"], student["course"])
     send_reminder(student["email"], reminder)
     log_reminder(student, reminder)
     print("Reminder sent to " + student["name"])
    print("All reminders sent and logged")

def add_student(students_manager):
   """Add a new student manually"""
   name = input("Enter student name: ")
   email = input("Enter student email: ")
   course = input("Enter course name: ")
   preferred_time = input("Enter preferred reminder (e.g., 08:00): ")
   if preferred_time == "":
      preferred_time = "08:00"
    
   students_manager.add_student(name, email, course, preferred_time)
   print("Student " + name + " added successfully!")

def list_students(students_manager):
   """List all students currently in the system"""
   students = students_manager.get_students()
   if not students:
      print("No students found")
   else:
      print("Student list:")
      for student in students:
         print("Name: " + student["name"] + ", Email: " + student["email"]
               + ", Course: " + student["course"]
               + ", Preferred Time: " + student["preferred_time"])

def remove_student(students_manager):
   """Remove a student by name"""
   name = input("Enter the name of the student to remove: ")
   students_manager.remove_student(name)
   print("Student " + name + " Removed successfully!")

def scheduled_reminders(students_manager):
   """
   Start the daily reminder scheduler
   """
   print("Starting daily reminder scheduler")
   print("Reminders will be sent automatically based on preferred times")
   schedule_reminders(students_manager, generate_reminder, send_reminder, log_reminder)

def main():
   print("Study Reminders Automation Tool")
   students_manager = StudentsManager()

   menu_options = {
      "1": send_reminders_now,
      "2": scheduled_reminders,
      "3": add_student,
      "4": list_students,
      "5": remove_student
   }

   while True:
      print("Options:")
      print("1. Send reminders now (manual test)")
      print("2. Start scheduled daily reminders")
      print("3. Add a new student")
      print("4. List all students")
      print("5. Remove A student")
      print("6. Quit")

      choice = input("Choose an option (1-6): ")

      if choice == "6":
         print("Exiting Study Reminder Tool. Goodbye!")
         break
      elif choice in menu_options:
         #Call the matching function
         menu_options[choice](students_manager)
      else:
          print("Invalid option. Please selecect a number between 1 and 6.")

if __name__ == "__main__":
   main()