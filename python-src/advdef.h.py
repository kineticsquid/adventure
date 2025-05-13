
# /*	header ADVDEF.H						*\
# \*	WARNING: GLOBAL variable allocations for adventure	*/

# /*
# 	Database variables
# */

# Added this to create an array of a specific size to allow for references to structs. numpy array creation is
# insufficient
def init_array(n, value=None):
    a = []
    for i in range(n):
        a.append(value)
    return a

travel = init_array(MAXTRAV)

#ifndef BUILTIN
# FILE *fd1, *fd2, *fd3, *fd4;
#endif

actmsg = init_array(32, value=0) # /* action messages	*/

# /*
# 	English variables
# */

verb = 0 
object = 0
motion = 0

word1 = init_array(WORDSIZE)
word2 = init_array(WORDSIZE)


# /*
# 	Play variables
# */
turns = 0
loc = 0
oldloc = 0
oldloc2 = 0
newloc = 0  #/* location variables */
cond = init_array(MAXLOC, value=0)		 # /* location status	*/
place = init_array(MAXOBJ, value=0)		 # /* object location	*/
fixed = init_array(MAXOBJ, value=0)		 # /* second object loc	*/
visited = init_array(MAXLOC, value=0)		 # /* >0 if has been here	*/
prop = init_array(MAXOBJ, value=0)		 # /* status of object	*/
tally = 0 
tally2 = 0		 # /* item counts		*/
limit = 0			 # /* time limit		*/
lmwarn = 0			 # /* lamp warning flag	*/
wzdark = 0
closing = 0
closed = 0     # /* game state flags	*/
holding = 0			 # /* count of held items	*/
detail = 0			 # /* LOOK count		*/
knfloc = 0			 # /* knife location	*/
clock1 = 0
clock2 = 0
panic = 0	 # /* timing variables	*/
dloc = init_array(DWARFMAX, value=0)		 # /* dwarf locations	*/
dflag = 0			 # /* dwarf flag		*/
dseen = init_array(DWARFMAX, value=0)		 # /* dwarf seen flag	*/
odloc = init_array(DWARFMAX, value=0)		 # /* dwarf old locations	*/
daltloc = 0			 # /* alternate appearance	*/
dkill = 0			 # /* dwarves killed	*/
chloc = 0
chloc2 = 0		 # /* chest locations	*/
bonus = 0			 # /* to pass to end	*/
numdie = 0			 # /* number of deaths	*/
object1 = 0			 # /* to help intrans.	*/
gaveup = 0			#  /* 1 if he quit early	*/
foobar = 0			#  /* fie fie foe foo...	*/
saveflg = 0			 # /* if game being saved	*/
dbugflg = 0			 # /* if game is in debug	*/
lastglob = 0			 # /* to get space req.	*/
