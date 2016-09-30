ques=['Name of this game is _1_.This game have _2_ levels.You are playing _3_ level.Type of this game is _4_',
      'Full form of HTML is _1_.This language is used to make _2_ pages._3_ tag is used for largest heading._4_ tag is used to highlight the text.',
      'Full form of CSS is _1_.Types of CSS are _2_ , _3_ and_4_ ',
      'Programming language used in this game is _1_.It is used for _2_ development.This uses _3_ for compilation.This language supports _4_ oriented programming']
#ques list defines the questions corresponding to each level with 4 unique questions at each level.
answer=[['madlib','4','novice','puzzle'],
        ['hyper text markup language','web','h1','mark'],
        ['cascading style sheet','external','internal','inline'],
        ['python','web','interpreter','object']]
#answer list defines the answer corresponding to questions at each level.
#defination main is the first and foremost defination which asks user which level user wants to play and if entered wrong prompts user to enter the value again and return index as index of ques and ans list..
levels=['1','2','3','4']
#levels is list of stage numbers i.e stages that are prompted to user to play
no_of_blanks=4
#no of blanks defines the total no of questions at each level.
def main():
    print "1.Novice "+" "*5+"2.Easy"+" "*5+"3.Difficult"+" "*5+"4.Expert"
# here a stands for index
    index=raw_input("Enter level number  you want to play..")
    print index
    if(index in levels):
        index=int(index)
        index=index-1
        print ques[index]
        ans(index)
    else:
        print "You have entered wrong level number.Please try again.. "
        main()
#defination ans is the main game changer.In this module we have asked ques and prompted user to input the right answer and if he/she is not able to answer then we ask again...
def ans(ques_index):
#Here ans_index is a variable which defines the questions no which is asked to the user and relates it answers at that index in answer list.If the user enters right answer then value of ans_index i.e counter variable is increased else it will remain same until the user guess the correct answer..
    ans_index=0
    while(ans_index<no_of_blanks):
        #var is the variable that stores raw input which user enters to play the game
        var=raw_input("Enter "+str(ans_index+1)+" blank...").lower()
        #string is a variable in which ques of particular stage is temporarily stored to perform action in string i.e replace the blank with correctly inputted answer by user...
        string=ques[ques_index]
        #to replace is a variable that is used to replace the blank with var i.e the value that is given by user correctly......
        toreplace=("_"+str(ans_index+1)+"_")
        string=string.replace(toreplace,var)
        if(var==answer[ques_index][ans_index]):
            ques[ques_index]=string
            print "\n"+"You entered correct answer :)"+"\n"
            print string
            ans_index=ans_index+1
        else:
            print "you entered wrong answer try again!!"

print "Welcome to Mad_lib Game..."
play='y'
while(play=='y'):
    main()  
    print "\n"+"Congratulations you have completed current level :)"+"\n"
    #play variable stores 'y' or 'n' which will decide if user will play further or not...
    play=raw_input("To continue playing press 'y' else press 'n'.. :)").lower()
print "Thank you for playing the game :)"
