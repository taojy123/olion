import pprint
import step

html = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Kid Words</title>
    <style>
        table{
            border-collapse: collapse;
            margin: 0 auto;
            text-align: center;
        }

        td, th {
            border: 1px solid #cad9ea;
            color: #666;
            height: 30px;
        }

        thead th {
            background-color: #CCE8EB;
            width: 100px;
        }

        tr:nth-child(odd) {
            background: #fff;
        }

        tr:nth-child(even) {
            background: #F5FAFA;
        }
    </style>
  </head>
  <body>
    <table width="100%">
      <thead>
        <tr>
          <th style="width:40px">日期</th>
          <th>新词</th>
          <th>新句</th>
        </tr>
      </thead>
      <tbody>
        %for r in rs:
          <tr>
            <td>{{ r['day'][-4:] }}</td>
            <td>{{ r['new_words'] }}</td>
            <td>{{ r['new_sentences'] }}</td>
          </tr>
        %endfor
      </tbody>
    </table>
  </body>
</html>
"""



text = """
20200817
Dear parents, this week's story is The Gingerbread Man. Today we introduced 2 new words to the kids:
- cat
- dog
We played games to help the kids understand the new words and work on their pronunciation:
~- what do you hear? 
~- hit what you hear
We introduced a new greeting to the kids:
- how are you? 
- I'm happy.
- I'm sad. 
- I'm tired 



20200818
Dear parents, today we reviewed our new vocabulary from yesterday:
- dog
- cat
We played a game to test the kids knowledge and pronunciation of the vocabulary:
~- cross the river 
We practiced common greetings:
- hello
- goodbye
- how are you? 



20200819
Dear parents, today we introduced the numbers 1-7 to the children, focusing on numbers 1-3. 
We introduced new vocabulary to the kids:
- fox 
- frog
We used numbers to practice our new vocabulary:
~- roll the dice
We practiced our new sentences:
- What animal is it?
- it's a...



20200820
Dear parents, today we reviewed all of our new vocabulary:
- fox 
- frog
- dog 
- cat
We played games to review these words:
~- slap card
~- basketball
We also reviewed our four new colours:
- blue
- yellow
- red
- green 
We read the story book of the week "the gingerbread man".



20200821
Dear parents, today we reviewed all of our new vocabulary:
- dog
- cat
- frog
- fox
We played the dice game to review both our vocabulary and our numbers. 
We played flashcard reveal to review our new sentences:
- what animal is it?
- it's a...



20200824
Dear parents, this week we have a new story book:
- the hungry caterpillar
We introduced new vocabulary to the children:
- apple 
- pear
We played a bowling game to help the kids understand the new words while working on their pronunciation. 




20200825
Dear parents, today we reviewed our new vocabulary from yesterday:
- apple
- pear
We played a game to test the kids knowledge and pronunciation of the vocabulary:
~- strawberry
We practiced common greetings:
- good morning
- goodbye
- how are you? 




20200826
Dear Parents, today we reviewed all of our new vocabulary:
- apple
- pear
- plum
- strawberry
We played "find the flashcard" to test the kids' knowledge of the new words.
We also read our story book:
- The Hungry Caterpillar




20200827
Dear Parents, today we reviewed all of our new vocabulary:
- apple
- pear
- plum
- strawberry
We played "little teacher", this game helps to test the kids' knowledge of the new words and also their pronunciation. One students acts as the teachers and shouts commands at the other student. Example: " find the strawberry", then we switch rolls so the kids can practice both rolls. 
We also read our story book:
- The Hungry Caterpillar
We reviewed our numbers from 1-10




20200828
Dear Parents, today we reviewed all of our new vocabulary:
- apple
- pear
- plum
- strawberry
We introduced a new sentence structure:
- What fruit do you like? I like...
We played a game called "what's missing" to test the kids' knowledge of the new words.  




20200831
Dear parents, this week our new topic is "my school".
We introduced two new words to the children:
- baby
- kiss
We played "sticky ball" to incourage the children to say the new vocabulary.



20200901
Dear Parents, today we reviewed the new vocabulary that we learned yesterday:
- baby 
- kiss
We played a game called "find the word" to review the new vocabulary. 




20200902
Dear Parents, today we learned two new words:
- love
- hug
We played an obstacle course game to help the kids learn the new words. 
We introduced a new sentence structure:
- I love...
We also reviewed some of the colours we learned. 



20200903
Dear Parents, today we reviewed our new vocabulary:
- love
- hug
We played "guess where the ball is" to encourage the kids to say the words. 
We reviewed our new sentence:
- I love...
We also introduce some vocabulary relating to the weather:
- it's sunny
- it's raining
- it's hot
- it's cold
- how's the weather?




20200904
Dear Parents, today we reviewed all of our new content from this week:
- baby
- love
- hug
- kiss
We also reviewed our new sentence structure:
- I love...
With played "jump and find the word" which helps the kids practice their pronunciation and work on their knowledge of the words. 




20200907
Dear parents, this week our topic is Adults in school. We introduced two new words:
- teacher
- school
We played a game to help the kids remember the new words:
- hit the word
We also reviewed vocabulary from previous weeks during the games. 



20200908
Dear Parents, today we reviewed the new vocabulary that we learned yesterday:
- teacher
- school
We played a game called "find the word" to review the new vocabulary. 




20200909
Dear Parents, today we learned a new word:
- friends
And review the words we learned yesterday. 
We played a matching game to help the kids learn the new words. 
We also reviewed some of the colours we learned. 




20200911
Dear Parents, today we reviewed all of our new content from this week:
- teacher
- school
- friends
We also reviewed our new sentence structure:
- I love...
With played "pat and find the word" which helps the kids practice their pronunciation and work on their knowledge of the words. 





20200914
Dear parents, this week our new topic is "senses".
We introduced two new words to the children:
- see
- hear
We played "pull cards" to incourage the children to say the new vocabulary.





20200915
Dear Parents, today we reviewed our new vocabulary:
- see
- hear
We played "Which one is picture see" to encourage the kids to say the words. 




20200916
Dear Parents, today we learn our new vocabulary:
- taste
- smell
We played "sticky ball game" to encourage the kids to say the words. 
We reviewed our new sentence:
- I can...




20200917
Dear Parents, today we reviewed all of our new content from this week:
- hear
- see
- smell
- taste
We also reviewed our new sentence structure:
- I can...




20200921
- 
Dear parents, this week our new topic is "happy me,happy friends".
We introduced two new phrases to the children:
- good morning
- good afternoon
We played "greetings" to incourage the children to say the new vocabulary.




20200922
-
Dear Parents, today we reviewed our new vocabulary:
- good morning
- good afternoon
We played "roleplay game"" to encourage the kids to say the words. 




20200923
-
Dear Parents, today we learn our new phrases:
- thank you
- good bye
We played "thank you game" to encourage the kids to say the phrases. 




20200925
-
Dear Parents, today we reviewed all of our new content from this week:
- good morning
- good afternoon
- thank you
- good bye
We also reviewed our new sentence structure:
- I love you. Hand in hand. 




20200927
Dear parents, this week our new topic is "our bodies".
We introduced two new words to the children:
- eye
- ear
We played "pat game" to incourage the children to say the new vocabulary.




20200928
Dear Parents, today we reviewed our new vocabulary:
- eye
- ear
We played "jump game"" to encourage the kids to say the words. 





20200929
Dear Parents, today we learn our new words:
- nose
-eye
We played "point game" to encourage the kids to say the words. 



20200930
Dear Parents, today we reviewed all of our new content from this week:
- eye
- ear
- nose
- mouth
We also reviewed our new sentence structure:
- This is my...(nose).



20201009
Dear Parents, today we reviewed all of our new content from this week:
- eye
- ear
- nose
- mouth
We also learn new sentence structure:
- I have two eyes .



20201010
Dear Parents, today we reviewed all of our new content from this week:
- eye
- ear
- nose
- mouth
We also review sentence structures:
- This is my nose. 
- I have two eyes .

"""


paragraphs = text.split('\n\n\n')

print(len(paragraphs))

all_words = set()
all_sentences = set()
rs = []
for p in paragraphs:
    p = p.strip()
    if not p:
        continue
    lines = p.splitlines()
    flag = 1
    words = []
    sentences = []
    day = lines[0]
    new_words = []
    new_sentences = []
    for line in lines:
        if line.startswith('-'):
            item = line[1:].strip()
            if flag <= 2:
                flag = 2
                words.append(item)
                if item not in all_words:
                    new_words.append(item)
                    all_words.add(item)
            else:
                sentences.append(item)
                if item not in all_sentences:
                    new_sentences.append(item)
                    all_sentences.add(item)
        elif flag == 2:
            flag = 3

    new_words = '<br>'.join(new_words)
    new_sentences = '<br>'.join(new_sentences)
    rs.append({'day': day, 'words': words, 'sentences': sentences, 'paragraph': p, 'new_words': new_words, 'new_sentences': new_sentences})

pprint.pprint(rs)

page = step.Template(html).expand({'rs': rs})

open('olion.html', 'wb').write(page.encode('utf8'))

