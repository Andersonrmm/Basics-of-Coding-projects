import random

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
   math_test = [
      {"Query:": "If x is a positive integer in the equation 12x = q, then q must be", "options": ["Positive integer", "Negative even integer", "Zero", "Positive odd integer"], "response":1},
      {"Query:": "If x + 6 = 9, then 3x + 1 =", "options": ["1", "5", "10", "7"], "response":3},
      {"Query:": "What is the approximate value of the square root of 1596?", "options": ["10", "20", "30", "40"], "response":4},
      {"Query:": "The simple interest on $160 for 6 months at 5% per annum is", "options": ["$4", "$8", "$16", "$48"], "response":1},
      {"Query:": "What is the number 2.0847 to 2 decimal places?", "options": ["2.09", "2.08", "2.1", "2.10"], "response":2}
   ]

   science_test = [
      {"Query:": "Which part of the Central Nervous System controls “reflex Actions” ?", "options": ["Mesencephalon", "Rhombencephalon", "Medulla oblongata", "Spinal Chord"], "response":4},
      {"Query:": "Ripening of fruits is because of which among the following plant hormones?", "options": ["Auxin", "Ethylene", "Gibberellins", "Carins"], "response":2},
      {"Query:": "Which among following is not a Fish?", "options": ["Cuttle Fish", "Gold Fish", "Dog Fish", "Zebra Fish"], "response":1},
      {"Query:": "Which of the following elements is less electronegative than carbon?", "options": ["Si", "N", "Cl", "F"], "response":1},
      {"Query:": "Which of the following elements is the most electropositive?", "options": ["Br", "Cl", "F", "I"], "response":4}
   ]

   history_test = [  
      {"Query:": "How many colonies were there in the United States?", "options": ["12", "13", "14", "15"], "response":2},
      {"Query:": "The Louisiana Purchase took place in what year?", "options": ["1803", "1813", "1823", "1837"], "response":1},
      {"Query:": "Which of the following was NOT Greek?", "options": ["Homer", "Herodotus", "Virgil", "Aglaophon"], "response":3},
      {"Query:": "On what island was Napoleon born?", "options": ["Corsica", "Elba", "Sicily", "Sardinia"], "response":1},
      {"Query:": "Who was the first emperor of Rome?", "options": ["Julius Caesar", "Augustus ", "Nero", "Constantine"], "response":2}
   ]

   Economics_test = [
      {"Query:": "What happens if the price floor is set higher than the equilibrium price?", "options": ["Scarcity", "Stability", "Surpluses", "None of the precending"], "response":3},
      {"Query:": "What is societys primary economic problem?", "options": ["Unemployment", "Inequality", "Poverty", "Scarcity"], "response":4},
      {"Query:": "What exactly do you mean when you say “mixed economy”?", "options": ["Traditional and modern industries", "Both the public and private sectors are involved", "Involvement of both foreign and domestic investors", "Subsistence and commercial farming"], "response":2},
      {"Query:": "What exactly do you mean when you say “under perfect competition in the product market”?", "options": ["VMP = MRP", "MRP > VMP", "VMP > MRP", "None of the preceding"], "response":4},
      {"Query:": "Which of the following individuals is not considered economically inactive?", "options": ["People who are looking for work but do not have one", "Caregivers in the family or at home", "Students who are unemployed.", "Workers who are discouraged"], "response":1}
   ]


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
               take_test(Economics_test)
            else:
               print("Choose a valid option between (1,2,3 or 4)")
         except ValueError:
            print("Type a number!")


if __name__ == "__main__":                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
   main()
