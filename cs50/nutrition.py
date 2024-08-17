# def main():
#     dict = {'apple':'130','avocado':'50','banana':'110','cantaloupe':'50','grapefruit':'60','grapes':'90','honeydew':'50','kiwifruit':'90','lemon':'15','lime':'20','nectarine':'60','orange':'80','peach':'60','pear':'100','pineapple':'50','plums':'70','strawberries':'50','sweet cherries':'100','tangerine':'50','watermelon':'80'}


#     userInput = input("Item: ")
#     if userInput in dict:
#         print("Calories: ",dict[userInput])
        
    

# main()

chart={'apple':'130','avocado':'50','banana':'110','cantaloupe':'50','grapefruit':'60','grapes':'90','honeydew':'50','kiwifruit':'90','lemon':'15','lime':'20','nectarine':'60','orange':'80','peach':'60','pear':'100','pineapple':'50','plums':'70','strawberries':'50','sweetcherries':'100','tangerine':'50','watermelon':'80'}

A=input("item:")
if A in chart:
    result=chart.get(A)
    print(result)


