"""
Ον/νυμο : Ιωάννης Κογχυλάκης
     ΑΜ : 321/2013077
"""
import random # import την συνάρτηση random καθώς θα την χρησιμοποιήσω στη συνέχεια
noumera = []  # Αρχικοποιώ τις δύο λίστες
klirwsi = []
count = 0     # Ορίζω έναν μετρητή που θα χρειαστεί για να μετρήσουμε πόσα νούμερα βρήκε ο χρήστης
"""
*    Η συγκεκριμένη while είναι δικές μου επιλογής καθώς δεν αναφερόταν στην εργασία. Την έβαλα να πιάνει όλο
* το πρόγραμμα και έδωσα με ένα input την επιλογή στο χρήστη να επιλέξει με ένα y ή ένα n αν θέλει να ξαναπαιξει ή οχι.
"""
while True:   
  kerdos = ((0,2.5),
            (0,1,5),
            (0,0,2.5,25),
            (0,0,1,4,100),
            (0,0,0,2,20,450),
            (0,0,0,1,7,50,1600),
            (0,0,0,1,3,20,100,5000),
            (0,0,0,0,2,10,50,1000,15000),
            (0,0,0,0,1,5,25,200,4000,40000),
            (2,0,0,0,0,2,20,80,500,10000,100000),
            (2,0,0,0,0,1,10,50,250,1500,15000,50000),
            (4,0,0,0,0,0,5,25,150,1000,2500,25000,1000000)) # Δήλωση της πλειάδας για τα κέρδη
  while True:                       # Μια while για το πόσους αριθμούς θέλει να παίξει ο χρήστης και έλεγχος των δεδομένων που εισήγαγε.
    arithmoi=int(input("Με πόσους αριθμούς επιλέγεις να παίξεις (στο διάστημα 1-12); ")) 
    if 1<=arithmoi<=12:             # Αν ο αριθμός που έδωσε είναι στο διάστημα 1-12 τότε κάνει break και βγαίνει από την while
      break
    else:                           # Αλλίως βγάζει μήνυμα λάθους και αρχίζει ξανά η παραπάνω while.
      print("Ο αριθμός που έδωσες δεν είναι στο διάστημα [1-12] προσπάθησε ξανά")
  for i in range(0,arithmoi,1):     # For από το 0 έως το νούμερο που έδωσε ο χρήστης για το πόσο νούμερα θέλει να επιλέξει με βήμα 1
    while True:                     # While για την εισαγωγή και την σωστή δήλωση των αριθμών.
      print("Δώσε τον",i+1,"αριθμό (από 1 έως 80) : ",end="")
      giv=int(input())              # Αρχικά ο χρήστης δίνει έναν αριθμό ο οποίος αποθηκεύεται στη μεταβλητή giv
      if 1<=giv<=80:                # Aν ο αριθμός που έδωσε ο χρήστης είναι στο διάστημα [1-80] τότε μπές στην παρακάτω if
        if giv in noumera:          # όπου εδώ γίνεται έλεγχος για το αν ο χρήστης επιλέξει έναν αριθμό που έχει ήδη επιλέξει προηγουμένος
          print("Ο αριθμός",giv,"υπάρχει ήδη, δεν μπορείς να τον επιλέξεις ξανά. Δώσε άλλον") # Αν τον έχει ξαναεπιλέξει βγάλε μήνυμα λάθους
        else:                       # Αν δεν τον έχει ξαναεπιλέξει 
          noumera.insert(i,giv)     # Κάνει insert στη θέση i το νούμερο giv και με το break βγαίνει απο την while.
          break
      else:                         # Αν έχει δώσει κάποιο νούμερο εκτός διαστήματος εμφανίζει μήνυμα λάθους και ξαναμπαίνει στην while
        print("Οι αριθμοί θα πρέπει να είναι από 1 έως 80")
  noumera.sort()                    # Ταξινομεί τον πίνακα, για να φαίνονται καλύτερα όλα τα στοιχεία της λίστας και ακριβώς απο κάτω τα εμφανίζει.
  print("Τα νούμερα που επέλεξες είναι :",noumera)
  while True:                       # while επενάληψη για την εισαγωγή και τον έλεγχο του ποσού συμμετοχής από τον χρήστη
    poso = int(input("Επέλεξε το ποσό συμμετοχής (1,2,5 ή 10 ευρώ) : "))
    if poso==1 or poso==2 or poso ==5 or poso==10:
      break                         # Αν το ποσό που έδωσε ο χρήστης είναι 1 ή 2 ή 5 ή 10 τότε βγές απο την while
    else:                           # αλλιώς εμφάνισε μήνυμα λάθους και ξαναμπένει στη while για να ξαναδώσει ποσό
      print("Τα δυνατά ποσά είναι 1,2,5,10 ευρώ")
  for i in range(0,20,1):           # Επανάληψη για την επιλογή τυχαίων αριθμών απο το σύστημα.
    while True:                     # Η χρησιμότητα της while αυτής είναι για να ελέγχει άν ο αριθμός που διάλεξε το σύστημα έχει ξαναεπιλεγεί.
      ran=random.randint(1,80)      # Επιλογή αριθμούς από το 1 έως το 80 με την χρήση της rand.randint
      if ran not in klirwsi:        # Αν ο αριθμός που επέλεξε το σύστημα δεν υπάρχει ήδη μέσα στην υπάρχουσα λίστα τότε 
        klirwsi.insert(i,ran)       # βάλε στη λίστα klirwsi στη θέση i τον αριθμό αυτόν, και στη συνέχεια βγές απο την while
        break
  klirwsi.sort()                    # Ταξινόμηση του πίνακα για να φαίνεται καλύτερα στον χρήστη και στη συνέχεια τον εμφανίζει
  print("Οι αριθμοί που κληρώθηκαν είναι : ",klirwsi)
  for i in range(0,arithmoi,1):     # Επανάληψη για την καταμέτρηση των αριθμών που βρήκε ο χρήστης.
    if noumera[i] in klirwsi:       # Αν το νούμερο στη θέση i της λίστα noumera βρισκεται κάπου στη λίστα klirwsi
      count+=1                      # Τότε ανέβασε την μεταβλητή count ανά μια μονάδα.
  print("Πέτυχες",count,"αριθμούς") # Εμφανίζει πόσα στοιχεία βρήκε ο χρήστης.
  """
  *   Στη παρακάτω γραμμή εκτυπώνεται πόσο χρήματα κέρδισε ο παίκτης. Για να γίνει αυτο παίρνει τη μεταβλητη poso και την πολλαπλασιάζει με
  * την τιμή από τον πίνακα kerdos. Για να μπορέσουμε να χρησιμοποίησουμε τον πίνακα σωστά θα πρέπει να βρούμε πίο κελί θα πρέπει να γυρίσει για
  * να πολλαπλασιαστεί με το ποσό. Οι στήλες του πίνακα είναι πόσους αριθμούς επέλεξε να παίξει και οι γραμμές είναι πόσα νούμερα βρήκε
  * σωστά. Το νούμερο arithmoi που χρησιμοποιούμε για τις στήλες θα πρέπει να αφαιρεθεί κατά 1 γιατί ο πίνακας είναι απο 0-11 ενώ ο χρήστης
  * έδωσε τιμές απο 1-12.
  """
  print("Το ποσό που κέρδισες είναι : ",poso*kerdos[arithmoi-1][count])
  again=input("Θές να ξαναπαίξεις ? [y for yes /n for no] : ") # Επιλέγει αν ο χρήστης θέλει να ξαναπαίξει ξανά η όχι
  if again=='n':                    # Αν ο χρήστης έδωσε n ως απάντηση τότε βγες απο την μεγάλη while. Που σημαίνει και το τέλος του προγράμματος.
    break
  
  
  
  
  
