# P_A_project_1
Python Academy project 1 - Text analyser - první projekt na Python akademii na Engeto.

## Popis projektu
V tomto projektu bylo cílem vytvořit textový analyzátor - program, který se bude umět prokousat libovolně dlouhým textem a zjistit o něm různé informace. 

## Program obsahuje
- importování seznamu textových souborů z jiného souboru `task_template.py`
- vyžádání si od uživatele přihlašovacího jména a hesla
    ```
    users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
    ```
- zjištění, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,
  - pokud je registrovaný, pozdraví jej a umožni mu analyzovat texty,
  - pokud není registrovaný, upozorní jej a ukonči program
- volbu uživatele mezi texty, uloženými v souboru `task_template.py`:
- pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí
- pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí
- pro vybraný text spočítá následující statistiky:
    - počet slov,
    - počet slov začínajících velkým písmenem,
    - počet slov psaných velkými písmeny,
    - počet slov psaných malými písmeny,
    - počet čísel (ne cifer),
    - sumu všech čísel (ne cifer) v textu.
  
- zobrazení jednoduchého sloupcového grafu, který bude reprezentovat četnost různých délek slov v textu
    ```
    ----------------------------------------
    LEN|   OCCURANCES  |NR.
    ----------------------------------------
      1|*              |1
      2|***********    |11
      3|***************|15
      4|*********      |9
      5|**********     |10
      6|*****          |5
      7|***********    |11
      8|******         |6
      9|***            |3
     10|***            |3
    ```
