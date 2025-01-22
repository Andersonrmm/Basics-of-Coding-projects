import random
import json

print("\nHello and greeetings to the test")
       
def take_test(questions):
   result = 0
   
   
   for idx, inquiry in enumerate(questions):
         print(f"\nInquiry {idx + 1}: {inquiry['Query:']}")
         for i, option in enumerate(inquiry['options'], start=1):
            print(f"{i}. {option}")

         """To evaluate if answer is correct or incorrect"""
         while True:
            try:
               user_response = int(input(f"\nPlease enter the number of your response here:"))
               if 1 <= user_response <= len(inquiry['options']):
                  break
               else:
                  print("Please input a correct option.")  
            except ValueError:
               print("Please input a number")
             
         if user_response == inquiry["response"]:
            print("Correct!")
            result += 1
         else:
            correct_option = inquiry['options'][inquiry['response'] -1]
            print("\nNice attempt")
            print(f"The correct response was: {correct_option}")


   """Personalised messages for the each final result""" 
   final_result = {
      0: "\nUps... :(",
      1: "\nTry again...",
      2: "\nMaybe next time",
      3: "\nNot bad",
      4: "\nYou were almost there!",
      5: "\nCongrats you scored the HIGHEST!!!"
   }
   print(final_result.get(result))
   print(f"Your final result was: {result}/{len(questions)}.")


   """To play again or exit the app"""
   while True:
      answer = input("\nTo choose another subject press (1) | To leave the test press (2):")
      if answer == "1":
         break
      elif answer == "2":
         print("\nEnd of the test. Thank you!") 
         return
      else:
         print("Please input a correct option.")


def main():

   while True:
      print("\nChoose Subject")
      print("1. Maths", )
      print("2. Science")
      print("3. History")
      print("4. Economics")

      while True:
         try:
            selected_subject = int(input(f"\nPlease enter the number of your subject here:"))
            if selected_subject == 1:
               take_test(math_test)
               break
            elif selected_subject == 2:
               take_test(science_test)
               break
            elif selected_subject == 3:
               take_test(history_test)
               break
            elif selected_subject == 4:
               take_test(economics_test)
            else:
               print("Choose a valid option between (1,2,3 or 4)")
         except ValueError:
            print("Type a number!")


if __name__ == "__main__":                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
   main()
       
