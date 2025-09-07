with open("story.txt","r") as f:
    story=f.read()
words=[]
start_charater="<"
end_charater=">"
start_of_word=-1
for i,char in enumerate(story):
    if char==start_charater:
        start_of_word=i
    if char==end_charater and start_of_word!=-1:
        
        word=story[start_of_word:i+1]   
        words=tuple(word) 
        start_of_word=-1
print(words)
answers={}
for word in words:
    user_words=input(f"Enter a {word.strip("<>")}: ")
    answers[word]=user_words
print(answers)
for word,ans in answers.items():
    story=story.replace(word,ans)
print(story)