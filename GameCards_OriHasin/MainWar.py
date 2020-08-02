from GameCards_OriHasin.CardGame import CardGame

#מודול שבו מתרחש התוכנית הראשית
#AmoundRound,maxIndex , listcards = רשימה של קלפים בסיבוב
Game=CardGame()
AmountRound=0
for y in range(1,6): #לולאת המשחק - 5 סיבובים
    listcards = []
    for i in Game.listPlayers: # לולאת שליפת קלפים ועדכון סכומים בכל סיבוב
        listcards.append(i.getCard())
        i.reduceAmount(100*y)
    AmountRound+=(100*y)*4
    if listcards[0]>listcards[1]: #בודק את הקלף הגדול ביותר ( שימוש בפונקצית __gt__)
        maxcard1=listcards[0]
        maxIndex=0
    else:
        maxcard1=listcards[1]
        maxIndex=1
    if listcards[2]>listcards[3]:
        maxcard2=listcards[2]
        maxIndex2=2
    else:
        maxcard2=listcards[3]
        maxIndex2=3
    if maxcard1>maxcard2:
        Game.listPlayers[maxIndex].addAmount(AmountRound)  #הוספת סכום בקופת סיבוב לשחקן בעל הקלף הזוכה
        print(f'The cards in round: {listcards} , The Winner Card : {listcards[maxIndex]} ')
    else:
        Game.listPlayers[maxIndex2].addAmount(AmountRound)  #הוספת סכום בקופת סיבוב לשחקן בעל הקלף הזוכה
        print(f'The cards in round: {listcards} , The Winner Card : {listcards[maxIndex2]} ')

maxAmount=0
for i in range(len(Game.listPlayers)): #בודק את השחקן הזוכה
    if Game.listPlayers[i].Amount>maxAmount:
        maxAmount=Game.listPlayers[i].Amount
        indexAmount=i
print(f'The Winner in the game is: {Game.listPlayers[indexAmount]}')


