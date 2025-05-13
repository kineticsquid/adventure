# /*	header ADVENT.H						*\
# \*	WARNING: HEADER file for all adventure modules		*/

MAXOBJ = 100		# /* max # of objects in cave	*/
MAXWC = 306		# /* max # of adventure words	*/
MAXLOC = 140		# /* max # of cave locations	*/
WORDSIZE = 20		# /* max # of chars in commands	*/
MAXMSG = 201		# /* max # of long location descr	*/

MAXTRAV = (16 + 1)  # /* max # of travel directions from loc  */
			    #   /* +1 for terminator travel[x].tdest=-1 */
DWARFMAX = 7	      # /* max # of nasty dwarves	*/
MAXDIE = 3	      # /* max # of deaths before close	*/
MAXTRS = 79	      # /* max # of			*/

# /*
# 	Object definitions
# */
KEYS = 1
LAMP = 2
GRATE = 3
CAGE = 4
ROD = 5
ROD2 = 6
STEPS = 7
BIRD = 8
DOOR = 9
PILLOW = 10
SNAKE = 11
FISSURE = 12
TABLET = 13
CLAM = 14
OYSTER = 15
MAGAZINE = 16
DWARF = 17
KNIFE = 18
FOOD = 19
BOTTLE = 20
WATER = 21
OIL = 22
MIRROR = 23
PLANT = 24
PLANT2 = 25
AXE = 28
DRAGON = 31
CHASM = 32
TROLL = 33
TROLL = 34
BEAR = 35
MESSAGE = 36
VEND = 38
BATTERIES = 39
NUGGET = 50
COINS = 54
CHEST = 55
EGGS = 56
TRIDENT = 57
VASE = 58
EMERALD = 59
PYRAMID = 60
PEARL = 61
RUG = 62
SPICES = 63
CHAIN = 64

# /*
# 	Verb definitions
# */
NULLX = 21
BACK = 8
LOOK = 57
CAVE = 67
ENTRANCE = 64
DEPRESSION = 63

# /*
# 	Action verb definitions
# */
TAKE = 1
DROP = 2
SAY = 3
OPEN = 4
NOTHING = 5
LOCK = 6
ON = 7
OFF = 8
WAVE = 9
CALM = 10
WALK = 11
KILL = 12
POUR = 13
EAT = 14
DRINK = 15
RUB = 16
THROW = 17
QUIT = 18
FIND = 19
INVENTORY = 20
FEED = 21
FILL = 22
BLAST = 23
SCORE = 24
FOO = 25
BRIEF = 26
READ = 27
BREAK = 28
WAKE = 29
SUSPEND = 30
HOURS = 31
LOG = 32
LOAD = 33

# /*
# 	BIT mapping of "cond" array which indicates location status
# */
LIGHT = 1
WATOIL = 2
LIQUID = 4
NOPIRAT = 8
HINTC = 16
HINTB = 32
HINTS = 64
HINTM = 128
HINT = 240

# /*
# 	Structure definitions
# */
# struct wac {
# 	char *aword;
# 	int   acode;
# };

# struct trav {
# 	int   tdest;
# 	int   tverb;
# 	int   tcond;
# };

#include "proto.h"
#include "config.h"
