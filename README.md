# Textutils.in
							TEXTUTILS.IN
                                                       ----------------
This is a text editor website create by using Django Framework

In this website i also use the bootstrap which is a library of html,css,and javascript to give a better look to it

There is a textarea present in it ,when a user enter some text then he is able to try some action like

Remove punctuation like remove the (. , / ' " ; ] [ } { \ |) etc from a string

  captalige a string means the first letter of all the word must be capital method -- string.title()
  
  Uppercase to a sting means all the character of the string is in capital letter methos--- string.upper()
  
  lowercase means all the string is in lowercase method is ----- string.lower()
  
  length of a string means the total number of item present in a string method--len(string)
  
  Character count means only count how many character are present in a string without the white spaces methos-- 
              count = 0
        for index, item in enumerate(textvalue):
            if not (textvalue[index] == ' '):
                count = count + 1
				
	Remove extra spaces from a string
	
	user string=Hii           i     am            IPCODE77         
	Newstring=Hii i am IPCODE77
	
	Remove Newline from a string means
	
	user string=Hiii
				i
				am
				IPCODE77
	After click the remove extra line action the string looks like this newstring=Hiii i am IPCODE77			
	
  ![Screenshot (82)](https://user-images.githubusercontent.com/89587666/184400176-9ea251ae-946e-4e3c-a617-75b3725723fd.png)
