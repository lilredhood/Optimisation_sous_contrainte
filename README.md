# Optimisation_sous_contrainte

Dossier Contraintes_inegalite (https://en.wikipedia.org/wiki/Karush%E2%80%93Kuhn%E2%80%93Tucker_conditions) : 
  - Optimisation sous contraintes de la fonction quadratique $J(x, y) = 2x^2 + 3xy + 2y^2$ définie sur le cadran $Q = ${ $(x, y) ~~ \vert ~~ x \leq -\frac{1}{2}, ~ y \leq -\frac{1}{2} $}.
  - Résolution numérique par méthode de descente de gradient projeté
  - Résolution numérique par méthode de descente de gradient du problème avec pénalisation
 
 Dossier Contraintes_egalite (https://en.wikipedia.org/wiki/Lagrange_multiplier) : 
  - On considère le problème de l’optimisation d’un portefeuille. On appelle $J$, la fonction définie sur $\mathbf{R}$ par 
  $J(x) = \frac{1}{2} \langle x, Ax \rangle_{\mathbf{R}^n}$
  On désigne par $K$, l’ensemble des contraintes, soit $K = \lbrace x \in \mathbf{R}^n \vert \langle x, u \rangle = 1, ~ \langle x, e \rangle = r_0 \rbrace$. L’objectif est de résoudre numériquement le problème $\inf_{x \in K} J(x)$. Nous allons ré-écrire notre ensemble $K$ de la façon suivante : $K = \lbrace x \in \mathbf{R}^n \vert Cx = f \rbrace$ avec : 

```math
 C = \begin{pmatrix} 1 & \cdots & 1 \\ e_1 & \cdots & e_n \end{pmatrix} ~ \text{et} ~~ f = (1, r_0)^T
```
  - Théorème des extrémas liés
  - Algorithme d'Uzuwa
