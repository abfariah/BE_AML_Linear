#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#EXAMEN 2021 : Cet examen est composé de deux exercices realises idealement en binome et
#eventuellement seul. Les réponses seront données dans un notebook qui indiquera clairement
# les noms et prenoms du binome d'eleves, ou de l'eleve, l'ayant realise.
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Exercice 1 : Un medecin souhaite mettre en lien l'impact de differentes variables mesurees sur
#un 'score' qu'il estime pour quantifier le niveau d'une maladie. Les donnees sont
#sauvegardees dans le fichier 'obs2021_1.csv'. Idealement, il souhaiterait que seul un
#sous ensemble de ces variables permette d'expliquer le score.
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import pandas
import numpy as np
import matplotlib.pyplot as plt

dataframe=pandas.read_csv("./obs2021_1.csv",sep=';')

listColNames=list(dataframe.columns)


XY=dataframe.values
ColNb_Y=listColNames.index('score')


Y=XY[:,ColNb_Y].reshape((XY.shape[0],1))   #reshape is to make sure that Y is a column vector
X = np.delete(XY, ColNb_Y, 1)

listColNames.pop(ColNb_Y)     #to make it contains the column names of X only


for Col in range(len(listColNames)):
  plt.plot(X[:,Col],Y[:],'.')
  plt.xlabel(listColNames[Col])
  plt.ylabel('score')
  plt.show()



#QUESTION 1.1 : Observez les donnees unes par unes. Est-ce que vous identifiez visuellement des liens entre
#certaines variables et la variable 'score'. Si oui, lesquels ?


#QUESTION 1.2 :   On se demande si il est possible de predire le niveau de 'score' à partir d'une
#               seule des variables 'var02', 'var09' ou 'var16'.
#
#QUESTION 1.2.1 : Effectuez une regression lineaire simple entre 'score' et chacune de ces
#               variables.  Toutes les donnees seront utilisees pour l'apprentissage. Evaluez alors la
#               qualité des predictions, sur toutes les donnees, l'aide de la moyenne de l'erreur de
#               prediction sur toutes les donnees, l'aide de la moyenne de l'erreur de prediction au
#               carre (MSE). Quel est le risque potentiel en utilisant cette stratégie de validation
#               de l'apprentissage ?
#
#QUESTION 1.2.2 : Evaluez a quel point les predictions sont stables a l'aide d'une methode de validation croisee
#               de type 5-folds.
#
#QUESTION 1.2.3 : Peut-on enfin dire si on observe une relation significative entre 'score'
#               et (independament) 'var02', 'var09' ou bien 'var16'. On peut le valider
#               a l'aide d'un test d'hypothese dont on decrira la procedure.



#QUESTION 1.3 : On s'interesse maintenant au lien entre la variable 'score' et 'var12'.
#               On peut remarquer que ces donnees contiennent deux valeurs aberrantes.
#
#QUESTION 1.3.1 : Definissez une procedure pour detecter automatiquement deux donnees aberrantes dans
#               un jeu de donnees.
#
#QUESTION 1.3.2 : Nous supprimerons dans la suite de cet exercice les deux observations qui sont aberrantes sur
#               la variable 'var12'. Comment auriez-vous traite ces observations si vous aviez absolument
#                voulu preserver l'information qu'elles contiennent dans les autres variables ?


#QUESTION 1.4 :   Une fois les deux observations aberrantes de 'var12' supprimees, on souhaite selectionner les
#               variables de 'X' qui permettent de prédire au mieux 'score' a l'aide de la
#               regression multiple regularisee.

#QUESTION 1.4.1 : Quelle strategie vous semble la plus appropriee pour selectionner les variables les plus
#               pertinentes ? Quel pretraitement allez-vous de meme effectuer sur les donnees.

#QUESTION 1.4.2 : Effectuez la procedure de selection des variables optimales en parametrant a la main le poids
#               entre la qualite de prediction et le niveau de regularisation.

#QUESTION 1.4.3 : Effectuez la procedure automatique de parametrisation de ce poids, de sorte a ce q'un maximum
#               de trois variables soit typiquement selectionne et que la qualite de prediction soit optimale.
#               Quelle methode de validation croisee vous semble la plus raisonnable ici ? La selection des
#               variables est-elle stable ?




#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Exercice 2 : Lors d'essais cliniques, un groupe pharmaceutique souhaite savoir si la
#              concentration d'un produit dans un traitement pour la vue a le meme effet
#              sur deux sous populations. Les resultats d'observations sont regroupes dans
#              le fichier obs2021_2.csv. Dans chacun des groupes, on supposera que le lien
#              entre la concentration du produit et l'efficacite du traitement est lineaire.
#              Definissez et appliquez une methodologie pour tester si l'impact de cette
#              concentration est similaire dans les deux groupes ?
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import pandas
import numpy as np
import matplotlib.pyplot as plt

dataframe=pandas.read_csv("./obs2021_2.csv",sep=',')

plt.figure(figsize=(7,7))
plt.scatter(dataframe['concentration'], dataframe['Efficacite'], c=['r' if t == 'Groupe_1' else 'b' for t in dataframe['Groupe']])
plt.xlabel("concentration")
plt.ylabel("Efficacite")
plt.show()

print(2)
